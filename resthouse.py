# -*- coding: gbk -*-
import requests
import bs4


def get_lastdata():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    data = requests.get("http://zu.tj.fang.com/house/n31/", headers=headers)
    # ��Ϊ��ӡ�����ĸ�ʽ�����룬���Ը���һ�±���
    data.encoding = "gbk"
    soup = bs4.BeautifulSoup(data.text, "html.parser")
    # ����
    title = soup.find_all("p", "title")
    #print(title)
    # �۸�
    price = soup.select("#listBox > div.houseList > dl:nth-of-type(1) > dd > div.moreInfo > p > span")
    print(price)
    # ���������
    concretedata = soup.select("#listBox > div.houseList > dl:nth-of-type(1) > dd > p.font15.mt12.bold")
    print(concretedata)

    for title, price, concretedata in zip(title, price, concretedata):
        last_data = {
            "title": title.get_text().strip(),
            "concretedata": concretedata.get_text().strip(),
            "price": price.get_text().strip()
        }

        print(last_data)


if __name__ == '__main__':
    get_lastdata()
