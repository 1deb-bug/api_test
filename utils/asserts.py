import logging

import allure
import jsonpath
import  time
from utils.send_request import send_jdbc_request

@allure.step("3.http响应断言")
def http_assert(case,res):
    if case['check']:
        result=jsonpath.jsonpath(res.json(), case['check'])[0]
        assert result == case['expected']

        logging.info(f"3.http响应结果断言，预期结果 {case['expected']} ==实际结果{result}")
    else:
        assert case['expected'] in res.text
        logging.info(f"3.http响应结果断言，预期结果 {case['expected']} ==实际结果{res.text}")




def jdbc_assert(case):
    if case['sql_check']  and case['sql_expected']:
        assert send_jdbc_request(case['sql_check']) == case['sql_expected']



