import requests

if __name__ == '__main__':
    a = input("请输入你要爬取网页的网址:")

    res = requests.get(url=a)

    g = res.text

    print(g)

    with open('./data.html', "w", encoding="utf-8") as fp:
        fp.write(g)

    print("OK")
