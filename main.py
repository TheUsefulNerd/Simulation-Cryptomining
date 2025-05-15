from chain import Blockchain
from transaction import create_mempool

# Initialize blockchain
bc = Blockchain()

# Print genesis block info
genesis_block = bc.chain[0]
print("Genesis Block Created")
print(f"Index: {genesis_block.index}")
print(f"Hash: {genesis_block.hash}")
print(f"Previous Hash: {genesis_block.previous_hash}")
print(f"Transactions: {len(genesis_block.transaction)}")
print(f"Nonce: {genesis_block.nonce}")

print("\nInitial Balances:")
for user, balance in bc.balances.items():
    print(f"{user}: {balance:.4f}")

# Generate transactions and add them to the mempool
txs = create_mempool(n=10)
for tx in txs:
    bc.add_transaction_to_pool(tx)

print("\nAll Transactions Added to Mempool:")
for i, tx in enumerate(bc.mempool, 1):
    print(f"{i}. {tx['sender']} -> {tx['receiver']} | {tx['amount']:.4f}")

# Select a subset of transactions to include in the next block
pending_txs = bc.mempool[:5]
bc.mempool = bc.mempool[5:]  # Remove them from the pool

# Mine a new block with selected transactions
print("\n Mining new block with Alice as miner...")
bc.add_block(pending_txs, miner_address="Alice", difficulty=2)

# Get the new block and print info
new_block = bc.get_last_block()
print("\n New Block Mined!")
print(f"Index: {new_block.index}")
print(f"Hash: {new_block.hash}")
print(f"Previous Hash: {new_block.previous_hash}")
print(f"Nonce: {new_block.nonce}")
print(f"Total Transactions: {len(new_block.transaction)}")

# Show all transactions (including reward)
print("\n Transactions in the New Block:")
for i, tx in enumerate(new_block.transaction, 1):
    print(f"{i}. {tx['sender']} -> {tx['receiver']} | {tx['amount']:.4f}")

# Print final balances
print("\nUpdated Balances After Mining:")
for user, balance in bc.balances.items():
    print(f"{user}: {balance:.4f}")

# Mine second block with remaining transactions
if bc.mempool:
    print("\nMining second block with Miner1 as miner...")
    remaining_txs = bc.mempool.copy()  # Snapshot of remaining txs
    bc.add_block(remaining_txs, miner_address="Miner1", difficulty=2)

    second_block = bc.get_last_block()
    print("\nSecond Block Mined!")
    print(f"Index: {second_block.index}")
    print(f"Hash: {second_block.hash}")
    print(f"Previous Hash: {second_block.previous_hash}")
    print(f"Nonce: {second_block.nonce}")
    print(f"Total Transactions: {len(second_block.transaction)}")

    print("\nTransactions in second block:")
    for i, tx in enumerate(second_block.transaction, 1):
        print(f"{i}. {tx['sender']} -> {tx['receiver']} | {tx['amount']:.4f}")

else:
    print("\nNo transactions left in the mempool!")

# Show final balances
print("\nFinal Balances After Two Blocks:")
for user, balance in bc.balances.items():
    print(f"{user}: {balance:.4f}")
