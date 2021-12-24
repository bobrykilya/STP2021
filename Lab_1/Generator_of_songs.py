# main_file
from Classes.Crawler import Crawler
from Classes.Generator import Generator
from Classes.Saver import Saver

dir, verse_size_1, verse_size_2, chorus_size = map(str, input('Введите название папки для поиска песен, \
размеры каждого из двух куплетов и припева через пробел: ').split())

ex_crawl = Crawler(dir)
ex_gen = Generator(verse_size_1, verse_size_2, chorus_size)
Saver().saver_function(ex_gen.lyrics_generation(ex_crawl.crawl_function()))














