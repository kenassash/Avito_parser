import time
from seleniumbase import SB


class AvitoParser:
    def __init__(self, url: str, items: list, count: int = 10, ):
        self.url = url
        self.items = items
        self.count = count

    def __get_url(self):
        self.driver.open(self.url)

    def __paginator(self):
        while self.count > 0:
            self.__parse_page()
            if self.driver.find_elements('css selector', '[data-marker*="pagination-button/nextPage]"'):
                self.driver.find_element('css selector', '[data-marker*="pagination-button/nextPage]"').click()
                self.count -= 1


    def __parse_page(self):
        titles = self.driver.find_elements('css selector', '[data-marker="item"]')
        for title in titles:
            NAME = ('css selector', "[itemprop='name']")
            name = title.find_element(*NAME).text

            URL = (By.CSS_SELECTOR, "[data-marker='item-title']")
            url = title.find_element(*URL).get_attribute("href")

            print(name, url)

    def parse(self):
        with SB(uc=True, headed=True, block_images=True) as self.driver:
            self.__get_url()
            self.__paginator()


if __name__ == '__main__':
    AvitoParser(url='https://www.avito.ru/amurskaya_oblast_blagoveschensk/telefony?cd=1', items=['iphone'], count=1).parse()