import requests
import subprocess
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from UnOfficialAPIs.SubDomainFinder import find_subdomains



def hrefFinder(html):
    soup = BeautifulSoup(html, "html.parser")
    hrefs = set()

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if href.startswith("http://") or href.startswith("https://"):
            result = subprocess.run(f'curl -L -o NUL -s -w "%{{http_code}}" "{href}"',capture_output=True,text=True,shell=True)
            status = result.stdout.strip()
            hrefs.add((href, status))
    return hrefs

def LinksFinder(html):
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]

        if href.startswith("http://") or href.startswith("https://"):
            result = subprocess.run(f'curl -L -o /dev/null -s -w "%{{http_code}}\n" "{href}"', capture_output=True, text=True, shell=True)
            links.add((href, result.stdout.strip()))

    return links


def ExternalLinkFinder(domain):
    clean_domain = (
        domain.replace("https://", "")
        .replace("http://", "")
        .strip("/")
        .lower()
    )

    request_url = f"https://{clean_domain}"

    response = requests.get(
        request_url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    response.raise_for_status()

    Links = LinksFinder(response.text)

    Subdomains = find_subdomains(clean_domain)

    subdomain_hosts = {
        subdomain[0].strip().lower()
        for subdomain in Subdomains
    }

    for link in list(Links):
        url = link[0]  # extract URL from tuple
        hostname = urlparse(url).hostname

        if hostname:
            hostname = hostname.strip().lower()

            if hostname in subdomain_hosts:
                Links.remove(link)

            elif hostname.endswith(clean_domain):
                Links.remove(link)

    return Links

def InternalLinkFinder(domain):
    clean_domain = (
        domain.replace("https://", "")
        .replace("http://", "")
        .strip("/")
        .lower()
    )

    request_url = f"https://{clean_domain}"

    response = requests.get(
        request_url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    response.raise_for_status()

    Links = hrefFinder(response.text)

    InternalLinks = set()

    for link in Links:
        url = link[0]  # extract URL from tuple
        hostname = urlparse(url).hostname

        if hostname:
            hostname = hostname.strip().lower()

            if hostname.endswith(clean_domain):
                InternalLinks.add(link)

    return InternalLinks


if __name__ == "__main__":
    target = input("Enter the domain to find external links: ")

    try:
        links = ExternalLinkFinder(target)

        if links:
            print("\nExternal Links Found:\n")

            for link in sorted(links):
                print(link)

        else:
            print("\nNo external links found.")

    except Exception as e:
        print(f"\nError: {e}")