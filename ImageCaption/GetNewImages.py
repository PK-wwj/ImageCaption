"""https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1684051103692_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=&ie=utf-8&sid=&word=%E4%B8%80%E4%B8%AA%E7%BA%A2%E8%89%B2%E7%9A%84%E7%90%83"""
import os
import shutil
import requests
import simplejson as json1
import json

def download_image(url, i):

    with open(f'NewImages/{i}.jpg', 'wb') as f:
        print(i)
        f.write(requests.get(url).content)

def scrape_images(query, count=10, path='./NewImages'):
    #爬虫主体
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42',
        'Host': 'image.baidu.com',
        'Cookie': 'BDqhfp=%E8%8B%B9%E6%9E%9C%26%260-10-1undefined%26%261020%26%262; BIDUPSID=26F9CE6D9F3FB1EDECD2704B27AF2FA0; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BAIDUID=26F9CE6D9F3FB1EDDBD3894BD1C7DD14:FG=1; BAIDUID_BFESS=26F9CE6D9F3FB1EDDBD3894BD1C7DD14:FG=1; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=cn.bing.com; firstShowTip=1; indexPageSugList=%5B%22%E8%8B%B9%E6%9E%9C%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; ab_sr=1.0.1_NzM4ZmZjMGNmMWVhYmYwZTNkZWVjOTRmMDg4ODEwZmFiNTQyMDkyZDkxMWY2NjcxZjQzNGMyOWY3MzFmMjY4YjRkY2I3NWQ4OTk1MzBiN2NmM2FhMjg0NWNlOTBlNTY4NWU3ZDAzMTIyNzY4YzlkMDFmOWEzMWNlNWFkNzc4Y2JjNTg1N2I3Y2JkNDAxYjVlMTJlNzM0NGM2ZWYzYTRmYw==',
       'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111110&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%8B%B9%E6%9E%9C&oq=%E8%8B%B9%E6%9E%9C&rsp=-1'
    }
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10619707237655351117&ipn=rj&ct=201326592&is=&fp=result&fr=&word={query}&queryWord={query}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=90&rn=30&gsm=5a&1684067853330='.format(query=query)

    print(url)
    response = requests.get(url, headers=headers)

    #强制删除再创建该文件夹
    shutil.rmtree(path)
    os.mkdir(path)
    # print(response.json())
    num=0
    #for item in response.json(strict=False).get('data', []):#
    #for item in json.loads(response.text, strict=False).get('data', []):
    #for item in json.loads(response.content.decode('utf-8'), strict=False).get('data', []):
    try:
        # 尝试使用第三方库进行解析
        data = json1.loads(response.content.decode('utf-8'), strict=False)
    except json.JSONDecodeError:
        # 如果报错，则使用原生的 json 模块进行解析
        data = json.loads(response.text, strict=False)

    num = 0
    for item in data.get('data', []):
        print(item)
        if (item.get('thumbURL') and num <= count):
            url = item['thumbURL']
            print(url)

            try:
                download_image(url, num)
                num=num+1
            except:
                print('erro')
                pass


def read_parameters(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    # 解析参数
    param1 = lines[0].strip()
    param2 = lines[1].strip()

    return param1, param2

if __name__ == '__main__':
    count = 10
    path = '/NewImages'
    query='一个男人在打棒球'
    scrape_images(query, count, path)