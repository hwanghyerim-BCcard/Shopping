// rankingData and cardMetadata are declared via script tag in index.html

const malls = [
    "쿠팡", "지마켓", "지그재그", "이마트", "옥션", "NOL", "오늘의집", "알리", "예스24", 
    "Hmall", "트립닷컴", "호텔스닷컴", "LFmall", "아고다", "교보문고", "롯데온", 
    "11번가", "아이허브", "클리오", "맘큐", "롯데홈쇼핑", "CJ더마켓", "GS샵", 
    "W컨셉", "땡처리닷컴", "하이마트"
];

const tabsList = document.getElementById('tabsList');
const currentMallTitle = document.getElementById('currentMallTitle');
const cardsGrid = document.getElementById('cardsGrid');
const wrapper = document.querySelector('.tabs-wrapper');
const btnLeft = document.querySelector('.scroll-btn.left');
const btnRight = document.querySelector('.scroll-btn.right');

let activeMall = malls[0];

// Initialize Tabs
function initTabs() {
    malls.forEach(mall => {
        const li = document.createElement('li');
        const button = document.createElement('button');
        button.className = 'tab-btn';
        button.textContent = mall;
        if (mall === activeMall) {
            button.classList.add('active');
        }
        
        button.addEventListener('click', () => {
            if (activeMall === mall) return; // Ignore if already selected
            
            // Remove active classes
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            activeMall = mall;
            
            // Animate out previous cards
            const currentCards = cardsGrid.querySelectorAll('.ranking-card');
            if (currentCards.length > 0) {
                currentCards.forEach(card => card.style.opacity = '0');
                setTimeout(() => {
                    renderCards();
                }, 200);
            } else {
                renderCards();
            }
            
            // Center the clicked tab
            centerTab(button);
        });
        
        li.appendChild(button);
        tabsList.appendChild(li);
    });
    
    // Initial check for scroll buttons
    setTimeout(updateScrollButtons, 100);
}

// Center the clicked tab horizontally
function centerTab(buttonEl) {
    const parentWidth = tabsList.offsetWidth;
    const scrollPos = buttonEl.offsetLeft - (parentWidth / 2) + (buttonEl.offsetWidth / 2);
    tabsList.scroll({ left: scrollPos, behavior: 'smooth' });
}

// Render Cards for the selected mall
function renderCards() {
    currentMallTitle.textContent = `${activeMall} 추천 카드 랭킹`;
    cardsGrid.innerHTML = '';
    
    const cards = rankingData[activeMall] || [];
    
    if (cards.length === 0) {
        cardsGrid.innerHTML = '<div class="empty-state">해당 쇼핑몰에 대한 추천 데이터가 없습니다.</div>';
        return;
    }
    
    cards.forEach((card, index) => {
        const cardEl = document.createElement('div');
        cardEl.className = 'ranking-card';
        cardEl.setAttribute('data-rank', card.rank);
        cardEl.style.animationDelay = `${index * 0.08}s`;
        
        const meta = cardMetadata[card.cardName] || { gdsno: '', image: '' };
        const gdsnoText = meta.gdsno ? `<div class="card-gdsno">카드번호: ${meta.gdsno}</div>` : '';
        const imgHtml = meta.image ? `<img src="${meta.image}" class="card-image" alt="${card.cardName}">` : '<div class="card-image-placeholder"></div>';
        const fallbackBadge = card.isFallback ? `<span class="fallback-badge">차선책</span>` : '';
        
        cardEl.innerHTML = `
            ${imgHtml}
            <div class="card-content-wrapper">
                <div class="card-header">
                    <div class="card-name-wrapper">
                        <div class="card-name-row">
                            <div class="card-name">${card.cardName}</div>
                            ${fallbackBadge}
                        </div>
                        ${gdsnoText}
                    </div>
                    <div class="rank-badge">${card.rank}</div>
                </div>
                <div class="card-reason">${card.reason}</div>
            </div>
        `;
        
        cardsGrid.appendChild(cardEl);
    });

    // Excluded Cards Logic
    const excludedCardsGrid = document.getElementById('excludedCardsGrid');
    if (excludedCardsGrid) {
        excludedCardsGrid.innerHTML = '';
        const allCards = Object.keys(cardMetadata);
        const recommendedCardNames = cards.map(c => c.cardName);
        const excludedCards = allCards.filter(name => !recommendedCardNames.includes(name));
        
        if (excludedCards.length === 0) {
            excludedCardsGrid.innerHTML = '<div class="empty-state">추천 제외된 카드가 없습니다.</div>';
        } else {
            excludedCards.forEach(name => {
                const meta = cardMetadata[name];
                const el = document.createElement('div');
                el.className = 'excluded-card';
                
                const imgHtml = meta.image ? `<img src="${meta.image}" class="excluded-card-image" alt="${name}">` : '<div class="excluded-card-image-placeholder"></div>';
                const reason = "해당 쇼핑몰 제휴 혜택 없음 (상대적 혜택률 우위 밀림) 및 범용 추천 우선순위 제외";
                
                el.innerHTML = `
                    ${imgHtml}
                    <div class="excluded-card-info">
                        <div class="excluded-card-name">${name}</div>
                        <div class="excluded-card-gdsno">카드번호: ${meta?.gdsno || ''}</div>
                        <div class="excluded-card-reason">${reason}</div>
                    </div>
                `;
                excludedCardsGrid.appendChild(el);
            });
        }
    }
}

// Scroll handling for tabs
function updateScrollButtons() {
    if (tabsList.scrollWidth > tabsList.clientWidth) {
        btnLeft.style.display = 'block';
        btnRight.style.display = 'block';
    } else {
        btnLeft.style.display = 'none';
        btnRight.style.display = 'none';
    }
}

btnLeft.addEventListener('click', () => {
    tabsList.scrollBy({ left: -250, behavior: 'smooth' });
});

btnRight.addEventListener('click', () => {
    tabsList.scrollBy({ left: 250, behavior: 'smooth' });
});

window.addEventListener('resize', updateScrollButtons);

// Setup
initTabs();
renderCards();
