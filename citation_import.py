import requests
from bs4 import BeautifulSoup
import yaml
import os
import logging

def scrape_google_scholar(profile_url, output_dir, max_pages=100):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    start = 0
    has_more_pages = True
    citations = []
    page_count = 0

    logging.basicConfig(level=logging.INFO)
    
    while has_more_pages and page_count < max_pages:
        try:
            response = requests.get(f"{profile_url}&cstart={start}&pagesize=20", headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Check if there are any results on this page
            items = soup.select('.gsc_a_tr')
            if not items:
                logging.info("No more items found, ending scrape.")
                has_more_pages = False
                continue
            
            logging.info(f"Scraping page starting at index {start}")
            
            # Iterate through all citations on the current page
            for item in items:
                title_element = item.select_one('.gsc_a_at')
                if title_element:
                    title = title_element.text
                    # Check if 'data-href' attribute exists
                    link = 'https://scholar.google.com' + title_element['data-href'] if 'data-href' in title_element.attrs else ''
                else:
                    title = 'No title found'
                    link = ''
                
                authors_element = item.select_one('.gsc_a_at+ .gs_gray')
                authors = authors_element.text if authors_element else 'No authors found'
                
                publisher_element = item.select_one('.gs_gray+ .gs_gray')
                publisher = publisher_element.text if publisher_element else 'No publisher found'
                
                year_element = item.select_one('.gsc_a_h .gsc_a_y')
                year = year_element.text if year_element else 'No year found'
                
                # Citation structure
                citation = {
                    'title': title,
                    'authors': [author.strip() for author in authors.split(',')] if authors != 'No authors found' else [],
                    'publisher': publisher,
                    'date': year,
                    'link': link,
                    'plugin': 'orcid.py',
                    'file': 'orcid.yaml'
                }
                citations.append(citation)
            
            # Increment the start index for the next page
            start += 20
            page_count += 1
        except requests.RequestException as e:
            logging.error(f"Request failed: {e}")
            has_more_pages = False
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            has_more_pages = False
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Write each citation to a separate YAML file
    for i, citation in enumerate(citations):
        yaml_file = os.path.join(output_dir, f"citation_{i+1}.yaml")
        with open(yaml_file, 'w') as f:
            yaml.dump(citation, f, default_flow_style=False, sort_keys=False)
        logging.info(f"Saved citation {i+1} to {yaml_file}")

# Example profile URL (replace with the actual profile URL)
profile_url = 'https://scholar.google.com/citations?user=dlLdZhUAAAAJ'
scrape_google_scholar(profile_url, 'output_directory')
