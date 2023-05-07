import requests
import scrapy
from ..items import NewswebscrapeItem
import os


class NewsbotSpider(scrapy.Spider):
    name = 'newsbot'
    # start_urls = ['https://bengali.abplive.com/district/december-comes-to-end-but-high-temperature-may-increase-the-risk-of-dengue-945067']
    start_urls = ['https://bengali.abplive.com/news/kolkata/page-1']
    folder_name = 'image'

    def parse(self, response):
        for i in range(10):
            next_page = requests.get(
                'https://bengali.abplive.com/news/kolkata/' + 'page-' + str(i))
        # next_page = requests.get('https://bengali.abplive.com/news/kolkata/' + 'page-' + str(NewsbotSpider.page_number))
            np = scrapy.http.TextResponse(body=next_page.content,url='https://bengali.abplive.com/news/kolkata/' + 'page-' + str(i))
            print(np)

            next_article = np.css('div.other_news a').xpath('@href').extract()
            print(next_article)

            for links in next_article:
                print(links)
                yield response.follow(links, callback=self.itemparser)

    def itemparser(self, response):
        items = NewswebscrapeItem()

        heading = response.css('h1.article-title::text')[0].extract()
        title = response.css('h2.article-excerpt::text')[0].extract()
        description = response.css('div.article-data p::text').extract()
        # raw_image_urls = response.css('img.article_feature').xpath("@data-src")[0].extract()
        date = response.css('p.article-author::text')[3].extract()


        items['heading'] = heading
        items['title'] = title
        items['description'] = description
        # items['image'] = raw_image_urls
        items['date'] = date

        yield items

        # os.mkdir(os.path.join(os.getcwd(), NewsbotSpider.folder_name))
        # os.chdir(os.path.join(os.getcwd(), NewsbotSpider.folder_name))
        # with open(title + '.jpeg', 'wb') as f:
        #     im = requests.get(raw_image_urls)
        #     f.write(im.content)
