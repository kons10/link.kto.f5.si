import csv
import os

# 設定
CSV_FILE = 'links.csv'
INDEX_FILE = 'index.html'

def generate():
    links = []
    
    # CSVファイルを読み込む
    with open(CSV_FILE, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            links.append(row)

    # 各短縮リンクのディレクトリと転送用index.htmlを作成
    for link in links:
        path = link['path'].lstrip('/')
        url = link['url']
        
        os.makedirs(path, exist_ok=True)
        
        with open(os.path.join(path, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(f'<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url={url}"><script>window.location.href="{url}"</script><title>Redirecting...</title></head><body>Redirecting to <a href="{url}">{url}</a></body></html>')

    # --- ここから index.html (一覧ページ) 生成機能 ---
    
    html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Link List</title>
    <style>
        body { font-family: sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: 0 auto; }
        h1 { border-bottom: 2px solid #eee; }
        ul { list-edge: none; padding: 0; }
        li { margin-bottom: 10px; border: 1px solid #ddd; padding: 10px; border-radius: 5px; }
        a { color: #007bff; text-decoration: none; font-weight: bold; }
        a:hover { text-decoration: underline; }
        .path { color: #666; font-size: 0.9em; }
    </style>
</head>
<body>
    <h1>短縮リンク一覧</h1>
    <ul>
"""

    for link in links:
        path = link['path']
        url = link['url']
        # 一覧に表示するリンクのリストを追加
        html_content += f'        <li><a href="{path}">{path}</a> <span class="path">→ {url}</span></li>\n'

    html_content += """    </ul>
</body>
</html>"""

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Generated {len(links)} links and {INDEX_FILE}")

if __name__ == '__main__':
    generate()
