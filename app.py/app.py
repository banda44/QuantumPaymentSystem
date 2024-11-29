from flask import Flask, jsonify

app = Flask(__name__)

# Sample endpoint for testing
@app.route('/')
def hello_world():
    return 'Welcome to the Quantum Payment System!'

# Sample API endpoint to get account balance
@app.route('/balance/<account_id>', methods=['GET'])
def get_balance(account_id):
    # Sample account data (in real scenarios, this should be fetched from a database or blockchain)
    accounts = {
        'account1': 5.0,  # Example: 5 Quantum Units
        'account2': 1.0,  # Example: 1 Quantum Unit
        'account3': 0.5   # Example: 0.5 Quantum Units
    }
    
    balance = accounts.get(account_id, 'Account not found')
    
    return jsonify({
        'account_id': account_id,
        'balance': balance
    })

# Sample API endpoint to perform a transaction
@app.route('/transfer/<from_account>/<to_account>/<amount>', methods=['GET'])
def transfer(from_account, to_account, amount):
    # Sample logic for transaction (this is a mock implementation)
    accounts = {
        'account1': 5.0,
        'account2': 1.0,
        'account3': 0.5
    }

    if from_account not in accounts or to_account not in accounts:
        return jsonify({
            'message': 'Invalid account(s)'
        })

    if accounts[from_account] < float(amount):
        return jsonify({
            'message': 'Insufficient balance'
        })

    # Perform transaction (mock)
    accounts[from_account] -= float(amount)
    accounts[to_account] += float(amount)

    return jsonify({
        'message': 'Transaction successful',
        'from_account': from_account,
        'to_account': to_account,
        'amount': amount,
        'new_from_balance': accounts[from_account],
        'new_to_balance': accounts[to_account]
    })

if __name__ == '__main__':
    app.run(debug=True)
