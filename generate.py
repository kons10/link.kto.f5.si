import csv
import os

# Configuration
CSV_FILE = 'links.csv'
INDEX_FILE = 'index.html'

def generate():
    links = []
    
    # Read links from CSV file
    # Ensure links.csv exists in the same directory
    try:
        with open(CSV_FILE, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                links.append(row)
    except FileNotFoundError:
        print(f"Error: {CSV_FILE} not found.")
        return

    # Generate individual redirect directories and their index.html
    for link in links:
        path = link['path'].lstrip('/')
        url = link['url']
        
        # Create directory for the shortcut
        os.makedirs(path, exist_ok=True)
        
        # Create redirect page
        with open(os.path.join(path, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(f'<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url={url}"><script>window.location.href="{url}"</script><title>Redirecting...</title></head><body>Redirecting to <a href="{url}">{url}</a></body></html>')

    # --- Generate index.html with a Table View ---
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Link List</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; padding: 40px; max-width: 1000px; margin: 0 auto; background-color: #f8f9fa; color: #333; }}
        h1 {{ text-align: center; color: #2c3e50; margin-bottom: 30px; }}
        table {{ width: 100%; border-collapse: collapse; background: #fff; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; }}
        th, td {{ padding: 15px; text-align: left; border-bottom: 1px solid #eee; }}
        th {{ background-color: #007bff; color: white; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }}
        tr:hover {{ background-color: #f1f4f9; }}
        a {{ color: #007bff; text-decoration: none; font-weight: bold; }}
        a:hover {{ text-decoration: underline; }}
        .path-cell {{ font-family: monospace; color: #e83e8c; }}
    </style>
</head>
<body>
    <h1>Link Directory</h1>
    <table>
        <thead>
            <tr>
                <th>Short Link</th>
                <th>Destination URL</th>
            </tr>
        </thead>
        <tbody>
"""

    for link in links:
        path = link['path']
        url = link['url']
        # Adding table rows for each link
        html_content += f"""            <tr>
                <td class="path-cell"><a href="{path}">{path}</a></td>
                <td><a href="{url}" target="_blank">{url}</a></td>
            </tr>\n"""

    html_content += """        </tbody>
    </table>
    <p style="margin-top: 20px; text-align: center; color: #666; font-size: 0.9em;">Generated automatically from links.csv</p>
</body>
</html>"""

    # Save the main index page
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Success: Processed {len(links)} links and updated {INDEX_FILE}")

if __name__ == '__main__':
    generate()
