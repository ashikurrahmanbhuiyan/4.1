import hashlib
import datetime

class Block:
    def __init__(self, block_number, transactions, previous_hash, gas_limit, gas_used, miner):
        self.block_number = block_number
        self.timestamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.gas_limit = gas_limit
        self.gas_used = gas_used
        self.miner = miner
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = (
            str(self.block_number)
            + str(self.timestamp)
            + str(self.transactions)
            + str(self.previous_hash)
            + str(self.gas_limit)
            + str(self.gas_used)
            + str(self.miner)
        )
        return hashlib.sha256(data_string.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0", 0, 0, "Genesis Miner")

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        self.chain.append(new_block)

    def print_block(self, block):
        print("Block Number:", block.block_number)
        print("Timestamp:", block.timestamp)
        print("Transactions:", block.transactions)
        print("Previous Hash:", block.previous_hash)
        print("Gas Limit:", block.gas_limit)
        print("Gas Used:", block.gas_used)
        print("Miner:", block.miner)
        print("Hash:", block.hash)
        print("")

    def traverse_chain(self):
        for block in self.chain:
            self.print_block(block)

my_blockchain = Blockchain()

my_blockchain.add_block(Block(1, "Transaction 1", "", 1000000, 500000, "Miner 1"))
my_blockchain.add_block(Block(2, "Transaction 2", "", 2000000, 1500000, "Miner 2"))
my_blockchain.add_block(Block(3, "Transaction 3", "", 3000000, 2500000, "Miner 3"))

my_blockchain.traverse_chain()