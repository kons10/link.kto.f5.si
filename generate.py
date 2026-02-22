import csv
import os

# HTMLのテンプレート
INDEX_TEMPLATE = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>短縮リンク一覧</title>
    <style>
        body {{ font-family: sans-serif; margin: 20px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
        th {{ background-color: #f4f4f4; }}
    </style>
</head>
<body>
    <h1>短縮リンク一覧</h1>
    <table>
        <tr><th>短縮名</th><th>リンク先URL</th></tr>
        {rows}
    </table>
</body>
</html>
"""

def generate():
    rows_html = ""
    
    # links.csv を読み込む
    with open('links.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row: continue
            short_name, target_url = row[0], row[1]
            
            # 各リンク用のディレクトリ作成などの既存処理がここにある想定
            # ...
            
            # 一覧ページ用の行を作成
            rows_html += f'<tr><td><a href="./{short_name}/">{short_name}</a></td><td>{target_url}</td></tr>'

    # index.html を書き出す
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(INDEX_TEMPLATE.format(rows=rows_html))

if __name__ == "__main__":
    generate()
