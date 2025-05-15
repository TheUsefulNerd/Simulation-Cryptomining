import json
import hashlib

class Block:
    def __init__(self, index, timestamp, transaction, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = None
        self.merkle_root = self.compute_merkle_root()

    def to_dict(self):
        return {
        'index': self.index,
        'transaction': self.transaction,
        'timestamp': str(self.timestamp),
        'previous_hash': self.previous_hash,
        'nonce': self.nonce  
    }
    
    def compute_hash(self):
        block_string = json.dumps(self.to_dict(), sort_keys=True, default=str).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def mine_block(self, difficulty):
        print("Started mining block...")
        prefix = '0' * difficulty
        max_nonce = 1_000_000
        while self.nonce < max_nonce:
            computed_hash = self.compute_hash()
            if computed_hash.startswith(prefix):
                self.hash = computed_hash
                print(f"Block mined! Nonce: {self.nonce} | Hash: {self.hash}")
                break
            else:
                self.nonce += 1
                if self.nonce % 10000 == 0:
                    print(f"🔄 Trying nonce: {self.nonce} | Hash: {computed_hash}")
        else:
            
            print(f"Failed to mine block after {max_nonce} attempts")
        print("Finished mining block!")




    def compute_merkle_root(self):
        tx_hashes = [hashlib.sha256(str(tx).encode()).hexdigest() for tx in self.transaction]

        if not tx_hashes:
           return None
        
        while len(tx_hashes) > 1:
            if len(tx_hashes) % 2 != 0:
                tx_hashes.append(tx_hashes[-1])

            tx_hashes = [
            hashlib.sha256((tx_hashes[i] + tx_hashes[i + 1]).encode()).hexdigest()
            for i in range(0, len(tx_hashes), 2)
        ]

        return tx_hashes[0]
    



