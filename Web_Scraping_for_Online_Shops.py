
# -*- coding: utf-8 -*-

#- Web Scraping for Online Shops
import requests
from lxml import html, etree

LAZADA_URL = "https://www.lazada.co.th/products/apple-iphone-11-i449100014-s829158696.html?spm=a2o4m.searchlistcategory.list.1.17ea4e9foRag5w&search=1"
SHOPEE_URL = 'https://shopee.co.th/Apple-iPhone-11-64GB-(TH)-%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%A8%E0%B8%B9%E0%B8%99%E0%B8%A2%E0%B9%8C1%E0%B8%9B%E0%B8%B5--i.133202612.3115813397'

def Lazada_scrape( LAZADA_URL ):
    script = '''
        headers = {
        ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        ['cookie'] = '_uab_collina=157271175786472924487354; lzd_cid=af1540c2-83a7-4fce-9487-9a5cec5ca766; t_uid=49638848-e464-4481-fdf1-9ea5782ad9a8; t_fv=1572711764418; pdp_sfo=1; miidlaz=miid5h31dt1dsbsn3vigp35; cna=TYpyFlJpxAICAQEvQNtOk666; cto_lwid=df7c881b-16c2-4668-8c59-a3b5be6a854b; _fbp=fb.2.1576652225801.800938252; _ga=GA1.3.502802355.1576652243; cto_axid=9g5lJozDsf4EheRDHQqubs8_x07AdRLK; ab.storage.deviceId.7f5273fc-4f97-4a9a-9f19-e816c0d197be=%7B%22g%22%3A%22c9b753d3-e1f7-115d-368b-043d0a34f3ba%22%2C%22c%22%3A1586977953985%2C%22l%22%3A1586977953985%7D; ab.storage.sessionId.7f5273fc-4f97-4a9a-9f19-e816c0d197be=%7B%22g%22%3A%223b67f08b-6065-babd-a6c2-f3fb86aaae80%22%2C%22e%22%3A1586980486362%2C%22c%22%3A1586977953980%2C%22l%22%3A1586978686362%7D; _bl_uid=m7kg29F4vg8jt1say678rgbyy57d; XSRF-TOKEN=35f20527-f543-461f-898e-6656db72bfd4; lzd_sid=1cf9cec8b03afd6a645d5930d4b97482; _tb_token_=7ef53b3ede616; hng=TH|th|THB|764; userLanguageML=th; t_sid=gTZ7N7PRskM2GTa9FaGcUEnsVIQCQO2d; utm_channel=NA; exlaz=c_%2FuZ3dL5pRwswDTCMS%2F%2BR7o6OCv5i9YcV4yzPV01knKc%3D; lzd_click_id=clk5h33dd1educat1hd42m; _gid=GA1.3.568239633.1595526191; _uetsid=4ec818d3d1a9444c7b3db42544d1f722; _uetvid=dc8e222f3709e688b345611c2811bfc4; l=eBP7LD8nqvs1m7ZtBOfanurza77OSIRYzuPzaNbMiOCP_3fp5gChWZk6FKY9C3MNhs1pR3SyK4s3BeYBcQAonxvTajwngjkmn; isg=BC0t-UDeDpWXMOiZEiOz58WNPM-nimFcMMfnvG8yTkQ65k2YN9gBLaOk1qIAgHkU',
        }
        
        splash:set_custom_headers(headers)
        splash.private_mode_enabled = false
        splash.images_enabled = false
        assert(splash:go(args.url))
        assert(splash:wait(1))
        return splash:html()

    '''

    resp = requests.post(url='http://localhost:8050/run',json={
        'lua_source':script,
        'url': str(LAZADA_URL)
    })

    hp = etree.HTMLParser(encoding='utf-8')
    tree = html.fromstring(html=resp.text, parser=hp)
    deals = tree.xpath("//*[@id='module_product_title_1']")
    
    product = {'name':'','detail':'','shop':'','original_price':'','discounted_price':'',}
    for deal in deals:

        product = {
            'name' : deal.xpath("./div/div/span/text()")[0] ,
            'detail' : deal.xpath('//*[@id="module_sku-select"]/div/div[2]/div/div/div[1]/span/text()')[0],
            'shop' : deal.xpath('//*[@id="module_seller_info"]/div/div[1]/div[1]/div[2]/a[1]/@href')[0] ,
            'original_price' : deal.xpath('//*[@id="module_product_price_1"]/div/div/div/span[1]/text()')[0],
            'discounted_price' : deal.xpath('//*[@id="module_product_price_1"]/div/div/span/text()')[0]
        }
    return product

def Shopee_scrape( SHOPEE_URL ):

    script = '''
        headers = {
        ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        ['cookie'] = '_gcl_au=1.1.1663624262.1595521788; _med=refer; _fbp=fb.2.1595521788337.1205732179; SPC_IA=-1; SPC_EC=-; SPC_F=z4nJ4h8DC2z2WPlauS7wiU872yV7Pm2M; REC_T_ID=be96f202-cd01-11ea-95a2-340a98386a15; SPC_SI=7d8dht3j6b6af8fc56h47qhu7sda0qn4; SPC_U=-; csrftoken=6kKp26wkYgDeYW0g67qQfNusdMxAiKtm; welcomePkgShown=true; language=en; _ga=GA1.3.44286297.1595521794; _gid=GA1.3.366676188.1595521794; SPC_CT_23df62a0="1595530398.99RnT3vNHPY0kVn9uisLWDzBMHz8ijkRSPI2DvV/Bmw="; AMP_TOKEN=%24NOT_FOUND; SPC_R_T_ID="DRmsdmckNqXIeT5STmGa7+RUNPYgNM26CbJIKpNix7s/rsId/t/4AR2+xFXqK/64u+dPXTf59g66RpTZroU9idMskdPWqQurh/bjmMOiYwI="; SPC_T_IV="Po2MuoA5O2zH448KfPd6yg=="; SPC_R_T_IV="Po2MuoA5O2zH448KfPd6yg=="; SPC_T_ID="DRmsdmckNqXIeT5STmGa7+RUNPYgNM26CbJIKpNix7s/rsId/t/4AR2+xFXqK/64u+dPXTf59g66RpTZroU9idMskdPWqQurh/bjmMOiYwI="',
        }
        
        splash:set_custom_headers(headers)
        splash.private_mode_enabled = false
        splash.images_enabled = false
        assert(splash:go(args.url))
        assert(splash:wait(1))
        return splash:html()
        '''

    resp = requests.post(url='http://localhost:8050/run',json={
        'lua_source':script,
        'url': str(SHOPEE_URL)
    })

    hp = etree.HTMLParser(encoding='utf-8')
    tree = html.fromstring(html=resp.text, parser=hp)

    deals = tree.xpath('//div[@class="flex-auto flex-column  _2TJgvU"]')
    product = {'name':'','detail':'','shop':'','original_price':'','discounted_price':'',}

    for deal in deals:
        product = {
            # 'name' : deal.xpath("./div[2]/span/text()")[0] 
            # 'detail' : deal.xpath('//*[@id="module_sku-select"]/div/div[2]/div/div/div[1]/span/text()')[0],
            # 'shop' : deal.xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/a/@href')[0] ,
            # 'original_price' : deal.xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div[1]/text()')[0]
            # 'discounted_price' : deal.xpath('//*[@id="module_product_price_1"]/div/div/span/text()')[0]
        }
    
    return product
    

    # print(product_2)

print( Lazada_scrape( LAZADA_URL ) )
print( Shopee_scrape( SHOPEE_URL ) )