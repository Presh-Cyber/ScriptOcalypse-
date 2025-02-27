import requests
import argparse
import json
import urllib3
import sys
from urllib.parse import urlparse, urlunparse
from termcolor import colored

# Suppress warnings from unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_swagger_data(swagger_url, proxy=None, verify_ssl=False):
    proxies = {"http": proxy, "https": proxy} if proxy else None
    try:
        response = requests.get(swagger_url, proxies=proxies, verify=verify_ssl)
        response.raise_for_status()
        
        try:
            return response.json()
        except json.JSONDecodeError:
            print("Error: Received an invalid JSON response. Ensure the URL points to a valid Swagger JSON.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None

def extract_endpoints(swagger_data, new_domain=None):
    if not swagger_data:
        return []
    
    endpoints = []
    
    # Determine API base URL
    if "servers" in swagger_data:  # OpenAPI 3.x
        base_urls = [server.get("url", "") for server in swagger_data.get("servers", [])]
    else:  # Swagger 2.0
        scheme = swagger_data.get("schemes", ["https"])[0]  # Default to https
        host = swagger_data.get("host", "")
        base_path = swagger_data.get("basePath", "")
        base_urls = [f"{scheme}://{host}{base_path}"] if host else []
    
    # Extract endpoints
    for path, methods in swagger_data.get("paths", {}).items():
        for method in methods:
            for base_url in base_urls:
                parsed_base_url = urlparse(base_url)
                scheme = parsed_base_url.scheme or "https"
                netloc = parsed_base_url.netloc
                full_url = f"{scheme}://{netloc}{parsed_base_url.path}{path}"
                
                if new_domain:
                    parsed_url = urlparse(full_url)
                    full_url = urlunparse((parsed_url.scheme, new_domain, parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment))
                
                endpoints.append(full_url)
    
    return endpoints


def check_endpoints(endpoints, proxy=None, verify_ssl=False):
    proxies = {"http": proxy, "https": proxy} if proxy else None
    for endpoint in endpoints:
        try:
            response = requests.get(endpoint, proxies=proxies, verify=verify_ssl, timeout=5)
            status_code = response.status_code
            if status_code == 200:
                print(colored(f"{endpoint:<80} [200]", "green"))
            elif status_code == 404:
                print(colored(f"{endpoint:<80} [404]", "red"))
            else:
                print(colored(f"{endpoint:<80} [{status_code}]", "cyan"))
        except requests.exceptions.RequestException:
            print(colored(f"{endpoint:<80} [Error]", "red"))
        except KeyboardInterrupt:
            print("\nScript was stopped by user...")
            sys.exit(0)

def main():
    ascii_art = """

┏┓       ┏┓┓     
┗┓┓┏┏┏┓┏┓┣ ┃┏┓┏┓╋
┗┛┗┻┛┗┻┗┫┻ ┗┗ ┗ ┗
        ┛  by pr35h_Cy63r       

    """
    print(ascii_art)
    
    parser = argparse.ArgumentParser(description="Extract API endpoints from a Swagger JSON document.")
    parser.add_argument("-u", "--url", required=True, help="Swagger JSON URL. Ensure it's a valid Swagger documentation link.")
    parser.add_argument("-d", "--domain", help="Replace the domain in extracted endpoints with a custom domain.")
    parser.add_argument("--proxy", help="Proxy URL to route requests through Brupsuit. Can only be used with --check.")
    parser.add_argument("--verify", action="store_true", help="Enable SSL certificate verification (default is disabled).")
    parser.add_argument("--check", action="store_true", help="Check if endpoints return a 200 or 404 status.")
    
    args = parser.parse_args()
    
    if args.proxy and not args.check:
        print("Error: --proxy can only be used alongside --check.")
        return
    
    swagger_data = fetch_swagger_data(args.url, args.proxy, args.verify)
    if swagger_data:
        endpoints = extract_endpoints(swagger_data, args.domain)
        if args.check:
            check_endpoints(endpoints, args.proxy, args.verify)
        else:
            for endpoint in endpoints:
                print(colored(f"{endpoint:<80}", "yellow"))
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript was stopped by user...\n")
        sys.exit(0)
