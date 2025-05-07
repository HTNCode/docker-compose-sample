from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="/app/frontend/build")


@app.route("/")
def main():
    return send_from_directory(app.static_folder, "index.html")


# 静的ファイルへのルートを追加
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(app.static_folder, path)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
