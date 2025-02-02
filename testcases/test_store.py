import logging

import allure
import pytest
import requests
import pprint

from utils.allure_ini import allure_init
from utils.analyse_data import ana_data
from utils.asserts import http_assert, jdbc_assert
from utils.excel_uitl import read_excel
from utils.extractor import json_extractor, jdbc_extractor
from  jinja2 import Template

from utils.send_request import send_http_request


class TestStore:

    #读取excel测试用例
    data=read_excel()
    all={}
    @pytest.mark.parametrize("case",data)
    def test_store(self,case):
        all =self.all
        #对提取的数据进行模块渲染
        case=eval(Template(str(case)).render(all))

        #初始化allure
        allure_init(case)

        logging.info(f"用户ID:{case['id']} 模块:{case['feature']} 场景:{case['story']} 标题:{case['title']}")
        #解析excel的测试数据
        request_data=ana_data(case)



        # 发送request请求
        res=send_http_request(**request_data)

        #处理http响应断言
        http_assert(case,res)


        #处理数据库断言
        jdbc_assert(case)

        #处理http响应提取
        json_extractor(case,res,all)

        #处理数据库提取
        jdbc_extractor(case,all)


