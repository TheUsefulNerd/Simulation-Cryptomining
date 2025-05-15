# 🔗 Blockchain Simulation with Mining, Transactions & Web UI

A fully functional blockchain simulation implemented in Python with Flask. This project simulates core blockchain mechanics such as mining, transaction validation, mempool prioritization, mining rewards, balance tracking, and a dynamic web interface for visualization.

## 🧠 Project Highlights

* ⛏️ **Proof-of-Work Mining** with adjustable difficulty  
* 🧾 **Transaction Generation** with realistic fees and balances  
* 🧺 **Mempool** to manage pending transactions  
* 💰 **Mining Rewards + Fee Accumulation**  
* 🧾 **Wallet Balance Sheet** auto-updates per block  
* 🌐 **Web Interface** built using Flask  
* 📦 **Modular Design** using `transaction.py`, `block.py`, `chain.py`, and `app.py`  

---

## 📁 Project Structure

```
.
├── app.py                 # Flask app for simulation UI
├── transaction.py         # Wallet + transaction generation logic
├── block.py               # Block structure and mining logic
├── chain.py               # Blockchain class with chain state, mempool, balances
├── templates/             # HTML templates for the Flask app
│   ├── home.html
│   ├── status.html
│   ├── generate_tx.html
│   └── mine_block.html

```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/TheUsefulNerd/Simulation-Cryptomining.git
```

### 2. Install Dependencies

This project uses only Flask and standard Python libraries.

```bash
pip install flask
```

### 3. Start the Web App

```bash
python app.py
```

Open your browser and go to `http://127.0.0.1:5000/`

---

## 🧪 Features in Action

### 🔹 Initialize Blockchain

Creates the genesis block.

### 🔹 Generate Transactions

Adds random transactions (sender, receiver, amount, fee) to the mempool.

### 🔹 Mine Block

User can select the miner and number of transactions to include. The mined block is added to the chain and miner gets rewarded.

### 🔹 View Blockchain Status

Use `/status` to see:

* All blocks and their contents  
* Mempool (unmined transactions)  
* User balances (wallet view)  

---

## 🔐 Blockchain Design

* Each block contains:

    * Index  
    * Timestamp  
    * List of transactions (including miner reward)  
    * Nonce (solved using proof-of-work)  
    * Previous hash  
    * Hash of current block  

* Transactions contain:

    * Sender and receiver  
    * Amount and fee  
    * Automatically rewarded miner with 50 + total fees  

---

## 🧹 Possible Extensions

* 🔑 ECDSA-based digital signatures  
* 🗃️ File/database persistence  
* 📊 Visual block explorer or dashboard  
* 🌍 Network simulation with multiple nodes  

---

## 👨‍💼 Author

**\[Advait Joshi]**  
Machine Learning, Data Science and Blockchain Enthusiast  
GitHub: [TheUsefulNerd](https://github.com/TheUsefulNerd)  
LinkedIn: \[www.linkedin.com/in/advaitszone]  

---

## 🏁 License

MIT License - feel free to fork, build on, and share!  