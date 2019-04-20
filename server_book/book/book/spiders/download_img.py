# -*- coding: utf-8 -*-
import pymysql,requests

def main():
    connect = pymysql.connect(
        host='47.93.37.167',
        db='book',
        user='root',
        passwd='root',
        charset='utf8mb4',
        use_unicode=True,
        cursorclass=pymysql.cursors.DictCursor,
    )
    cousor=connect.cursor()
    status=86853
    limit=200
    while status <98400:
        sql="""select book_img,book_img_md5 from book_name_jianjie_
              mulu_url limit {},{}
            """.format(status,limit)
        cousor.execute(sql)
        datas=cousor.fetchall()
        for data in datas:

            print(data['book_img'])
            response = requests.post(data['book_img'].
                        replace('http://www.lwxslwxs.com',''))

            with open(r'/book/book/book/spiders/url/{}.png'.
                        format(data['book_img_md5']),'ab') as f:

                f.write(response.content)
        status+=limit
if __name__ == '__main__':
    main()
