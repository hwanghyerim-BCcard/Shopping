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

malls = ["쿠팡", "지마켓", "지그재그", "이마트", "옥션", "NOL", "오늘의집", "알리", "예스24", "Hmall", "트립닷컴", "호텔스닷컴", "LFmall", "아고다", "교보문고", "롯데온", "11번가", "아이허브", "클리오", "맘큐", "롯데홈쇼핑", "CJ더마켓", "GS샵", "W컨셉", "땡처리닷컴", "하이마트"]

mall_aliases = {
    "지마켓": ["지마켓", "G마켓", "g마켓"],
    "옥션": ["옥션", "Auction"],
    "알리": ["알리", "AliExpress", "알리익스프레스"],
    "이마트": ["이마트", "emart", "이마트몰"],
    "11번가": ["11번가", "11st"],
    "NOL": ["NOL", "놀"],
    "Hmall": ["Hmall", "현대Hmall", "에이치몰"],
    "LFmall": ["LFmall", "엘에프몰"],
    "CJ더마켓": ["CJ더마켓", "씨제이더마켓"],
    "GS샵": ["GS샵", "GS SHOP", "지에스샵"],
    "W컨셉": ["W컨셉", "더블유컨셉"]
}

results = {mall: [] for mall in malls}

# General shopping/online terms
general_terms = ["온라인쇼핑", "인터넷쇼핑", "소셜커머스", "오픈마켓", "쇼핑할인", "쇼핑몰", "가맹점", "전가맹점"]

for card_name, url in urls.items():
    print(f"Scraping: {card_name}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        
        # We need to find elements that might contain benefit texts
        # <dl>, <dd>, <li>, <td>, <p>, <span>
        elements = soup.find_all(['li', 'p', 'dd', 'td', 'div'])
        
        seen_texts = set()
        
        for el in elements:
            text = el.get_text(separator=' ', strip=True)
            if not text or text in seen_texts or len(text) > 300 or len(text) < 2:
                continue
            
            seen_texts.add(text)
            
            for mall in malls:
                aliases = mall_aliases.get(mall, [mall])
                matched = False
                for alias in aliases:
                    if alias in text or alias.lower() in text.lower():
                        matched = True
                        break
                
                if matched:
                    # Also collect the parent's generic context if it might be a sub-bullet.
                    # But text itself is enough since we have separator=' '
                    results[mall].append({
                        "card": card_name,
                        "benefit": text
                    })
                    
    except Exception as e:
        print(f"Error scraping {card_name}: {e}")

# Deduplicate identical card/benefit matches for the same mall
for mall in malls:
    unique_benefits = []
    seen = set()
    for item in results[mall]:
        key = (item['card'], item['benefit'])
        if key not in seen:
            seen.add(key)
            unique_benefits.append(item)
    results[mall] = unique_benefits

with open('card_benefits.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Scraping completed. Results saved to card_benefits.json")
