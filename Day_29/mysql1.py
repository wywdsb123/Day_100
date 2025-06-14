"""wang

删除数据
"""
import pymysql



no=int(input("部门编号:"))

#1.创建链接 (connection)
conn = pymysql.connect(host = '127.0.0.1',port = 3306,
                       user = 'guest',password = 'Guest.618',
                       database = 'hrs' ,charset= 'utf8mb4',
                       autocommit= True)
try :
    # 2.获取游标对象(Cursor)
    with conn.cursor() as cursor:
        # 3.通过游标对象向数据库服务器发出SQL语句
        affected_rows = cursor.execute(
            'delete from `tv_dept` where `dno` = %s',(no,)
        )
        if affected_rows ==1:
            print('删除部门成功!!!')
finally:
    # 5.关闭连接释放资源
    conn.close()
    