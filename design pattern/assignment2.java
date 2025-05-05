class Car{
    private String modelName;
    private String engineType;
    private String color;
    private String transmission;
    private boolean sunroof;
    private boolean infotainmentSystem;

    private Car(carBuilder builder){
        this.modelName = builder.modelName;
        this.engineType = builder.engineType;
        this.color = builder.color;
        this.transmission = builder.transmission;
        this.sunroof = builder.sunroof;
        this.infotainmentSystem = builder.infotainmentSystem;
    }

    @Override
    public String toString(){
        return "Model Name: " + modelName +"\n"+
                "Engine Type: "+engineType +"\n"+
                "Color: "+color+"\n"+
                "Transmission: "+transmission+"\n"+
                "Sunroof: " +(sunroof ? "Yes" : "No") + "\n" +
               "Infotainment System: " + (infotainmentSystem ? "Yes" : "No");
    }

    public static class carBuilder{
        private String modelName = "default model";
        private String engineType = "petrol";
        private String color = "Black";
        private String transmission = "Manual";
        private boolean sunroof = false;
        private boolean infotainmentSystem = false;

        public carBuilder setModelName(String modelName) {
            this.modelName = modelName;
            return this;
        }

        public carBuilder setEngineType(String engineType) {
            this.engineType = engineType;
            return this;
        }

        public carBuilder setColor(String color) {
            this.color = color;
            return this;
        }

        public carBuilder setTransmission(String transmission) {
            this.transmission = transmission;
            return this;
        }

        public carBuilder setSunroof(boolean sunroof) {
            this.sunroof = sunroof;
            return this;
        }

        public carBuilder setInfotainmentSystem(boolean infotainmentSystem) {
            this.infotainmentSystem = infotainmentSystem;
            return this;
        }
        public Car build(){
            return new Car(this);
        }
    }
}


public class assignment2 {
    public static void main(String[] args) {
        Car defaultCar = new Car.carBuilder().build();
        System.out.println("Default Car Configuration:\n" + defaultCar + "\n");

        Car customCar = new Car.carBuilder()
                .setModelName("Tesla Model 3")
                .setEngineType("Electric")
                .setColor("Midnight Silver")
                .setTransmission("Automatic")
                .setSunroof(true)
                .setInfotainmentSystem(true)
                .build();

        System.out.println("Customized Car Configuration:\n" + customCar);
    }
}
