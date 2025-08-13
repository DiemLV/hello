from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/")
def slow():
    # Lấy tham số 'delay' từ query parameter, mặc định là 0
    delay = request.args.get('delay', default=0, type=int)
    
    if delay > 0:
        time.sleep(delay)
        return f"Done after {delay} seconds\n=====================\n\n\n"
    else:
        return "Done immediately (no delay)\n=====================\n\n\n"

@app.route("/<int:delay>")
def slow_with_path(delay):
    # Route với delay truyền qua URL path
    if delay > 0:
        time.sleep(delay)
        return f"Done after {delay} seconds\n=====================\n\n\n"
    else:
        return "Done immediately (no delay)\n=====================\n\n\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
