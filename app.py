from flask import Flask, render_template, request, redirect, url_for
from chain import Blockchain
from transaction import create_mempool

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'

# Global state — singleton blockchain instance
blockchain = None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/init')
def init_blockchain():
    global blockchain
    blockchain = Blockchain()
    return redirect(url_for('status'))

@app.route('/generate_tx', methods=['GET', 'POST'])
def generate_tx():
    if request.method == 'POST':
        n = int(request.form['num_txs'])
        txs = create_mempool(n)
        for tx in txs:
            blockchain.add_transaction_to_pool(tx)
        return redirect(url_for('status'))
    return render_template('generate_tx.html')

@app.route('/mine_block', methods=['GET', 'POST'])
def mine_block():
    if request.method == 'POST':
        miner = request.form['miner']
        tx_limit = int(request.form['tx_limit'])

        selected_txs = blockchain.mempool[:tx_limit]
        blockchain.mempool = blockchain.mempool[tx_limit:]

        blockchain.add_block(selected_txs, miner_address=miner, difficulty=2)
        return redirect(url_for('status'))

    return render_template('mine_block.html')

@app.route('/status')
def status():
    return render_template(
        'status.html',
        chain=blockchain.chain,
        mempool=blockchain.mempool,
        balances=blockchain.balances
    )

if __name__ == '__main__':
    app.run(debug=True)
