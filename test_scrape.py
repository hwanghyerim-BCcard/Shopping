import urllib.request
from bs4 import BeautifulSoup

url = "https://www.bccard.com/app/card/CreditCardMain.do?gdsno=104520&mbkNo=050"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Let's find common benefit classes or just print stripped text
    body_text = soup.body.get_text(separator='\n', strip=True)
    
    print("--- HEAD START ---")
    print(body_text[:1500])
    print("--- HEAD END ---")
    
    # Try looking for specific keywords like 쿠팡, 쇼핑
    import re
    lines = body_text.split('\n')
    for i, line in enumerate(lines):
        if re.search(r'(쿠팡|쇼핑|할인|적립)', line):
            print(f"Match [{i}]: {line}")
            
except Exception as e:
    print("Error:", e)
