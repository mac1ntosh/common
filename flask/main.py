from flask import Flask

app = Flask(__name__)

@app_route("/get_apple")
def get_apple():
    return "Apple"

if __name__== "__main___":
    app.run(debug=True)