from flask import Flask, Response, jsonify, request
import matplotlib
matplotlib.use("Agg")  # non-gui backend
import matplotlib.pyplot as plt
from random_walk import random_walk
from page_rank import page_rank
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
        ax.plot(xpoints, ypoints, 'o', color=color, markersize=1)
    ax.set_title("Random Walks")

    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=300)
    plt.close(fig)
    buf.seek(0)
    return Response(buf.getvalue(), mimetype="image/png")

@app.route("/api/random-walk")
def random_walk_coords():
    xpoints, ypoints = random_walk()
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

if __name__ == "__main__":
    app.run(debug=True)
