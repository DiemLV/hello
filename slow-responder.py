from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def slow():
    time.sleep(20)
    return "Done after 20 seconds\n=====================\n\n\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
