import requests
from lxml import html
import re
import json
import csv
import click
 
def write_to_json(filename, data):
    f = open(filename, 'w')
    f.write(json.dumps(data))
    f.close()
 
 
def write_to_csv(filename, data):
    headers = ['title', 'url', 'price', 'amount of searches']
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerow(data)
 
@click.command()
@click.option('--ebayurl', default='https://www.ebay.com/itm/Nike-Free-RN-2018-White-Black-942836-100-Mens-Running-Shoes-NEW/153992200465?var=454094203427', help='Please provide a book url from https://www.ebay.com/trending')
@click.option('--filename', default='assign1_output.json', help='Please provide a filename CSV/JSON')

def scrape(ebayurl, filename):
    resp = requests.get(url=ebayurl, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    })
 
    tree = html.fromstring(html=resp.text)
    product_main = tree.xpath("//div[contains(@id, 'LeftSummaryPanel')]")[0]
    title = product_main.xpath(".//*[@id='itemTitle']/text()")[0]
    URL = "https://www.ebay.com/itm/Nike-Free-RN-2018-White-Black-942836-100-Mens-Running-Shoes-NEW/153992200465?var=454094203427"
    Price = product_main.xpath(".//*[@id='prcIsum']/text()")[0]

    
    searches = product_main.xpath(".//*[@id='vi_notification_new']/span/text()")[0]
    

    assign1_information = {
        'title': title,
        'url': URL ,
        'price': Price,
        'amount of searches': searches
    }
 
    print(assign1_information)
    extension = filename.split('.')[1]
 
    if extension == 'json':
        write_to_json(filename, assign1_information)
    elif extension == 'csv':
        write_to_csv(filename, assign1_information)
    else:
        click.echo("The extension your provided is not supported please use csv or json")
 
if __name__ == '__main__':
    scrape()

# {
#     "name": "...",
#     "url": "...",
#     "info": "...",
#     "searches": "..."
# }
