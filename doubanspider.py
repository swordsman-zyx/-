'''
    豆瓣的爬虫豆瓣图书 Top 250书籍信息，包括书名、作者、内容简介...等
'''
import re
from urllib import request
class DoubanSpider():
    '''
    找出豆瓣top250图书的地址
    '''
    urlstart = 'https://book.douban.com/top250?start='
    boot_pattern = '<div class="pl2">([\s\S]*?)</div>'
    son_url = '<a href="([\s\S]*?)"'
    end_url = [0,25,50,75,100,125,150,175,200,225]
    label_a =[]
    def __fetch_content(self,url):
        r = request.urlopen(url)
        htmls = r.read()
        htmls = str(htmls,encoding = "UTF-8")
        return htmls

    def __analysis(self,htmls):
        html_list = re.findall(DoubanSpider.boot_pattern,htmls)
        
        for html in html_list:
            a_url = re.findall(DoubanSpider.son_url,html)
            DoubanSpider.label_a.append(a_url[0])
        

    def go(self):
        for u in DoubanSpider.end_url:
            url = DoubanSpider.urlstart+str(u)
            html = self.__fetch_content(url)
            self.__analysis(html)


class BookInformation():
    boot_pattern = '<div id="info" class="">([\s\S]*?)</div>'
    boot_content = '<div class="intro">([\s\S]*?)</div>'    
    # url = 'https://book.douban.com/subject/3259440/'
    i = 1
    def __fetch_content(self,url):
        r = request.urlopen(url)
        htmls = r.read()
        htmls = str(htmls,encoding = "UTF-8")
        return htmls

    def __analysis(self,htmls):
        boot_htmls = re.findall(BookInformation.boot_pattern,htmls) 
        word = re.findall('>([\s\S]*?)<',boot_htmls[0])
        
        ww = []
        for w in word:
            if '&nbsp;' not in w and w != '':
                
                w1 = re.findall('\S',w)
               
                if w1 != [] and w1 != [':'] and w1 !=['/']:
                    
                    w2 = ''.join([str(i) for i in w1])
                    ww.append(w2)            
        return ww

    def __bookname__(self,htmls):
        bookname = re.findall('iewed">([\s\S]*?)</span>',htmls)
        return bookname[0]
    
    def __word_content__(self,htmls): 
        content = re.findall(BookInformation.boot_content,htmls)
        p = re.findall('<p>([\s\S]*?)</p>',content[0])
        contents = ''.join([str(i) for i in p])  
        return contents

    def __print__(self,ww,contents,bookname,i):#
        BookInformation.i += 1
        print("第"+str(i)+"本书")
        print(bookname)

        for i in range(0,len(ww)):
            print(ww[i])

        print('作品简介：\n'+contents)   
        
    def go(self,label_a):#
        for url in label_a:
            if BookInformation.i == 120:
                continue
            htmls = self.__fetch_content(url)
            contents = self.__word_content__(htmls)
            ww = self.__analysis(htmls)
            bookname = self.__bookname__(htmls)
            self.__print__(ww,contents,bookname,BookInformation.i) #


spider = DoubanSpider()
spider.go()

bi = BookInformation()
bi.go(DoubanSpider.label_a)