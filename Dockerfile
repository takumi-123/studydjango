FROM python:3.11-slim

WORKDIR /app

# 必要なmysqlの必要なパッケージ
# 上からlinuxで起動できるインストール, mysqlに必要な道具, インストール終わったら不要ファイル削除
RUN apt-get update && apt-get install -y \ 
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 必要なpythonライブラリーダウンロード
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# appにこぴー
COPY . .