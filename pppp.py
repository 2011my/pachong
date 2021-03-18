import requests
if __name__ == '__main__':
    a = input("请输入你要爬取网页的网址:")
    b = input("请输入爬取数据保存文件名(不需要拓展名):")
    c = b + ".html"
    res = requests.get(url=a)

    g = res.text

    print(g)

    with open(c, "w", encoding="utf-8") as fp:
        fp.write(g)

    print("OK")