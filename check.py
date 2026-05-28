#!/usr/bin/env python3

import time
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError

urls_file = Path("urls.txt")
output_file = Path("missing.txt")

# pick up where we left off if possible
last_checked = None
if output_file.is_file():
    for line in output_file.open("r"):
        last_checked = line.strip()


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    # append to output in case we are picking up again
    output = output_file.open("a")

    for url in urls_file.open("r"):
        url = url.strip()

        if last_checked is not None:
            if last_checked == url:
                last_checked = None
            print(f"skipping {url}")
            continue

        max_tries = 5
        for attempt in range(1, max_tries):
            try:
                page.goto(url)
                break
            except TimeoutError as e:
                print(f"Timeout on attempt {attempt} for {url}: {e}")
                time.sleep(10)
                if attempt == max_tries:
                    print(f"Giving up on {url}")
                    break

        if 'Page not found' in page.inner_html('body'):
            print(f"💥 {url}")
            output.write(url + "\n")
        else:
            print(f"✅ {url}")

        time.sleep(1)
