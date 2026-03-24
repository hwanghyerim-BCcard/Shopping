import urllib.request
from bs4 import BeautifulSoup
import json
import re

urls = {
    "BC 바로 ZONE 카드": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=104520&mbkNo=050",
    "BC 바로 에어 마스터": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=104452&mbkNo=050",
    "BC 바로 에어 맥스": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=104453&mbkNo=050",
    "KT SUPER DC BC 바로카드": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=104063&mbkNo=050",
    "BC 바로 기후동행카드": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=103992&mbkNo=050",
    "BC바로 MACAO 카드": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=101010&mbkNo=050",
    "BC 바로 KaPick": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=103862&mbkNo=050",
    "KT 마이알뜰폰 BC 바로카드": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=103127&mbkNo=050",
    "GOAT BC 바로카드": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=100008&mbkNo=050",
    "kt DC PLUS": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=103125&mbkNo=050",
    "BC 바로 On&Off 카드": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=102040&mbkNo=050",
    "K-패스 카드": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=103112&mbkNo=050",
    "신세계 푸빌라 BC 바로카드": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=102603&mbkNo=050",
    "신세계 BC 바로 콰트로 플러스": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=101874&mbkNo=050",
    "신세계 BC 바로 SEVEN FLEX": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=101883&mbkNo=050",
    "신세계 BC 바로 클리어 플러스": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=101881&mbkNo=050",
    "신세계 BC 바로 리워드 플러스": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=101877&mbkNo=050",
    "BC 바로 클리어 플러스": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=101922&mbkNo=050",
    "로스트아크 카드": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=101686&mbkNo=050",
    "케이뱅크 SIMPLE 카드": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=100972&mbkNo=050",
    "그린카드": "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=100980&mbkNo=050"
}

metadata = {}
for name, link in urls.items():
    gdsno = re.search(r'gdsno=([^&]+)', link).group(1)
    
    img_url = ""
    try:
        req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        
        for img in soup.find_all('img'):
            src = img.get('src')
            if src and 'image.bccard.com' in src and 'card' in src:
                img_url = src
                break
                
        if not img_url:
            card_img_div = soup.find('div', class_='card_img')
            if card_img_div and card_img_div.find('img'):
                img_url = card_img_div.find('img').get('src')
                
    except Exception as e:
        pass
        
    metadata[name] = {
        "gdsno": gdsno,
        "image": img_url
    }

with open("data.js", "a", encoding="utf-8") as f:
    f.write("\nexport const cardMetadata = " + json.dumps(metadata, ensure_ascii=False, indent=2) + ";\n")
print("done")
