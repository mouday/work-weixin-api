# -*- coding: utf-8 -*-

from work_weixin_api import WorkWeixinClient

from environs import Env

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


if __name__ == '__main__':
    client = CustomWorkWeixinClient()

    # print(client.gettoken())

    print(client.user_simplelist(department_id=1))

    print(client.message_send(
        agentid=client.genie_helper_agent_id,
        msgtype="text",
        msgdata={'content': 'hi'}, touser="PengShiYu"
    ))
