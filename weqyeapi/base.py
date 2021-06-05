import requests

class Base:

    def __init__(self):
        self.s = requests.Session()
        self.s.params = {"access_token": self.get_token()}

    def send(self,*args,**kwargs):
        return self.s.request(*args,**kwargs)

    def get_token(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww4a46226a29aa2532&corpsecret=N4kThJsdsL-N3wvzQTFkIB-eg--bVZAOn2HB0aoNs7g")
        return r.json()["access_token"]



















