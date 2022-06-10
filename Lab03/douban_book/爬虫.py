import requests;
from bs4 import BeautifulSoup;


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    resp = requests.get(url, headers=headers).text;
    return resp;


def html_parser():
    for url in all_page():
        soup = BeautifulSoup(get_html(url), 'lxml');
        print(soup)
        # 书名
        allDiv = soup.find_all('div', class_='info')
        names = [a.find("a")["title"] for a in allDiv];

        # 作者
        versions = [];
        pubs = soup.find_all(class_="pub");
        versions = [i.get_text().strip() for i in pubs];

        # 评分
        ratingNums = soup.find_all(class_="rating_nums");
        ratings = [i.get_text().strip() for i in ratingNums];

        # 简介
        allDiv2 = soup.select('.info p');
        jianjie = [i.get_text().strip() for i in allDiv2];
        # jianjie = [a.find("p").get_text().strip() for a in allDiv2];
        for name, version, rating, p in zip(names, versions, ratings, jianjie):
            name = "书名：" + str(name) + "\n";
            version = "作者：" + str(version) + "\n";
            rating = "评分：" + str(rating) + "\n";
            p = "简介：" + str(p) + "\n";
            data = name + version + rating + p;
            print("data=",data)
            f.writelines(data + "==================" + "\n");


def all_page():
    base_url = "https://book.douban.com/tag/%E6%8E%A8%E7%90%86%E5%B0%8F%E8%AF%B4?start=";
    urlList = [];
    for page in range(0, 1000, 20):
        print(page)
        allurl = base_url + str(page)+'&type=T';
        urlList.append(allurl);
    return urlList;


filename = "豆瓣读书tl.txt";
f = open(filename, 'w', encoding="utf-8");
html_parser();
f.close();
print("保存成功 ");