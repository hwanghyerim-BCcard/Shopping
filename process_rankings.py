import json

with open("card_benefits.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# To backfill, we identify cards that are good for "online shopping" or "all merchants"
generic_cards = [
    {"card": "BC 바로 ZONE 카드", "benefit": "온라인 쇼핑몰 최대 10% 할인 (LIFE-ZONE 전월 실적 조건 충족 시)"},
    {"card": "신세계 BC 바로 콰트로 플러스", "benefit": "국내외 모든 가맹점 기본 할인 및 주요 온라인몰 7% 할인"},
    {"card": "케이뱅크 SIMPLE 카드", "benefit": "전월 실적/할인 한도 제한 없이 국내외 가맹점 0.8% ~ 1.5% 청구할인"},
    {"card": "GOAT BC 바로카드", "benefit": "국내 가맹점 결제 시 1.5% ~ 3% 페이북 머니 적립 (한도 없음)"},
    {"card": "BC 바로 에어 마스터", "benefit": "국내/해외 가맹점 이용금액 1,000원당 1 마일리지 적립 (전월 실적 조건 없음)"}
]

ranking_data = {}

for mall, specific_benefits in data.items():
    cards = []
    seen = set()
    
    # 1. Add specific benefits first
    for b in specific_benefits:
        if b["card"] not in seen:
            cards.append({
                "rank": len(cards) + 1,
                "cardName": b["card"],
                "reason": b["benefit"]
            })
            seen.add(b["card"])
            if len(cards) >= 5:
                break
    
    # 2. Backfill with generic cards
    for gb in generic_cards:
        if len(cards) >= 5:
            break
        if gb["card"] not in seen:
            reason = gb["benefit"]
            if len(cards) == 0:
                reason = f"[{mall} 특별 제휴 혜택 없음] " + reason
            cards.append({
                "rank": len(cards) + 1,
                "cardName": gb["card"],
                "reason": reason
            })
            seen.add(gb["card"])
            
    ranking_data[mall] = cards

# Special patches for aliases missed
def patch_rankings(target_mall, patched_card, patched_reason):
    if target_mall in ranking_data:
        m_cards = ranking_data[target_mall]
        if patched_card not in [c["cardName"] for c in m_cards]:
            m_cards.insert(0, {"rank": 1, "cardName": patched_card, "reason": patched_reason})
            for i, c in enumerate(m_cards):
                c["rank"] = i + 1
            ranking_data[target_mall] = m_cards[:5]

patch_rankings("예스24", "신세계 BC 바로 리워드 플러스", "서점(교보문고, 영풍문고, YES24) 결제 시 특별 혜택 제공")

with open("final_rankings.json", "w", encoding="utf-8") as f:
    json.dump(ranking_data, f, ensure_ascii=False, indent=2)

print("final_rankings.json created")
