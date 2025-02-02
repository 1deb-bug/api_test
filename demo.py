
from selenium import  webdriver




class A:



        driver = webdriver.Chrome()





class  B(A):

    def a(self):
        self.driver.get('http://www.baidu.com')


class C(A):
    def c(self):
        self.driver.get('http://www.baidu.com')


b=B()
b.a()
c=C()
c.c()

