#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests


URL_IP = "http://ip.taobao.com/service/getIpInfo2.php"

#构建带有参数的请求：
def use_params_requests(ip):
    #构建参数
    params = {'ip':ip}
    #发送请求   类似  URL_IP？params
    response = requests.post(URL_IP, params=params)
    
#     #处理响应
#     print '>>>>>Response Headers:'
#     print response.headers
#     print '>>>>>Status code:'
#     print response.status_code
#     print response.reason
#     #reason解释为什么是200
#     print '>>>>>Response Body:'
    return response.json()["data"]["city"]+"=="+response.json()["data"]["isp"]
      
    
    
if __name__ == '__main__':
    print  use_params_requests('127.0.0.1') 