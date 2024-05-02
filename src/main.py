import sys
import json
from concurrent.futures import ThreadPoolExecutor
from scraper import find_logo_and_phone

def main():
    urls = sys.stdin.read().splitlines()
    results = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(find_logo_and_phone, urls))

    print(json.dumps(results, indent=4))

if __name__ == "__main__":
    main()
