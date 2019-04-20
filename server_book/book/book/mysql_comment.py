#-*-conding:utf-8 -*-

import pymysql,os,logging,hashlib



class Mysql_connect(object):

    def __init__(self,sql_address='',sql_username='',
                 sql_password='',sql_db='',sql_port=3306):

        self.__connect=pymysql.connect(
            host=sql_address,
            db=sql_db,
            user=sql_username,
            passwd=sql_password,
            charset='utf8',
            port=sql_port,
            use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor,

        )
        self.__cursor=self.__connect.cursor()

        self.sql=''

    def Get_data(self,sql):

        self.__cursor.execute(sql)
        datas=self.__cursor.fetchall()
        return datas
    def Insert_data(self,sql):
        try:
            self.__cursor.execute(sql)
            self.__connect.commit()
        except Exception as e:
            print(e)

    def md5_key(self,arg):
        hash = hashlib.md5()
        hash.update(arg.encode("utf-8"))
        return hash.hexdigest()

# def main(status,end):
#     run = Mysql_connect()
#     # 第一
#     sql = """
#         select * from book_name_url limit {},{}
#         """.format(status,end)
#     datas = run.Get_data(sql)
#
#     for book in datas:
#
#         update = """update book_name_url set book_url_md5='{}' where book_url='{}'""".format(
#             md5_key(book['book_url']), book['book_url'])
#         run.Insert_data(update)
#         for text_url in str(book['mulu_url']).split(':::'):
#             if text_url != '':
#                 text_sql = """
#                         insert into datas_book2(`type`,`name`,`name_url`,`name_url_ma5`
#                         ,`section_url`,`srction_md5`)
#                          values ('{}','{}','{}','{}','{}','{}')
#                         """.format(book['book_type'], book['book_name'],
#                                    book['book_url'],
#                                    md5_key(book['book_url']), text_url,
#                                    md5_key(text_url))
#                 run.Insert_data(text_sql)
#     # 第二
#
# if __name__ == '__main__':
#
#     status=0
#     while status <98400:
#         print(status)
#         main(status,10)
#         status+=10
if __name__ == '__main__':
    Mysql_connect()