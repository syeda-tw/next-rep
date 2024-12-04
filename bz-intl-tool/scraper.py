import requests
import json
from bs4 import BeautifulSoup

def run_scraper():
    url = "https://job.fibladi.com/fr"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
        select_element = soup.find('select', id='wilaya-input')

        if select_element:
            option_elements = select_element.find_all('option')
            region_values = [option['value'] for option in option_elements]
            
            for region in region_values:
                try:
                    print(f"Scraping data for region: {region}")
                    run_child_scraper(region)
                except Exception as e:
                    print(f"Error processing region {region}: {e}")
        else:
            print("Failed to fetch data from the URL")


def run_child_scraper(region):
    url = f"https://job.fibladi.com/fr/search?q=&region={region}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content.decode('ISO-8859-1'), 'html.parser')
        list_items = soup.find_all('li', class_='view-list list-item')
        scraped_data = []

        for item in list_items:
            try:
                link = item.find('a')['href']
                title = item.find('h2', class_='h4').get_text(strip=True)
                description = item.find('p', class_='description').get_text(strip=True)[:500] if item.find('p', class_='description') else ""
                image = item.find('img')['data-src'] if item.find('img') else "No image available"

                wilaya_element = item.find('span')
                if wilaya_element:
                    wilaya = wilaya_element.get_text(strip=True)
                else:
                    wilaya = "Unknown"

                item_data = {
                  "Link": link.strip().replace('"', ''),  # Strip leading and trailing whitespace, remove double quotes
                  "Title": title.strip().replace('"', ''),  # Strip leading and trailing whitespace, remove double quotes
                  "Image": image.strip().replace('"', ''),  # Strip leading and trailing whitespace, remove double quotes
                  "Wilaya": wilaya.strip().replace('"', ''),  # Strip leading and trailing whitespace, remove double quotes
                  "Description": description.replace('"', '').replace('\n', ' ')  # Remove double quotes and newline characters, replace with space
                }
                scraped_data.append(item_data)
            except Exception as e:
                print(f"Error processing item: {e}")

        # Load existing data if any
        try:
            with open("scraped_data.json", "r", encoding='utf-8') as json_file:
                existing_data = json.load(json_file)
        except FileNotFoundError:
            existing_data = []

        # Append new data to existing or create new list
        all_data = existing_data + scraped_data

        # Write all data to JSON file
        with open("scraped_data.json", "w", encoding='utf-8') as json_file:
            json.dump(all_data, json_file, indent=4, ensure_ascii=False)
        
        print(f"Scraped data for region {region} saved successfully")
    else:
        print(f"Failed to fetch data for region {region} from the URL")
