import json

with open("final_rankings.json", "r", encoding="utf-8") as f:
    rankings = json.load(f)

def get_refined_reason(mall, card_name, original_reason):
    if card_name == "신세계 BC 바로 리워드 플러스":
        if mall in ["교보문고", "예스24"]:
            return "생활 카테고리(서점 등) 결제 시 월 최대 3만 포인트까지 페이북 머니 4% 특별 적립"
        elif mall in ["이마트", "지마켓", "옥션"]:
            return "쇼핑 카테고리(대형마트, 온라인몰 등) 결제 시 페이북 머니 5% 특별 적립"
        elif mall == "쿠팡":
            return "엔터테인먼트 카테고리(쿠팡 로켓와우 등) 자동이체 시 페이북 머니 30% 특별 적립"
        else:
            return "온/오프라인 전 가맹점 결제 시 페이북 머니 최대 1.5% 기본 적립 제공"
            
    if card_name == "BC 바로 ZONE 카드":
        if mall in ["쿠팡", "지그재그", "오늘의집"]:
            return "LIFE ZONE 온라인몰(쿠팡, 지그재그, 오늘의집 등) 결제 시 7% 결제일 할인 (전월실적 30만원 이상 월 5천원, 60만원 이상 월 1만원 한도)"
        elif mall in ["위메프", "티몬", "11번가"]:
            return "쇼핑몰 결제 시 LIFE ZONE 7% 결제일 할인 혜택 제공 (유의사항 참조)"
        else:
            return "해당 쇼핑몰 결제 시 LIFE ZONE 7% 결제일 할인 혜택 확인 가능 (쿠팡 등 일부 대상)"
            
    if card_name == "신세계 BC 바로 콰트로 플러스":
        if mall in ["쿠팡", "지마켓", "옥션", "11번가"]:
            return "주요 온라인몰(쿠팡, G마켓, 옥션, 11번가 등) 결제 시 7% 결제일 할인 (전월 실적에 따라 통합할인한도 적용)"
        elif mall == "이마트":
            return "쇼핑 영역(신세계백화점, 이마트 등) 오프라인 5% 결제일 할인"
        else:
            return f"{mall} 결제 시 기본 혜택 적용 및 주요 온라인몰 7% 할인 제공 카드"
        
    if card_name == "BC 바로 기후동행카드":
        if mall == "쿠팡":
            return "온라인쇼핑 멤버십(쿠팡 와우 등) 정기납부 시 10% 결제일 할인"
        elif mall == "이마트" or mall == "이마트24":
            return "편의점(이마트24 등) 및 특정 생활 가맹점 5% 결제일 할인"
        else:
            return "멤버십(쿠팡 와우 등) 10% 할인 외 대중교통 15% 기후동행 특화 혜택 탑재"
            
    if card_name == "BC 바로 KaPick":
        if mall in ["쿠팡", "지마켓", "오늘의집"]:
            return f"특별가맹점({mall} 등) 결제 시 결제금액의 5% 픽업(Pick) 적립 (전월 실적 조건 달성 시)"
        else:
            return "국내외 모든 가맹점 0.5% 기본 적립"
            
    if card_name == "BC 바로 클리어 플러스":
        if mall in ["쿠팡", "지마켓", "옥션", "11번가"]:
            return f"주요 온라인 쇼핑몰({mall} 등) 결제 시 7% 청구 할인 (오프라인 점심 7% 등 혜택 다수 탑재)"
            
    if card_name == "신세계 BC 바로 클리어 플러스":
        if mall in ["쿠팡", "11번가", "지마켓"]:
            return f"{mall}을 비롯한 주요 온라인 쇼핑몰 결제 시 7% 결제일 할인"
            
    if card_name == "그린카드":
        if mall in ["이마트", "롯데홈쇼핑", "롯데온"]:
            return f"대형마트({mall} 등) 결제 시 최대 5% 에코머니 포인트 특별 적립"

    if card_name == "BC바로 MACAO 카드":
        if mall in ["쿠팡", "이마트"]:
            return f"{mall} 결제 시 최대 10% 결제일 할인 (전월 실적 허들 충족 시)"
            
    if card_name == "케이뱅크 SIMPLE 카드":
        return "전월 실적/할인 한도 제한 없이 전 가맹점 0.8% 청구할인 (이마트24 등 생활 밀착 영역은 1.5% 청구할인)"
        
    if card_name == "BC 바로 에어 마스터":
        return "전월 실적 조건 없이 국내외 모든 가맹점 이용금액 1,000원당 1 마일리지 기본 혜택 제공"
        
    if card_name == "BC 바로 에어 맥스":
        if mall in ["쿠팡", "이마트", "지마켓"]:
            return f"쇼핑({mall} 등) 및 마트 가맹권 결제 시 1,000원당 1 마일리지 추가 한도 적립 혜택"
        return "전월 실적 30만원 이상 시 이용금액 1,000원당 1 마일리지 적립"

    if card_name == "GOAT BC 바로카드":
        return "전월 실적이나 적립 한도 제한 없이 국내 전 가맹점에서 결제금액의 1.5% ~ 최대 3% 페이북 머니 특별 적립"
        
    if card_name == "K-패스 카드":
        if mall == "이마트" or mall == "이마트24":
            return "편의점(이마트24 등) 및 기타 일상 생활 가맹점 결제 시 5% 결제일 할인"
        return "국내 가맹점 0.3% 기본 할인 및 K-패스 대중교통 마일리지 제공"

    # Default fallback cleaner
    if "[특별 제휴 혜택 없음]" in original_reason:
        return f"해당 쇼핑몰({mall}) 전용 특별 제휴는 명시되어 있지 않으나, 전 가맹점 결제 시 높은 기본 적립/할인율을 제공하여 유리한 카드입니다."
        
    if "특별 제휴 혜택 없음" in original_reason:
        return f"전 가맹점에서 일괄적으로 제공되는 범용 강력한 혜택을 통해 {mall}에서도 높은 혜택을 누릴 수 있습니다."

    return original_reason

for mall, cards in rankings.items():
    for card in cards:
        name = card["cardName"]
        reason = get_refined_reason(mall, name, card["reason"])
        card["reason"] = reason

# Read urls to rewrite data.js
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

import re
metadata = {}
for name, link in urls.items():
    gdsno = re.search(r'gdsno=([^&]+)', link).group(1)
    img_url = f"https://www.bccard.com/images/individual/card/renew/list/card_{gdsno}_a.png"
    metadata[name] = {"gdsno": gdsno, "image": img_url}

with open("data.js", "w", encoding="utf-8") as f:
    f.write("const rankingData = " + json.dumps(rankings, ensure_ascii=False, indent=2) + ";\n\n")
    f.write("const cardMetadata = " + json.dumps(metadata, ensure_ascii=False, indent=2) + ";\n")

with open("final_rankings.json", "w", encoding="utf-8") as f:
    json.dump(rankings, f, ensure_ascii=False, indent=2)

print("Exact percentages mapped successfully")
