import hashlib
import time

class Block:
  def __init__ (self, data, previous_hash):
    self.timestamp = time.time()
    self.data = data
    self.previous_hash = previous_hash
    self.nonce = 0
    self.hash = self.generate_hash()
  
  def generate_hash(self):
    block_contents = str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
    block_hash = hashlib.sha256(block_contents.encode()).hexdigest()
    return block_hash
  
  
  def mine_block(self, difficulty):
    while self.hash[:difficulty] != '0' * difficulty : 
      self.nonce += 1 
      self.hash = self.generate_hash()
    print("block mined")
  


class Blockchain:
  def __init__(self):
    self.chain = [self.create_genesis_block()]
    self.difficulty = 2
  
  def create_genesis_block(self):
    return Block("genesis block", "0")
  
  
  def add_block(self,new_block):
    new_block.previous_hash = self.chain[-1].hash
    new_block.mine_block(self.difficulty)
    self.chain.append(new_block)
  

bc = Blockchain()
block1 = Block("T1","")
bc.add_block(block1)

for block in bc.chain:
  print("Block data:", block.data)
  print("hash:",block.hash)
  
  




















