import jsonpath

from utils.send_request import send_jdbc_request


def  json_extractor(case,res,all):

    if case['jsonExData']:
        for k,v  in eval(case['jsonExData']).items() :
            key=k
            value=jsonpath.jsonpath(res.json(),v)[0]

            all[key]=value



def jdbc_extractor(case,all):
    if case['sqlExData']:
        for k, v in eval(case['sqlExData']).items():
            key = k
            value = send_jdbc_request(v)

            all[key] = value


