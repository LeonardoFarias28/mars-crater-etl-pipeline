import zipfile
import os
from playwright.sync_api import Playwright


def download_data(playwright: Playwright, url) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)

    download_dir = os.path.join(os.path.expanduser("~"), "Downloads", "mars_data")
    os.makedirs(download_dir, exist_ok=True)

    with page.expect_download() as download_info:
        page.get_by_role("link", name="Database as of").click()
    download = download_info.value
    file_path = os.path.join(download_dir, download.suggested_filename)
    download.save_as(file_path)

    print(f"File save: {file_path}")

    context.close()
    browser.close()

    return file_path

def unzip_file(zip_path: str) -> str:

    extract_dir = os.path.dirname(zip_path)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

        extracted_files = zip_ref.namelist()

    extracted_file_path = os.path.join(extract_dir, extracted_files[0])

    print(f"File extracted: {extracted_file_path}")

    return extracted_file_path

