from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests


class Website(ABC):

    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name

    @abstractmethod
    def get_articles(self):
        pass


class Pixnet(Website):

    # 取得餐廳食記
    def get_articles(self):

        result = []  # 回傳結果

        if self.restaurant_name:  # 如果非空值，才進行爬取

            # 取得第一頁的資料
            response = requests.get(
                f"https://www.pixnet.net/mainpage/api/tags/{self.restaurant_name}/feeds?filter=articles&sort=latest&per_page=15")

            # 取得食記資料
            feeds = response.json()["data"]["feeds"]

            for feed in feeds:
                avatar = feed["avatar"]  # 食記作者大頭貼
                author = feed["display_name"]  # 食記作者
                title = feed["title"]  # 食記標題
                hit = feed["hit"]  # 食記點擊次數
                link = feed["link"]  # 食記連結
                source = "痞客邦"  # 食記來源網站

                result.append(
                    dict(avatar=avatar, author=author, title=title, hit=hit, link=link, source=source))

        return result
