import json
import re

with open("card_benefits.json", "r", encoding="utf-8") as f:
    extracted_data = json.load(f)

generic_cards = [
    "BC 바로 ZONE 카드",
    "신세계 BC 바로 콰트로 플러스",
    "케이뱅크 SIMPLE 카드",
    "GOAT BC 바로카드",
    "BC 바로 에어 마스터"
]

malls = ["쿠팡", "지마켓", "지그재그", "이마트", "옥션", "NOL", "오늘의집", "알리", "예스24", "Hmall", "트립닷컴", "호텔스닷컴", "LFmall", "아고다", "교보문고", "롯데온", "11번가", "아이허브", "클리오", "맘큐", "롯데홈쇼핑", "CJ더마켓", "GS샵", "W컨셉", "땡처리닷컴", "하이마트"]

def get_accurate_reason(mall, card_name, is_specific):
    if not is_specific:
        if card_name == "BC 바로 ZONE 카드":
            return f"{mall} 전용 특별 제휴는 없으나, 주요 온라인몰(쿠팡, 다이소 등) 7% 결제일 할인이 강력해 차선책으로 추천합니다."
        if card_name == "신세계 BC 바로 콰트로 플러스":
            return f"{mall} 전용 혜택은 없으나, 기타 주요 온라인몰(쿠팡, 11번가 등) 7% 할인을 제공하는 필수 카드라 보조 결제용으로 추천합니다."
        if card_name == "케이뱅크 SIMPLE 카드":
            return f"전용 할인 카드가 없다면, 전월 실적 조건 제한 없이 어디서나 0.8% 기본 청구할인을 즉시 받을 수 있는 이 카드를 차선책으로 사용해 보세요."
        if card_name == "GOAT BC 바로카드":
            return f"비록 특별 제휴는 없으나, 실적이나 한도 없이 1.5% ~ 최대 3% 페이북 머니가 범용적으로 무조건 적립되어 유리합니다."
        if card_name == "BC 바로 에어 마스터":
            return f"{mall} 제휴는 아니지만, 전월 실적 조건 없이 1,000원당 1 마일리지가 기본 적립되어 범용 카드로 활용성이 높습니다."
        return f"해당 쇼핑몰({mall}) 특별 제휴는 없으나, 범용 혜택이 우수하여 차선책으로 추천합니다."
        
    if card_name == "신세계 BC 바로 리워드 플러스":
        if mall in ["교보문고", "예스24"]:
            return "생활 카테고리(서점 등) 결제 시 월 최대 3만 포인트까지 페이북 머니 4% 특별 적립"
        elif mall in ["이마트", "지마켓", "옥션"]:
            return "쇼핑 카테고리(대형마트, 온라인 카테고리 등) 결제 시 페이북 머니 5% 특별 적립"
        elif mall == "쿠팡":
            return "엔터테인먼트 카테고리(쿠팡 로켓와우 등) 자동이체 시 페이북 머니 30% 특별 적립"
            
    if card_name == "BC 바로 ZONE 카드":
        if mall in ["쿠팡", "지그재그", "오늘의집"]:
            return "LIFE ZONE 온라인몰(쿠팡, 지그재그, 오늘의집 등) 결제 시 7% 결제일 할인 (전월실적 30만원 이상 월 5천원, 60만원 이상 월 1만원 한도)"
            
    if card_name == "신세계 BC 바로 콰트로 플러스":
        if mall in ["쿠팡", "지마켓", "옥션", "11번가"]:
            return "주요 온라인몰(쿠팡, G마켓, 옥션, 11번가 등) 결제 시 7% 결제일 할인"
        elif mall == "이마트":
            return "쇼핑 영역(신세계백화점, 이마트 등) 오프라인 결제 시 5% 결제일 할인"
        
    if card_name == "BC 바로 기후동행카드":
        if mall == "쿠팡":
            return "온라인쇼핑 멤버십(쿠팡 와우 등) 정기납부 시 10% 결제일 할인"
        elif mall == "이마트" or mall == "이마트24":
            return "편의점(이마트24 등) 및 특정 생활 가맹점 5% 결제일 할인"
            
    if card_name == "BC 바로 KaPick":
        if mall in ["쿠팡", "지마켓", "오늘의집"]:
            return f"안주하지 않는 쇼핑 혜택! 특별가맹점({mall} 등) 결제 시 5% 픽업(Pick) 적립"
            
    if card_name == "BC 바로 클리어 플러스":
        if mall in ["쿠팡", "지마켓", "옥션", "11번가"]:
            return f"주요 온라인 쇼핑몰({mall} 등) 결제 시 7% 청구 할인"
            
    if card_name == "신세계 BC 바로 클리어 플러스":
        if mall in ["쿠팡", "11번가", "지마켓"]:
            return f"{mall}을 비롯한 주요 온라인 쇼핑몰 결제 시 7% 결제일 할인"
            
    if card_name == "그린카드":
        if mall in ["이마트", "롯데홈쇼핑", "롯데온"]:
            return f"대형마트({mall} 등) 결제 시 최대 5% 에코머니 포인트 특별 적립"

    if card_name == "BC바로 MACAO 카드":
        if mall in ["쿠팡", "이마트"]:
            return f"{mall} 결제 시 최대 10% 결제일 할인"
            
    if card_name == "K-패스 카드":
        if mall == "이마트" or mall == "이마트24":
            return "편의점(이마트24 등) 및 기타 일상 생활 가맹점 결제 시 5% 결제일 할인"
            
    if card_name == "BC 바로 에어 맥스":
        if mall in ["쿠팡", "이마트", "지마켓"]:
            return f"쇼핑({mall} 등) 및 마트 가맹점 결제 시 1,000원당 1 마일리지 추가 한도 적립 혜택"

    return f"해당 가맹점({mall})에 대한 특별 제휴 혜택 탑재"

