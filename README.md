# Vajirayana Scraper
Python vajirayana.org thai literature data gathering module

## Installation
```bash
pip install vajirayana
```
## Usage
Gather any Literature data from vajirayana.org


```python
from vajirayana import scraper
vaj_scraper = scraper.Scraper('./data') # output directory
vaj_scraper.scrape('Literature_page_url', strip_first_section=False) # scrape url
```