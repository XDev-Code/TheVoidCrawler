import subprocess


def find_subdomains(domain):
    try:
        Domains = []
        result = subprocess.run(["curl", "https://api.hackertarget.com/hostsearch/?q=" + domain], capture_output=True, text=True, shell=True)

        if result.returncode == 0:
            subdomains = result.stdout.strip().split("\n")
            for subdomain in subdomains:
                status = subprocess.run(f'curl -o NUL -s -L -w "%{{http_code}}" {subdomain.split(",")[0]}',capture_output=True,text=True,shell=True)
                Domains.append((subdomain.split(",")[0], status.stdout.strip()))
            # returns the domains + status code
            return Domains
        else:
            print("Error occurred while fetching subdomains.")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
if __name__ == "__main__":
    domain = input("Enter the domain to find subdomains: ")
    subdomains = find_subdomains(domain)
    if subdomains:
        print("Subdomains found:")
        for subdomain in subdomains:
            print(f"{subdomain[0]} - Status: {subdomain[1]}")