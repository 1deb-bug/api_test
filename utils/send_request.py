import logging

import allure
import  pymysql
import requests

from conf.config import *


#发送http请求

@allure.step("2.发送http请求")
def send_http_request(**request_data):
    res = requests.request(**request_data)
    logging.info(f"2.发送http请求，响应数据为{res.json()}")
    return  res




#发送mysql数据库请求

def send_jdbc_request(sql):

    conn=pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE,
        user=DB_USER,
        password=DB_password,
        charset='utf8'
    )

    cursor=conn.cursor()
    cursor.execute(sql)
    result=cursor.fetchone()
    cursor.close()
    conn.close()

    return  result[0]





