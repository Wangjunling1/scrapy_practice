import urllib.request,os,pymysql
from bs4 import BeautifulSoup

def xieru(data):
    db=pymysql.connect('127.0.0.1','root','root','sql1')
    cursor=db.cursor()
    biao='create table if not exists tongcheng(id int primary key auto_increment,title text,detail text,price text,img text)'
    cursor.execute(biao)
    db.commit()
    for i in data:
        suju='insert into tongcheng values(0,"%s","%s","%s","%s")'%(i[0],i[1],i[2],i[3])
        try:
            cursor.execute(suju)
            db.commit()
        except:
            db.rollback()
    db.close()

def get(url,path):
    #获取网址
    html_str=urllib.request.urlopen(url)
    #将网址变为BeautifulSoup格式
    bsoup=BeautifulSoup(html_str,'html.parser')
    #求出网页内需要获取的部分的头部（以列表的格式）
    datas =bsoup.find_all('li',{'class':"clearfix car_list_less ac_item"})
    #不要第一个
    datas.pop(0)
    # print(datas[0])
    a=0
    list1=[]
    for i in datas:
        a+=1
        if a<9:
            img = i.find('div', {'class': "col col1"}).find('a', {'class': 'ac_linkurl'}).find('img').get('src')
        else:
            img = i.find('div', {'class': "col col1"}).find('a', {'class': 'ac_linkurl'}).find('img').get('ref')
        title = i.find('div', {'class': "col col1"}).find('a', {'class': 'ac_linkurl'}).find('img').get('alt')

        detail = i.find('div',{'class':'col col2'}).find('div',{'class':"info_param"}).get_text('spen').strip('\n').replace('spen','')
        price = i.find('div', {'class': 'col col3'}).find('h3').get_text()

        #将图片下载
        # file_path=os.path.join(path,str(a)+'.jpg')
        # urllib.request.urlretrieve(img,file_path)
        list1.append([title,detail,price,img])
        print(list1)
    xieru(list1)

if __name__ == '__main__':
    url='http://dg.58.com/ershouche/pve_4917_1/'
    path='D:\\学习资料\\py\\项目\\练习\\img58'
    get(url,path)
    'http://pic5.58cdn.com.cn/p1/small/n_v2cfea46597bf84a94a87d0496db6f7751.jpg?w=200&h=150&crop=1'