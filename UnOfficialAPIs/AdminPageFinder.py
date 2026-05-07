from urllib import response

import requests
from bs4 import BeautifulSoup

def GetAdminPage(domain):
    if not domain.startswith("http://") and not domain.startswith("https://"):
        domain = "https://" + domain

    response = requests.post("https://tools.prinsh.com/home/?tools=adfind",headers={"User-Agent": "Mozilla/5.0"},data={"url": domain,"submit": "Check Now!!!"})

    soup = BeautifulSoup(response.text, "html.parser")
    
    results = []
    
    for element in soup.find_all(['div', 'p', 'span']):
        text = element.get_text(" ", strip=True)
        if "https://" in text and ("exists" in text or "does not exist" in text):
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line.startswith('https://') and ('exists' in line or 'does not exist' in line):
                    results.append(line)
    
    if not results:
        full_text = soup.get_text()
        import re
        pattern = r'(https://[^\s]+/(?:admin|administrator|login|wp-admin|panel)[^\s]*)\s+(exists|does not exist)'
        matches = re.findall(pattern, full_text)
        for match in matches:
            results.append(f"{match[0]} {match[1]}")
    
    if results:
        unique_results = list(dict.fromkeys(results))
        existing_pages = []
        
        for result in unique_results:
            if "exists" in result and "does not exist" not in result:
                url = result.split(" exists")[0].strip()
                existing_pages.append(url)
        
        if existing_pages:
            return "\n".join(existing_pages)
        else:
            return "No admin pages found."
    else:
        return "No admin pages found."


if __name__ == "__main__":
    target = input("Enter the domain to find admin page: ")
    print(GetAdminPage(target))