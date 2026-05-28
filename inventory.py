import wayback

urls = set()
wb = wayback.WaybackClient()
for rec in wb.search('https://www.justice.gov/usao-dc/pr/*', filter_field=['mimetype:text/html']):

    # some of these aren't 200 OK
    if rec.status_code != 200:
        continue

    if rec.original.startswith('http://'):
        continue
    
    # there are some non-canonical URLs in there that must've been discovered by scraping the html
    if '?' in rec.original or '&' in rec.original or '%' in rec.original:
        continue

    if rec.original not in urls:
        urls.add(rec.original)
        print(rec.original)

output = open("urls.txt", "w")
for url in sorted(urls):
    output.write(url + "\n")
