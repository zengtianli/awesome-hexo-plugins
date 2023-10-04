import requests
from bs4 import BeautifulSoup

BASE_URL = "https://hexo.io/plugins/"

def get_plugins():
    response = requests.get(BASE_URL)
    if response.status_code != 200:
        print(f"Error: Unable to fetch the page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    plugins = soup.find('ul', id='plugin-list').find_all('li', class_='plugin')

    plugin_details = []
    for plugin in plugins:
        name_tag = plugin.find('a', class_='plugin-name')
        if name_tag:
            name = name_tag.text.strip()
            link = name_tag['href']
            plugin_details.append((name, link))
    
    return plugin_details

def get_stars_from_github(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Search for the tag containing the star count
    stars_tag = soup.find('span', class_='Counter js-social-count')
    if stars_tag:
        # Extract the number, handle 'k' notation, and convert to integer
        stars_str = stars_tag.text.strip().replace(',', '')
        if 'k' in stars_str:
            # Remove 'k' and convert to float, then multiply by 1000
            return int(float(stars_str.replace('k', '')) * 1000)
        else:
            return int(stars_str)
    return 0

plugins = get_plugins()
for name, link in plugins:
    stars = get_stars_from_github(link)
    print(f"Plugin Name: {name}, Link: {link}, Stars: {stars}")

