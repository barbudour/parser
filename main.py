import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import markdown2
import html2text

url = "https://mytessa.ru/docs/3.6/api/html/G_Tessa.htm"
prefix = "https://mytessa.ru/docs/3.6/api/html/"
output_path = "content/"
links_file = "links.txt"


def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def read_links_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def get_links_recursive(soup, depth=100):
    links = [
        link.get("href")
        if link.get("href") and not link.get("href").startswith("#")
        else None
        for link in soup.select(".toc-menu a")
    ]

    links = [
        prefix + link if link and not link.startswith("/") else link for link in links
    ]

    if depth > 0:
        toggle_buttons = soup.find_all("button", {"class": "toggle"})

        for button in toggle_buttons:
            if "toggleExpanded" not in button.get("class", []):
                button.click()
                WebDriverWait(driver, 10).until(EC.staleness_of(soup))

                expanded_items = driver.execute_script(
                    'return document.querySelectorAll(".toggle.expanded")'
                )

                button.click()

                for item in expanded_items:
                    item.click()

                time.sleep(0.1)

                soup = BeautifulSoup(driver.page_source, "html.parser")
                time.sleep(0.1)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        sub_links = get_links_recursive(soup, depth - 1)
        if sub_links:
            links += sub_links

    return links


def save_content_to_file(link, content, total_links, current_index):
    filename = os.path.join(
        output_path, link.replace(prefix, "").replace("/", "_").lstrip("_") + ".md"
    )
    filepath = os.path.join(output_path, filename)

    ensure_directory_exists(output_path)

    soup = BeautifulSoup(content, "html.parser")
    markdown_content = html2text.html2text(str(soup.select_one("#TopicContent")))

    with open(filename, "w", encoding="utf-8") as file:
        file.write(markdown_content)

    completion_percentage = (current_index + 1) / total_links * 100
    print(f"Saved content for {link} - {completion_percentage:.2f}% complete")


try:
    driver = webdriver.Chrome()
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    all_links = read_links_from_file(links_file)

    total_links = len(all_links)

    for index, link in enumerate(all_links):
        full_url = link
        try:
            driver.get(full_url)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "TopicContent"))
            )

            content = driver.page_source
            save_content_to_file(link, content, total_links, index)
        except Exception as e:
            print(f"Failed to retrieve content for {link}: {e}")

finally:
    driver.quit()
