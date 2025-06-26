from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
import urllib.parse
from urllib.parse import urlparse, urlencode, quote

app = Flask(__name__)
CORS(app)

@app.route("/get_ids")
def get_ids():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Referer": "https://bgm.tv/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
    }

    all_ids = []
    keyword = "百合" # 这里可以替换为其他tag
    encode = urllib.parse.quote(keyword)
    for page in range(1, 8): # 搜索前7页
        url = f"https://bgm.tv/book/tag/{encode}/?sort=collects&page={page}"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"页面 {page} 请求失败: {e}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        section_divs = soup.find_all("div", class_="section")

        for div in section_divs:
            lis = div.find_all("li")
            for li in lis:
                if 'id' in li.attrs:
                    all_ids.append(li['id'][5:])  # 去掉 'li_' 前缀

    return jsonify(all_ids)

if __name__ == "__main__":
    app.run(debug=True)
