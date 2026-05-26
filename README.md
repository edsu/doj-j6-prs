#  doj-j6-prs

The US Justice Department [removed] press releases related to the [January 6 US
Capitol Attack].

This repository contains some code to look at what press releases exist in the
Wayback Machine, and then looks at the live website to see which ones are
missing.

## Run

The code runs in two phases:

1. `inventory`: which finds all the URLs for DoJ press release pages in the
   Wayback Machine and writes them as `urls.txt`.
2. `check`: which reads the urls and writes the ones that are missing from the
   live web as `missing.txt`.

You can run the `inventory` and `check` tasks together (or separately) with `make`.

[January 6 US Capitol Attack]: https://en.wikipedia.org/wiki/January_6_United_States_Capitol_attack 
[removed]: https://www.nbcnews.com/politics/justice-department/justice-department-deletes-press-releases-charges-jan-6-rioters-rcna346613
