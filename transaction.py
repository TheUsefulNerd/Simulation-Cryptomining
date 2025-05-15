import random
import string


users = ["Alice", "Bob", "Charlie", "Miner1", "Miner2"]


def generate_wallet():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def create_transaction():
    sender = random.choice(users)
    receiver = random.choice([user for user in users if user != sender])
    amount = round(random.uniform(0.1, 5.0), 4)
    fee = round(random.uniform(0.00001, 0.1), 4)

    return {
        'sender': sender, 
        'receiver': receiver,
        'amount': amount,
        'fee': fee
    }

def create_mempool(n=20):
    return [create_transaction() for i in range(n)]

if __name__ == "__main__":
    txs = create_mempool()
    for tx in txs:
        print(tx)