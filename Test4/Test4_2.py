from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return """<html><head><title>Interest Calculator</title></head>
    <body><h1>Interest Calculator</h1>
      <form action="/compute_interest" method="POST">
        <label>Enter the amount:</label><input type="text" value="" name="amount" /><br/>
        <label>Enter the interest rate (0.05 for 5 percent):</label><input type="text" value="" name="interest_rate" /><br/>
        <br/><input type="submit" value="Compute Interest" />
      </form>
    </body></html>
    """

@app.route('/compute_interest', methods=['POST'])
def compute_interest():
    # Get the "amount" and "interest_rate" input values from the form and convert to float
    amount = float(request.form['amount'])
    interest_rate = float(request.form['interest_rate'])

    # Compute "computed_interest" from the amount & interest_rate, and the "new_balance"
    computed_interest = amount * interest_rate
    new_balance = amount + computed_interest

    return """<html><head><title>Computed Interest</title></head>
        <body><h1>Computed Interest</h1>
        <table>
        <tr><th>Value</th><th>Amount</th></tr>
        <tr><td>Initial Balance</td><td align="right">{amount:.2f}</td></tr>
        <tr><td>Interest Rate</td><td align="right">{interest_rate:.2f}</td></tr>
        <tr><td>Computed Interest</td><td align="right">{computed_interest:.2f}</td></tr>
        <tr><td>New Balance</td><td align="right">{new_balance:.2f}</td></tr>
        </table></body></html>""".format(amount=amount, interest_rate=interest_rate,
                                        computed_interest=computed_interest, new_balance=new_balance)

# Run the Flask app (which will launch a local webserver)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