ranking_data = {}

for mall in malls:
    specifics = extracted_data.get(mall, [])
    cards = []
    seen = set()
    
    for b in specifics:
        cname = b["card"]
        if cname not in seen:
            cards.append({
                "rank": len(cards) + 1,
                "cardName": cname,
                "reason": get_accurate_reason(mall, cname, True),
                "isFallback": False
            })
            seen.add(cname)
            if len(cards) >= 5:
                break
                
    if mall == "예스24" and "신세계 BC 바로 리워드 플러스" not in seen:
        cards.insert(0, {
            "rank": 1,
            "cardName": "신세계 BC 바로 리워드 플러스",
            "reason": get_accurate_reason("예스24", "신세계 BC 바로 리워드 플러스", True),
            "isFallback": False
        })
        seen.add("신세계 BC 바로 리워드 플러스")
        for i, c in enumerate(cards):
            c["rank"] = i + 1
        cards = cards[:5]

    for gc in generic_cards:
        if len(cards) >= 5:
            break
        if gc not in seen:
            cards.append({
                "rank": len(cards) + 1,
                "cardName": gc,
                "reason": get_accurate_reason(mall, gc, False),
                "isFallback": True
            })
            seen.add(gc)
            
    ranking_data[mall] = cards

with open("data.js", "r", encoding="utf-8") as f:
    data_js = f.read()

match = re.search(r'(const cardMetadata = \{.*?\n\};)', data_js, re.DOTALL)
metadata_str = match.group(1) if match else "const cardMetadata = {};\n"

with open("data.js", "w", encoding="utf-8") as f:
    f.write("const rankingData = " + json.dumps(ranking_data, ensure_ascii=False, indent=2) + ";\n\n")
    f.write(metadata_str)

with open("final_rankings.json", "w", encoding="utf-8") as f:
    json.dump(ranking_data, f, ensure_ascii=False, indent=2)
