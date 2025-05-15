from datetime import datetime
from transaction import create_mempool
from chain import Blockchain
from block import Block
import time

# Create a block with dummy transactions
block = Block(
    index=0,
    transaction=[{"sender": "Alice", "receiver": "Bob", "amount": 1.0}],  # dict transaction
    timestamp=datetime.now(),
    previous_hash="0"
)

start_time = time.time()

print(" Mining block...")
block.mine_block(difficulty=1)

end_time = time.time()

print("\n Block mined!")
print("Hash:", block.hash)
print("Nonce:", block.nonce)
print(f" Time: {end_time - start_time:.2f} seconds")
