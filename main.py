from flask import Flask, Response, jsonify
import matplotlib
matplotlib.use("Agg")  # non-gui backend
import matplotlib.pyplot as plt
from random_walk import random_walk
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

if __name__ == "__main__":
    app.run(debug=True)
