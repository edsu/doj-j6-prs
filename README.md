#  doj-j6-prs

The US Justice Department [removed] press releases related to the [January 6 US
Capitol Attack].

This repository contains some code to look at what press releases exist in the
Wayback Machine, and then looks at the live website to see which ones are
missing.

## Run

First, get a list of the HTML pages at `https://www.justice.gov/usao-dc/pr/` and write
them as `urls.txt`:

```
uv run inventory.py
```

Now you can check them, which should write out the URLs to a file `missing.txt`:

```
uv run check.py
```

[January 6 US Capitol Attack]: https://en.wikipedia.org/wiki/January_6_United_States_Capitol_attack 
[removed]: https://www.nbcnews.com/politics/justice-department/justice-department-deletes-press-releases-charges-jan-6-rioters-rcna346613
