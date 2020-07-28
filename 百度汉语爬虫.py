#by zjs 1925879492 长安小巷
#2020-7-28 17:55:55 目前仅支持爬取古诗————之后也许会新增爬取古文成语等功能
import requests 
from lxml import etree

headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
mainURL='https://dict.baidu.com/s?wd='

Input=input('请输入查询内容：')
URL=mainURL+Input

r=requests.get(url=URL,headers=headers)
HTML=etree.HTML(r.text)

def writer_dynasty():      #爬作者朝代
    writer_dynasty_html=HTML.xpath('//*[@id="poem-detail-header"]/div[1]')
    writer_dynasty_list=[]
    for i in writer_dynasty_html:
        writer_dynasty_text=i.xpath('string(.)')
        writer_dynasty_list.append(writer_dynasty_text)
    return ''.join(writer_dynasty_list)
def poem():        #爬取古诗正文（有时可能会连译文对照一起爬）
    poemhtml=HTML.xpath('//*[@id="poem-detail-header"]/div[3]')
    poem_text_list=[]
    for i in poemhtml:
        poem_text=i.xpath('string(.)')
        poem_text_list.append(poem_text)

    return ''.join(poem_text_list)


print(writer_dynasty()+poem())