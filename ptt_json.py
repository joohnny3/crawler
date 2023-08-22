import json
import requests
from bs4 import BeautifulSoup

root_url = 'https://disp.cc/b/'

r = requests.get('https://disp.cc/b/PttHot')
soup = BeautifulSoup(r.text, 'html.parser')

# 建立一個空的列表來存放資料
data_list = []

for span in soup.select('#list span.listTitle'):
    href = span.find('a').get('href')
    if href == '796-59l9':
        break

    url = root_url + href
    title = span.text
    # 將資料加入到列表中
    data_list.append({
        'title': title,
        'url': url
    })

# 轉換列表為JSON格式
json_data = json.dumps(data_list, ensure_ascii=False)

# 如需將JSON資料存儲到檔案中，可以使用以下的程式碼：
with open('data.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

# 如此一來，您就可以在JavaScript中讀取data.json檔案，然後使用這些資料了。
