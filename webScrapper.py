from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dataclasses import dataclass
from typing import List
import json

@dataclass
class ArrestRecord:
    date: str
    first_name: str
    last_name: str
    team: str
    position: str
    case: str
    category: str
    description: str

def fetch_arrest_records(base_url: str, max_pages: int = 5) -> List[ArrestRecord]:
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    records = []

    try:
        for page in range(1, max_pages + 1):
            url = f"{base_url}/page/{page}/"
            driver.get(url)

            # Wait until the table is present
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "table"))
            )

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find('table')


            if not table:
                print(f"No table found on page {page}")
                continue

            rows = table.find_all('tr')[1:]  # Skip header row
            for row in rows:
                cols = row.find_all('td')
                if len(cols) < 7:
                    continue
                record = ArrestRecord(
                    date=cols[0].get_text(strip=True),
                    first_name=cols[1].get_text(strip=True),
                    last_name=cols[2].get_text(strip=True),
                    team=cols[3].get_text(strip=True),
                    position=cols[4].get_text(strip=True),
                    case=cols[5].get_text(strip=True),
                    category=cols[6].get_text(strip=True),
                    description=cols[7].get_text(strip=True)
                )
                records.append(record)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

    return records

def records_to_json(records: List[ArrestRecord]) -> str:
    return json.dumps([record.__dict__ for record in records], indent=4)

def save_to_file(data: str, filename: str) -> None:
    with open(filename, 'w') as file:
        file.write(data)

if __name__ == "__main__":
    base_url = "https://databases.usatoday.com/nfl-arrests"
    try:
        arrest_records = fetch_arrest_records(base_url, max_pages=5)
        if arrest_records:
            json_data = records_to_json(arrest_records)
            save_to_file(json_data, 'arrest_records.json')
            print("Arrest records saved to 'arrest_records.json'")
        else:
            print("No arrest records found.")
    except Exception as e:
        print(f"An error occurred: {e}")
