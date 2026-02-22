import csv
import os

# CSV読み込み
with open('links.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        path = row['path']
        url = row['url']

        # フォルダ作成（例: insta/）
        os.makedirs(path, exist_ok=True)

        # リダイレクト用HTML作成
        with open(f"{path}/index.html", "w", encoding='utf-8') as html:
            html.write(f'<html><head><meta http-equiv="refresh" content="0;url={url}"></head></html>')
