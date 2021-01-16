# -*- coding: utf-8 -*-

import unittest

from environs import Env

from work_weixin_api import WorkWeixinClient

env = Env()

env.read_env()


class CustomWorkWeixinClient(WorkWeixinClient):
    """
    药不能停
    该账号为注册测试使用，请勿他用
    """
    # 企业id
    corpid = env.str('corpid')

    # 秘钥
    corpsecret = env.str('corpsecret')

    # 应用id 康复小秘书
    genie_helper_agent_id = "1000002"


class TestWorkWeixinClient(unittest.TestCase):
    client = CustomWorkWeixinClient()

    chatid = 'wra6DxDAAAPFSCAc7R0OuRxjyMQOGRcg'

    media_id = '3Ax0DpzZegremWr-npOVtMhsEY6tmkwj18tdssHun2LmI8r8t-eSLqrycV7Ly9cHt'

    def test_user_simplelist(self):
        print(self.client.user_simplelist(department_id=1, fetch_child=1))

    def test_message_send_text(self):
        print(self.client.message_send_text(
            agentid=self.client.genie_helper_agent_id,
            content='hi01',
            touser="PengShiYu"
        ))

    def test_message_send_image(self):
        print(self.client.message_send_image(
            agentid=self.client.genie_helper_agent_id,
            media_id=self.media_id,
            touser="PengShiYu"
        ))

    def test_media_upload(self):
        with open('image.jpg', 'rb') as file:
            print(self.client.media_upload(file=file, type='image'))

    def test_appchat_create(self):
        # wra6DxDAAAPFSCAc7R0OuRxjyMQOGRcg
        print(self.client.appchat_create(['PengShiYu', 'PengShiYu']))

    def test_appchat_send_text(self):
        self.client.appchat_send_text(chatid=self.chatid, content='hi')

    def test_appchat_send_image(self):
        self.client.appchat_send_image(
            chatid=self.chatid,
            media_id=self.media_id)

    def test_appchat_send_markdown(self):
        self.client.appchat_send_markdown(
            chatid=self.chatid,
            content='**hi**'
        )