import urllib2
from bs4 import BeautifulSoup
import os.path

class WebCrawler:
    def __init__(self, url, title, file_path):
        self.url = url
        self.title = title
        self.file_path = file_path

    def diff_file(self, html):
        f = open(self.file_path, 'r')

        is_same = self.compare_title(html, f.read())
        f.close()
        return is_same

    def compare_title(self, url_html, file_html):
        url_soup = BeautifulSoup(url_html)
        file_soup = BeautifulSoup(file_html.read())

        url_title = url_soup.find(class_=self.title).text
        file_title = file_soup.find(class_=self.title).text

        if url_title == file_title:
            return True
        else:
            return False

    def save_html_to_file(self, html):
        f = open(self.file_path, 'w')
        f.write(html)
        f.close()

    def proc_chkupdate(self):
        url = urllib2.urlopen(self.url)
        html = url.read()

        if os.path.isfile(self.file_path) is False:
            self.save_html_to_file(html)
            return False

        if self.diff_file(self, html) is False:
            self.save_html_to_file(html)
            return False
        return True






