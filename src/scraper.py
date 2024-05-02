import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import sys

def find_logo_and_phone(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        logo = soup.find('img')
        logo_url = urljoin(url, logo['src']) if logo and 'src' in logo.attrs else 'No logo found'

        text = soup.get_text()
        phone_regex = r'\+?\d{1,3}[\s-]?\(?\d{2,3}\)?[\s-]?\d{2,4}[\s-]?\d{2,4}(?:[\s-]?\d{2,4})?'
        phone_numbers = re.findall(phone_regex, text)
        cleaned_phones = [re.sub(r'[^\d+() -]', '', phone).strip() for phone in phone_numbers if len(phone) > 7]

        return {
            'url': url,
            'logo_url': logo_url,
            'phone_numbers': cleaned_phones
        }
    except requests.RequestException as e:
        print(f"Request error {url}: {str(e)}", file=sys.stderr)
    except Exception as e:
        print(f"Error processing {url}: {str(e)}", file=sys.stderr)
    return {}
