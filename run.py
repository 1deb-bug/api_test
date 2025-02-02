import os

import pytest
import allure
if __name__ == '__main__':

    pytest.main(["-sv","./testcases/test_store.py",'--alluredir','./report/json_report','--clean-alluredir'])
    os.system('allure generate ./report/json_report -o ./report/html_report --clean')





