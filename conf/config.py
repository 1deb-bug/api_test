import pathlib

# excel测试用例数据路径以及表配置

EXCEL_FILE=pathlib.Path(__file__).parents[1].resolve()/ 'data'/'商城测试用例.xlsx'


SHEET='Sheet1'

#服务器以及端口配置

BASE_URL='http://192.168.10.131:8888/api/private/v1'


#数据库配置

DB_HOST='192.168.10.131'
DB_PORT=3306
DB_DATABASE='mydb'
DB_USER='root'
DB_password='123456'
