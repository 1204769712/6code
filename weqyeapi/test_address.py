from weqyeapi.address import Address


class TestAddress():
    def setup(self):
        self.address = Address()
        self.userid_data = {"userid":"zhangsan001"}
        self.create_member_data = {"userid": self.userid_data.get("userid"),"name": "张三hello","mobile": "+86 13814300000",'department': [1]}

    def test_create_member(self):
        self.address.delete_member(self.userid_data)
        r = self.address.create_member(self.create_member_data)
        assert r.get("errmsg") == "created"
        r = self.address.get_member_info(self.userid_data)
        self.address.delete_member(self.userid_data)
        assert r.get("name") == self.create_member_data.get("name")

    def test_get_member_info(self):
        self.address.create_member(self.create_member_data)
        r = self.address.get_member_info(self.userid_data)
        assert r.get("errmsg") == "ok"
        assert r.get("name") == self.create_member_data.get("name")

    def test_update_member(self):
        self.address.delete_member(self.userid_data)
        self.address.create_member(self.create_member_data)
        new_name = self.create_member_data.get("name") + "tmp"
        self.update_member_data = self.create_member_data.update({"name":new_name})
        r =self.address.update_member(self.create_member_data)
        assert r.get("errmsg") == "updated"
        r = self.address.get_member_info(self.userid_data)
        assert r.get("name") == new_name

    def test_delete_member(self):
        self.address.create_member(self.create_member_data)
        r = self.address.delete_member(self.userid_data)
        assert r.get("errmsg") == "deleted"
        r = self.address.get_member_info(self.userid_data)
        assert r.get("errcode") == 60111




