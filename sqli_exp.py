import requests
import sys




# Headers for the request (optional)
headers = {
    "User-Agent": "Mozilla/5.0"
}
# url = sys.argv[1]
def test_sql_injection():
    # Read the url in file
    with open(sys.argv[1], 'r') as file:
        for url in file:
            vulnerable = False
            with open('payloads.txt', 'r') as file:
                # Read the payload in file
                for payload in file:
                    # Append the payload to the URL
                    test_url = f"{url.strip()}{payload}"
                    # print(test_url)
                    try:
                        response = requests.get(test_url, headers=headers)
                        # Check for common SQL injection error messages
                        if "sql syntax" in response.text.lower() or "mysql" in response.text.lower() or "syntax error" in response.text.lower():
                            with open('vulnUrls.txt', 'a') as file:
                                file.write(f"[!] yes Find : Vulnerable to SQL injection: {test_url}")
                            vulnerable = True
                            break
                    except requests.RequestException as e:
                        with open('error.txt', 'a') as file:
                           file.write(f"Error requesting {test_url}: {e}")

#                 if not vulnerable:
#                     print(f"[-] No SQL injection vulnerability found in : {test_url}")

test_sql_injection()
print("Finished procces ;)")
