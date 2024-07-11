#!/bin/bash

# pip のインストールを確認する
if ! command -v pip &> /dev/null
then
    echo "pip が見つかりません、インストールします..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3.9 get-pip.py
    rm get-pip.py
fi

# 依存パッケージのインストール
python3.9 -m pip install -r requirements.txt
python3.9 -m pip install -y libmariadbclient-dev

# マイグレーションの適用
python3.9 manage.py migrate --noinput

# 静的ファイルの収集
python3.9 manage.py collectstatic --noinput
