function main(splash, args)
    headers = {
        ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        ['cookie'] = 'lzd_cid=933035ae-f783-4530-fdd4-c821c3e4564d; t_uid=933035ae-f783-4530-fdd4-c821c3e4564d; t_fv=1595510371177; t_sid=Z5hI1paaNG65L8rrLAJ8bNcXGj7pztX2; utm_channel=NA; hng=TH|en|THB|764; userLanguageML=en; lzd_sid=19239b83754729ddf57c08be5e682fc8; _m_h5_tk=b35fd3728d408dd540713a96466b133f_1595517938391; _m_h5_tk_enc=c799d57f7a134a3de3a8512b1b03be8e; cna=anygF9kfpEwCATEx7Rr7eRFK; _bl_uid=myktXcp6ykgtFqohthj8r6g9ggzn; _tb_token_=d33ae66e4013; _fbp=fb.2.1595510372377.2136847281; _ga=GA1.3.1719052397.1595510401; _gid=GA1.3.1891054345.1595510401; _gat_UA-30236174-1=1; JSESSIONID=D834DC0E0AED371D053E3C3DA20C2527; _uetsid=cc00390c57ae2238857f7721769382d2; _uetvid=abec04ea9a340b8847cc28404e4ccfaa; l=eBxTSFSqONFJYFaLBOfanurza77OSIRvSuPzaNbMiOCPOT5p5NiCWZk1EDL9C3HNhsdDR3oIr-vbBeYBqSD1j6GSjq7YiSDmn; isg=BEJCOkZcqQSmJrVYkCRfvAqJk0ikE0YtqA1674xbf7Um3-JZdKLpPe-NjMOjur7F'
      }
      
      splash:set_custom_headers(headers)
      assert(splash:go(args.url))
      assert(splash:wait(1))
      return splash:html()
end