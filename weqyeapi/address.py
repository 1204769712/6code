from weqyeapi.base import Base


class Address(Base):

    def create_member(self,json_data):
        create_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        r = self.send("POST",create_member_url,json = json_data)
        return r.json()

    def get_member_info(self,params):
        get_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        r = self.send("GET",get_member_url,params=params)
        return r.json()

    def update_member(self,json_data):
        update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        r = self.send("POST",url=update_member_url, json=json_data)
        return r.json()

    def delete_member(self,params):
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        r = self.send("GET",delete_url,params=params)
        return r.json()




