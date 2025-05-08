import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Input, Lambda
from tensorflow.keras.optimizers import Adam
import numpy as np
import matplotlib.pyplot as plt

# Load CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalize pixel values to [0, 1]
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Convert labels to one-hot encoding
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# Data augmentation for training
datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)
datagen.fit(x_train)









# Define input shape
input_shape = (32, 32, 3)

# Create input layer
inputs = Input(shape=input_shape)

# Resize images to 224x224 for MobileNetV2
resized_inputs = Lambda(lambda x: tf.image.resize(x, [224, 224]))(inputs)

# Load pre-trained MobileNetV2 (without top layers)
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze the base model
base_model.trainable = False

# Add custom layers
x = base_model(resized_inputs, training=False)
x = GlobalAveragePooling2D()(x)  # Pool to reduce dimensions
x = Dense(128, activation='relu')(x)  # Fully connected layer
outputs = Dense(10, activation='softmax')(x)  # Output layer for 10 classes

# Create the model
model = Model(inputs, outputs)

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Model summary
model.summary()












# Train the model
history_transfer = model.fit(
    datagen.flow(x_train, y_train, batch_size=32),
    epochs=5,
    validation_data=(x_test, y_test),
    verbose=1
)

# Evaluate on test set
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"Transfer Learning Test Accuracy: {test_acc:.4f}")








# Unfreeze the last 20 layers
base_model.trainable = True
for layer in base_model.layers[:-20]:
    layer.trainable = False

# Recompile with a lower learning rate
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Fine-tune the model
history_finetune = model.fit(
    datagen.flow(x_train, y_train, batch_size=32),
    epochs=5,
    validation_data=(x_test, y_test),
    verbose=1
)

# Evaluate on test set
test_loss_finetune, test_acc_finetune = model.evaluate(x_test, y_test, verbose=0)
print(f"Fine-Tuning Test Accuracy: {test_acc_finetune:.4f}")









# Plot accuracy
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history_transfer.history['accuracy'], label='Transfer Train Acc')
plt.plot(history_transfer.history['val_accuracy'], label='Transfer Val Acc')
plt.plot(range(5, 10), history_finetune.history['accuracy'], label='Finetune Train Acc')
plt.plot(range(5, 10), history_finetune.history['val_accuracy'], label='Finetune Val Acc')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.show()
