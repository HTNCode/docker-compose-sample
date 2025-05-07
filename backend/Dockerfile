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

# 依存関係のインストール (仮想環境内)
COPY backend/pyproject.toml ./
RUN poetry lock
RUN poetry install --no-root --without dev

# バックエンドのソースコードをコピー
COPY backend/ .

# フロントエンドのビルド済みファイルをコピー
COPY --from=frontend-builder /app/frontend/build ./frontend/build

EXPOSE 5000

# 仮想環境をアクティベートしてアプリケーションを実行
CMD ["poetry", "run", "python", "main.py"]