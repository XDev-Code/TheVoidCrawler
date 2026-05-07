from urllib import response

import requests
from bs4 import BeautifulSoup

def GetAdminPage(domain):
    if not domain.startswith("http://") and not domain.startswith("https://"):
        domain = "https://" + domain

    response = requests.post("https://tools.prinsh.com/home/?tools=adfind",headers={"User-Agent": "Mozilla/5.0"},data={"url": domain,"submit": "Check Now!!!"})

    soup = BeautifulSoup(response.text, "html.parser")
    

    p_tags = soup.find_all("p")

    if len(p_tags) >= 2:    
        
        current = p_tags[1]

        while current:
            current = current.find_next()
        
            if current:
                texto = current.get_text(" ", strip=True)
                if texto:
                    if "exists." in texto:
                        texto = texto.replace("exists.", "").strip()
                        texto = texto.replace("Admin Page Found!", "").strip()
                        return texto
                    else:
                        return "Admin page not found."


if __name__ == "__main__":
    target = input("Enter the domain to find admin page: ")
    print(GetAdminPage(target))