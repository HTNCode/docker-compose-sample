# フロントエンドビルドステージ
FROM node:24-bookworm-slim AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# バックエンドステージ
FROM python:3.13-slim-bookworm
WORKDIR /app

# Poetryのインストール
RUN pip install --no-cache-dir poetry

# バックエンドのソースコードをコピー(.dockerignoreでbackend/.envを含めないようにすることを忘れずに！)
COPY backend/ .

# 依存関係のインストール (仮想環境内)
RUN poetry lock
RUN poetry install --no-root --without dev

# HuggingFaceからモデルをダウンロードするスクリプトを実行
RUN --mount=type=secret,id=hf_token \
    export HF_TOKEN=$(cat /run/secrets/hf_token) && \
    poetry run python ./models/create_llm.py

# フロントエンドのビルド済みファイルをコピー
COPY --from=frontend-builder /app/frontend/build ./frontend/build

EXPOSE 5000

# 仮想環境をアクティベートしてアプリケーションを実行
CMD ["poetry", "run", "python", "main.py"]