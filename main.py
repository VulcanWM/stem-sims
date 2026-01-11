from flask import Flask, Response, jsonify, request
import matplotlib
matplotlib.use("Agg")  # non-gui backend
import matplotlib.pyplot as plt
from random_walk import random_walk
from page_rank import page_rank
from coin_toss import coin_toss
import numpy as np
import io

app = Flask(__name__)

@app.route("/")
def main():
    return "Hi"

@app.route("/visualisation/random-walk")
def random_walk_image():
    fig, ax = plt.subplots()
    colors = ['r', 'b', 'g', 'k', 'm']
    for color in colors:
        xpoints, ypoints = random_walk()
        ax.plot(np.array(xpoints), np.array(ypoints), 'o', color=color, markersize=1)
    ax.set_title("Random Walks")

    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=300)
    plt.close(fig)
    buf.seek(0)
    return Response(buf.getvalue(), mimetype="image/png")

@app.route("/visualisation/coin-toss")
def coin_toss_image():
    fig, ax = plt.subplots()

    count = coin_toss()
    x = np.array(["H", "T"])
    y = np.array([count['H'], count['T']])
    bars = ax.bar(x, y)

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, str(height),
                ha='center', va='bottom')

    ax.set_title("Coin Toss")

    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=300)
    plt.close(fig)
    buf.seek(0)
    return Response(buf.getvalue(), mimetype="image/png")

@app.route("/api/random-walk")
def random_walk_coords():
    n = int(request.args.get('n', 10000))
    if n > 10000:
        n = 10000
    l = int(request.args.get('l', 1))
    xpoints, ypoints = random_walk(n, l)
    coords = [{"x": float(x), "y": float(y)} for x, y in zip(xpoints, ypoints)]
    return jsonify({"coords": coords})

@app.route("/api/page-rank", methods=["post"])
def page_rank_route():
    data = request.get_json()

    outbound_links_raw = data["outbound_links"]
    outbound_links = {int(k): v for k, v in outbound_links_raw.items()}

    first_num = int(data["first_num"])
    last_num = int(data["last_num"])
    damping_factor = float(data.get("damping_factor", 0.85))
    n = int(data.get("n", 10000))
    if n > 10000:
        n = 10000

    result = page_rank(outbound_links, first_num, last_num, damping_factor, n)
    return jsonify({"count": result})

@app.route("/api/coin-toss")
def coin_toss_count():
    n = int(request.args.get('n', 10000))
    if n > 10000:
        n = 10000
    result = coin_toss(n)
    return jsonify({"count": result})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
