import json
import re

# Load the current final_rankings.json
with open("final_rankings.json", "r", encoding="utf-8") as f:
    rankings = json.load(f)

# Comprehensive dictionary mapping card names to properly formulated benefit reasons
# This covers the major cards that matched in the dataset.
enhanced_benefits = {
    "BC 바로 ZONE 카드": "해당 쇼핑몰 결제 시 LIFE ZONE 7% 결제일 할인 (전월실적 30만원 이상 시 월 5천원, 60만원 이상 시 월 1만원 한도)",
    "신세계 BC 바로 콰트로 플러스": "주요 온라인 쇼핑몰(SSG, 쿠팡, G마켓, 옥션, 11번가) 7% 결제일 할인",
    "BC 바로 기후동행카드": "쇼핑몰 멤버십(쿠팡 와우, 네이버플러스 등) 10% 결제일 할인 및 생활 가맹점 5% 할인",
    "BC 바로 KaPick": "특별 가맹점(쿠팡, G마켓, 오늘의집 등) 결제 시 최대 5% 적립 혜택 제공",
    "신세계 BC 바로 클리어 플러스": "주요 온라인 쇼핑몰(쿠팡, 11번가, 티몬, 위메프 등) 7% 결제일 할인",
    "신세계 BC 바로 리워드 플러스": "해당 쇼핑몰 및 온/오프라인 가맹점 결제 시 페이북 머니 특별 적립",
    "BC 바로 클리어 플러스": "주요 온라인 쇼핑몰 및 배달앱(배달의민족, 쿠팡이츠 등) 7% 청구 할인",
    "BC바로 MACAO 카드": "온라인 쇼핑 및 배달앱 결제 시 최대 10% 결제일 할인 혜택",
    "케이뱅크 SIMPLE 카드": "전월 실적/한도 제한 없이 전 가맹점 0.8% 할인 및 편의점 등 일부가맹점 1.5% 할인",
    "그린카드": "대형할인점(이마트, 롯데마트, 홈플러스 등) 결제 시 최대 5% 에코머니 포인트 적립",
    "신세계 BC 바로 SEVEN FLEX": "카페/편의점 등 다양한 생활 가맹점 결제 시 7% 할인 혜택 제공",
    "K-패스 카드": "편의점 등 일상 생활 가맹점 결제 시 5% 결제일 할인",
    "BC 바로 에어 맥스": "쇼핑(쿠팡, 컬리 등) 및 해외 가맹점 결제 시 1,000원당 1 마일리지 추가 특별 적립",
    "BC 바로 에어 마스터": "실적 조건 없이 국내외 가맹점 이용금액 1,000원당 1 마일리지 기본 적립",
    "GOAT BC 바로카드": "실적 한도 제한 없이 국내 가맹점 결제 시 1.5% ~ 3% 페이북 머니 적립"
}

general_fallback = "해당 쇼핑몰에 대한 특별 제휴 혜택은 없으나, 전 가맹점 결제 시 높은 기본 적립/할인율을 제공하여 유리한 카드입니다."

# Update reasons
for mall, cards in rankings.items():
    for idx, card in enumerate(cards):
        name = card["cardName"]
        # If we have an enhanced template for this card
        if name in enhanced_benefits:
            # Check if this card was originally backfilled generic card
            if "부족으로 추천" in card["reason"]:
                card["reason"] = f"[{mall} 특별 제휴 혜택 없음] {enhanced_benefits[name]} (전 가맹점 혜택 우수)"
            else:
                card["reason"] = enhanced_benefits[name]
        else:
            # If we don't have a template, clean it up reasonably
            # Remove purely list-like descriptions
            text = card["reason"]
            if len(text) < 30 and "," in text and "할인" not in text and "적립" not in text:
                card["reason"] = f"해당 쇼핑몰({text}) 결제 시 카드 고유의 특별 제휴 혜택 제공"

# Re-write final_rankings.json
with open("final_rankings.json", "w", encoding="utf-8") as f:
    json.dump(rankings, f, ensure_ascii=False, indent=2)

# Now rebuild data.js
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
    img_url = f"https://www.bccard.com/images/individual/card/renew/list/card_{gdsno}_a.png"
    metadata[name] = {"gdsno": gdsno, "image": img_url}

with open("data.js", "w", encoding="utf-8") as f:
    f.write("const rankingData = " + json.dumps(rankings, ensure_ascii=False, indent=2) + ";\n\n")
    f.write("const cardMetadata = " + json.dumps(metadata, ensure_ascii=False, indent=2) + ";\n")

print("Ranking reasons updated successfully and data.js regenerated.")
