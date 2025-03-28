from flask import Flask, request, render_template_string

app = Flask(__name__)

# Define a list of fortune messages
fortunes = [
    "You will have a great day!",
    "A pleasant surprise is waiting for you!",
    "Adventure awaits around the corner!",
    "Good things come to those who wait.",
    "Future is hazy."
]

@app.route('/')
def home():
    return """<html><head><title>Tell Your Fortune</title></head>
      <body><h1>Tell Your Fortune</h1>
      <form action="/fortune" method="POST">
        <label>Enter a name to get their fortune:</label>
        <input type="text" name="user_name" size="20" autofocus="autofocus" onfocus="this.select()"/>
        <br/><input type="submit" value="submit" />
      </form>
    </body></html>
    """

@app.route("/fortune", methods=["POST"])
def fortune():
    # Write the missing code:
    # Get the user_name from the `user_name` form field
    # Set `selected_fortune` to a fortune selected using the length
    # of the user_name modulo the 5 fortunes in the list.
    ...
    user_name = str(request.form['user_name'])
    selected_fortune = fortunes[len(user_name) % 5]



    # Display the fortune with the user's name
    return render_template_string(
        """<html><head><title>Tell Your Fortune</title></head>
      <body><h1>Tell Your Fortune</h1>
      <p>Hi, {{user_name}}, your fortune is:</p>
      <p>{{fortune}}</p>
      <form action="/fortune" method="POST">
        <label>Enter a new name to get their fortune:</label>
        <input type="text" name="user_name" size="20" autofocus="autofocus" onfocus="this.select()"/>
        <br/><input type="submit" value="submit" />
      </form>
    </body></html>
    """, user_name=user_name, fortune=selected_fortune)


# run the Flask app (which will launch a local webserver)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)