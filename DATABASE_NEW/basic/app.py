from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/math', methods=['GET'])
def simple_math():
    # Get numbers and operation from GET parameters
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    operation = request.args.get('operation', type=str)
    
    if not num1 or not num2 or not operation:
        return jsonify({"error": "Missing parameters"}), 400

    result = None
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return jsonify({"error": "Division by zero"}), 400

    if result is not None:
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Invalid operation"}), 400
    

# Expanded currency rates with MKD and other currencies
currency_rates = {
    'USD_EUR': 0.85,
    'EUR_USD': 1.18,
    'USD_MKD': 54.0,  # Example rate, replace with the current rate
    'MKD_USD': 0.018,  # Example rate, replace with the current rate
    'EUR_MKD': 61.5,   # Example rate, replace with the current rate
    'MKD_EUR': 0.016,  # Example rate, replace with the current rate
    'GBP_USD': 1.35,
    'USD_GBP': 0.74,
    'EUR_GBP': 0.87,
    'GBP_EUR': 1.15,
    'CAD_USD': 0.79,
    'USD_CAD': 1.27,
    # Add more pairs as necessary
}

@app.route('/convert', methods=['GET'])
def convert_currency():
    amount = request.args.get('amount', type=float)
    from_currency = request.args.get('from', type=str).upper()
    to_currency = request.args.get('to', type=str).upper()
    
    if not amount or not from_currency or not to_currency:
        return jsonify({"error": "Missing parameters"}), 400
    
    key = f"{from_currency}_{to_currency}"
    rate = currency_rates.get(key)
    
    if rate:
        converted_amount = amount * rate
        return jsonify({"converted_amount": converted_amount})
    else:
        return jsonify({"error": "Conversion rate not found"}), 400


if __name__ == '__main__':
    app.run(debug=True)