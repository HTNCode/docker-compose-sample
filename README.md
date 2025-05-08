# docker compose の練習

- backend: Flask
- frontend: react
- 上記のフロント側のビルド済みの静的ファイルを backend 側で読み込んでまるごと一つのコンテナとしてビルドする
- docker compose up する時に set DOCKER_BUILDKIT=1 && docker compose build --no-cache && docker compose up で BUILDKIT を使って secret 機能を利用することで、ビルド時にだけ.env ファイルを使わせることが可能。
