import csv

# CSVファイルを読み込む（例）
csv_data = []
with open('links.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        csv_data.append(row)

# HTMLのテーブル部分を生成
table_rows = ""
for item in csv_data:
    table_rows += f"""
        <tr>
            <td>{item['title']}</td>
            <td><code>/{item['path']}</code></td>
            <td><a href="{item['url']}" target="_blank">{item['url']}</a></td>
        </tr>"""

# index.html の中身
html_content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>リンク一覧 | {{{{ site_name }}}}</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/material-symbols@latest/outlined.css">
  <link rel="stylesheet" href="/assets/css/base.css">
  <style>
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
      background-color: var(--md-sys-color-surface-container-low);
      border-radius: 12px;
      overflow: hidden;
    }}
    th, td {{
      padding: 12px;
      text-align: left;
      border-bottom: 1px solid var(--divider-color);
    }}
    th {{
      background-color: var(--md-sys-color-primary-container);
      color: var(--md-sys-color-on-primary-container);
    }}
    code {{
      background: var(--md-sys-color-surface-variant);
      padding: 2px 6px;
      border-radius: 4px;
    }}
  </style>
</head>
<body>
  <main>
    <h1><span class="material-symbols-outlined">link</span> リンク一覧</h1>
    <p>現在有効な短縮リンク（リダイレクト）のリストだｿﾞ~</p>
    
    <table>
      <thead>
        <tr>
          <th>名前</th>
          <th>パス</th>
          <th>転送先URL</th>
        </tr>
      </thead>
      <tbody>
        {table_rows}
      </tbody>
    </table>
  </main>
</body>
</html>
"""

# ファイルに書き出し
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
