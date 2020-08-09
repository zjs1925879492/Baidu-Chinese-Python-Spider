#by 长安小巷 zjs 1925879492@qq.com

import requests 
from lxml import etree

headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
mainURL='https://dict.baidu.com/s?wd='

print('1.古诗\n2.成语\n其他正在加紧研发中')
choice=int(input('请输入查询类别：'))
Input=input('请输入查询内容：')

URL=mainURL+Input
r=requests.get(url=URL,headers=headers)
HTML=etree.HTML(r.text)

def poems():
    def writer_dynasty():      #爬作者朝代
        writer_dynasty_html=HTML.xpath('//*[@id="poem-detail-header"]/div[1]')
        writer_dynasty_list=[]
        for i in writer_dynasty_html:
            writer_dynasty_text=i.xpath('string(.)')
            writer_dynasty_list.append(writer_dynasty_text)
        return ''.join(writer_dynasty_list)
    def poem():        #爬取古诗正文（有时可能会连译文对照一起爬）
        poem_html=HTML.xpath('//*[@id="poem-detail-header"]/div[3]')
        poem_text_list=[]
        for i in poem_html:
            poem_text=i.xpath('string(.)')
            poem_text_list.append(poem_text)
        return ''.join(poem_text_list)
    def translation():       #爬取译文
        translation_html=HTML.xpath('//*[@id="poem-detail-translation"]/div[3]')
        translation_list=[]
        for i in translation_html:
            translation_text=i.xpath('string(.)')
            translation_list.append(translation_text)
        return ''.join(translation_list)
    def notes():        #爬取注释
        notes_html=HTML.xpath('//*[@id="poem-detail-zhushi"]/div[3]')
        notes_list=[]
        for i in notes_html:
            notes_text=i.xpath('string(.)')
            notes_list.append(notes_text)
        return ''.join(notes_list)
    def authorinfo():      #爬取作者简介
        authorinfo_html=HTML.xpath('//*[@id="poem-detail-author"]/div[3]/div/div/span')
        authorinfo_list=[]
        for i in authorinfo_html:
            authorinfo_text=i.xpath('string(.)')
            authorinfo_list.append(authorinfo_text)
        return ''.join(authorinfo_list)
    return writer_dynasty()+poem()+translation()+notes()+authorinfo()

def idioms():
    def basic_mean():
        basic_mean_html=HTML.xpath('//*[@id="basicmean-wrapper"]/div[1]/dl')
        basic_mean_list=[]
        for i in basic_mean_html:
            basic_mean_text=i.xpath('string(.)')
            basic_mean_list.append(basic_mean_text)
        return ''.join(basic_mean_list)
    def detail_mean():
        detail_mean_html=HTML.xpath('//*[@id="detailmean-wrapper"]/div[1]')
        detail_mean_list=[]
        for i in detail_mean_html:
            detail_mean_text=i.xpath('string(.)')
            detail_mean_list.append(detail_mean_text)
        return ''.join(detail_mean_list)
    def source():
        source_html=HTML.xpath('//*[@id="source-wrapper"]')
        source_list=[]
        for i in source_html:
            source_text=i.xpath('string(.)')
            source_list.append(source_text)
        return ''.join(source_list)
    def eg():
        eg_html=HTML.xpath('//*[@id="liju-wrapper"]')
        eg_list=[]
        for i in eg_html:
            eg_text=i.xpath('string(.)') 
            eg_list.append(eg_text)
        return ''.join(eg_list)
    def syn_antonym():
        syn_antonym_html=HTML.xpath('//*[@id="syn_ant_wrapper"]')
        syn_antonym_list=[]
        for i in syn_antonym_html:
            syn_antonym_text=i.xpath('string(.)')
            syn_antonym_list.append(syn_antonym_text)
        return ''.join(syn_antonym_list)
    def allusion():
        allusion_html=HTML.xpath('//*[@id="story-wrapper"]')
        allusion_list=[]
        for i in allusion_html:
            allusion_text=i.xpath('string(.)')
            allusion_list.append(allusion_text)
        return ''.join(allusion_list)
    return basic_mean()+detail_mean()+source()+eg()+syn_antonym()+allusion()

if choice==1:
    print(poems()+'\n')
if choice==2:
    print(idioms()+'\n')

input('回车退出')