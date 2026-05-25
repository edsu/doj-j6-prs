#!/usr/bin/env python3

import time

from playwright.sync_api import sync_playwright

output = open("missing.txt", "w")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for url in open("urls.txt"):
        url = url.strip()
        page.goto(url)

        if 'Page not found' in page.inner_html('body'):
            print(url)
            output.write(url + "\n")

        time.sleep(1)
