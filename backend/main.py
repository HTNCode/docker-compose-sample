import signal
import sys
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="/app/frontend/build")

@app.route("/")
def main():
    return send_from_directory(app.static_folder, "index.html")

# 静的ファイルへのルートを追加
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# Graceful shutdown handler
def handle_shutdown(signum, frame):
    print(f"Received shutdown signal: {signum}")
    # 必要に応じてリソース解放処理を追加（例: DB接続のクローズなど）
    print("Cleaning up resources...")
    sys.exit(0)

# シグナルハンドラー登録
signal.signal(signal.SIGINT, handle_shutdown)  # Ctrl+C
signal.signal(signal.SIGTERM, handle_shutdown)  # Dockerや他のプロセス管理ツールからの終了信号

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
