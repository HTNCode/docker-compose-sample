"""Dockerfileでコンテナビルド時に個別に実行しローカルにLLMを保存するためのスクリプト"""

import os
import getpass

from transformers import AutoModelForCausalLM, AutoModel


# キャッシュの場所を指定したいとき
os.environ["HF_HOME"] = "./cache"

# Huggingfaceのトークン認証が必要なとき
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN", "")


def download_model(model_name, save_path="/app/models"):
    """LLMをローカルに保存する

    Args:
        model_name (_type_): _description_
        save_path (str, optional): _description_. Defaults to "/app/models".
    """
    # トークナイザーとモデルを取得
    tokenizer = AutoModelForCausalLM.from_pretrained(model_name)
    model = AutoModel.from_pretrained(
        model_name,
        # device_map="cuda",  # GPU。これを使う場合はaccelerateもaddする必要あり
        device_map="auto",
    )

    # モデルをローカルに保存
    save_dir = f"{save_path}/{model_name}"
    tokenizer.save_pretrained(save_dir)
    model.save_pretrained(save_dir)
    print(f"モデルを {save_dir} に保存したよ！")


if __name__ == "__main__":
    # ここにダウンロードしたいモデル名を指定
    model_name = "kotoba-tech/kotoba-whisper-v2.2"  # 例：kotoba-whisper-v2.2
    download_model(model_name)
