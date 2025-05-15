from transaction import create_mempool
from block import Block
from datetime import datetime

class Blockchain:
    def __init__(self, chain=None):
        if chain is None:
            self.chain = []
            self.balances = {
                "Alice": 500,
                "Bob": 500,
                "Charlie": 500,
                "Miner1": 0,
                "Miner2": 0
            }
            self.create_genesis_block()
            self.mempool = []
        else:
            self.chain = chain
            self.balances = {}

    def create_genesis_block(self):
        genesis_block = Block(
            index=0,
            transaction=[],  # ✅ NO transactions
            timestamp=datetime.now(),
            previous_hash='0'
        )
        genesis_block.mine_block(difficulty=2)
        self.chain.append(genesis_block)

    def add_block(self, transactions, miner_address, difficulty=2):
        # ✅ Calculate total transaction fees
        total_fees = sum(tx.get('fee', 0) for tx in transactions)

        # ✅ Generate reward transaction including base reward and fees
        reward_tx = self.generate_reward_transaction(miner_address, reward_amount=50 + total_fees)

        # ✅ Combine reward and normal transactions
        all_txs = [reward_tx] + transactions

        previous_block = self.chain[-1]
        new_block = Block(
            index=previous_block.index + 1,
            transaction=all_txs,
            timestamp=datetime.now(),
            previous_hash=previous_block.hash
        )

        print(f"\nMining Block {new_block.index} by {miner_address} with {len(all_txs)} transactions")
        new_block.mine_block(difficulty)
        print(f"Block {new_block.index} mined with hash: {new_block.hash}")
        print(f"Merkle Root: {new_block.merkle_root}")

        self.chain.append(new_block)

        print("\nUpdating balances...")
        self.update_balances(all_txs)

        print(" Transactions in Block:")
        for tx in all_txs:
            print(f" - {tx['sender']} -> {tx['receiver']} | Amount: {tx['amount']}")

        print("\n Updated Balances:")
        for user, balance in self.balances.items():
            print(f"{user}: {balance:.4f}")

    def get_last_block(self):
        return self.chain[-1]

    def is_chain_valid(self, difficulty=2):
        temp_balances = {user: 0 for user in self.balances}

        # Assume genesis block contains the starting balances
        temp_balances = self.balances.copy()

        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.previous_hash != previous.hash:
                print(f" Chain broken at block {i} (hash mismatch)")
                return False

            if current.hash != current.compute_hash():
                print(f" Chain tampered at block {i} (invalid hash)")
                return False

            if not current.hash.startswith('0' * difficulty):
                print(f" Proof-of-work invalid at block {i}")
                return False

            for tx in current.transaction:
                sender = tx['sender']
                receiver = tx['receiver']
                amount = tx['amount']

                if sender != 'SYSTEM':
                    if temp_balances.get(sender, 0) < amount:
                        print(f" Overspend detected at block {i} by {sender}")
                        return False
                    temp_balances[sender] -= amount

                temp_balances[receiver] = temp_balances.get(receiver, 0) + amount

        for user, bal in temp_balances.items():
            if abs(bal - self.balances.get(user, 0)) > 1e-6:
                print(f" Balance mismatch for user {user}: computed {bal}, recorded {self.balances.get(user, 0)}")
                return False

        print(" The chain is fully valid.")
        return True

    def update_balances(self, transactions):
        for tx in transactions:
            sender = tx['sender']
            receiver = tx['receiver']
            amount = tx['amount']

            if sender != 'SYSTEM':
                if self.balances.get(sender, 0) < amount:
                    print(f" Sender {sender} has insufficient balance!")
                    continue
                self.balances[sender] -= amount

            self.balances[receiver] = self.balances.get(receiver, 0) + amount

    def generate_reward_transaction(self, miner_address, reward_amount=50):
        return {
            "sender": "SYSTEM",
            "receiver": miner_address,
            "amount": reward_amount,
            "timestamp": str(datetime.now())
        }

    def add_transaction_to_pool(self, tx):
        if self.validate_transaction(tx):
            self.mempool.append(tx)
            return True
        else:
            print(f" Invalid transaction: {tx}")
            return False

    def validate_transaction(self, tx):
        required_keys = {"sender", "receiver", "amount"}
        if not required_keys.issubset(tx.keys()):
            return False

        if tx["sender"] != "SYSTEM" and self.balances.get(tx["sender"], 0) < tx["amount"]:
            return False

        if tx["amount"] <= 0:
            return False

        return True
