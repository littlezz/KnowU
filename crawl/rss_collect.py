from collections import defaultdict
import re
import feedparser
from lxml import etree
from requests import get as _get
from .decorators import retry_connect, resolve_timeout
from . import models
import logging
logging.basicConfig(level=logging.WARNING, format='%(message)s')
__author__ = 'zz'

##############3 CONFIG #############
RETRY_TIME = 3
TIMEOUT = 5
###################################


@retry_connect(RETRY_TIME, TIMEOUT)
def requests_get(url, **kwargs):
    return _get(url, **kwargs)





class Article:
    _property_attr = ['title', 'link', 'author', 'tags']

    def __init__(self, feedparser_dict):
        self._dict = feedparser_dict

    def __getattribute__(self, item):
        if item in Article._property_attr:

            return self._dict[item]
        else:
            return super().__getattribute__(item)

    @property
    def content(self):
        try:
            return self._dict['content'][0].value
        except KeyError:
            return self._dict['summary']


class RssCollect:
    '''get rss info from a rss collect file
    usage:
        rc = RssCollect(path/.xml)
        for catalog in rc.catalogues:
            for rssinfo in rc.result[catalog]:
                url = rssinfo['url']
    '''

    def __init__(self, path):
        self.doc = etree.parse(path)
        self.catalogues = []
        self.result = defaultdict(list)
        self.collect()

    def collect(self):
        for catalogue in self.doc.iterfind('body/outline'):

            self.catalogues.append(catalogue.get('title'))
            for rss in catalogue:
                self.result[catalogue.get('title')].append(dict(url=rss.get('xmlUrl'),
                                                                title=rss.get('title')))


class RssContentGet:
    def __init__(self, xmlurl):

        self.xmlurl = xmlurl

    @resolve_timeout(None)
    def get_rss(self):
       return requests_get(self.xmlurl)

    @property
    def articles(self):
        '''
        gen of Ariticle
        '''
        res = self.get_rss()
        if res is None:
            logging.debug('unavailable %s', self.xmlurl)
            return []
        self.rss = feedparser.parse(res.text)
        for entry in self.rss.entries:
            yield Article(entry)




class MarkdownParse:

    pat = re.compile('\[|\]|\(|\)')

    def __init__(self, s: str):
        self.lines = s.splitlines()


    def iterparse(self):
        for i in self.lines:
            if i.startswith('['):
                source_name, xml_url = self.pat.split(i)[1::2]
            elif i:
                tags = i.split()
            else:
                yield source_name, xml_url, tags



def get_articles():
    """

    :return: (title, content, source_name, art_link, tags)
    """
    with open('crawl/RSS') as f:
        rss_string = f.read()

    markdownparse = MarkdownParse(rss_string)
    for source_name, xml_url, tags in markdownparse.iterparse():
        rss_content = RssContentGet(xml_url)
        for art in rss_content.articles:
            yield art.title, art.content, source_name, art.link, tags


def update_xml_database():
    with open('crawl/RSS') as f:
        rss_string = f.read()

    markdownparse = MarkdownParse(rss_string)
    for source_name, xml_url, tags in markdownparse.iterparse():
        xml, created = models.Xml.objects.get_or_create(name=source_name, xml_url=xml_url)
        if not created:
            xml.save()
        for tag in tags:
            tag, created = models.TemTag.objects.get_or_create(label=tag)
            if not created:
                tag.save()
            xml.tags.add(tag)

def update_article_database():
    xml_queries = models.Xml.objects.all()
    for xml in xml_queries:

        print(xml.xml_url,'..........','start')

        rss_content = RssContentGet(xml.xml_url)
        for receive_art in rss_content.articles:
            article, created = models.TemArticle.objects.get_or_create(headline=receive_art.title,
                                                              content=receive_art.content,
                                                              source_name=xml.name,
                                                              link=receive_art.link,
                                                              )
            if not created:
                article.save()

            for tag in xml.tags.all():
                article.tags.add(tag)

        print(xml.xml_url,'..........','ok')




if __name__ == '__main__':
    # rc=RssCollect('Subscriptions.opml')
    # for rss_info in rc.result['Blog']:
    #
    #     r=RssContentGet(rss_info['url'])
    #     with open('text.html','a') as f:
    #         for article in r.articles:
    #             tt = '标题: ' + article.title
    #             source = '来源a ' + article.link
    #             f.write(tt)
    #             f.write(source)
    #             f.write(article.content)

    pass

