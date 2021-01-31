# Work Weixin Api

![PyPI](https://img.shields.io/pypi/v/work-weixin-api.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/work-weixin-api)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/work-weixin-api)
![PyPI - License](https://img.shields.io/pypi/l/work-weixin-api)

企业微信接口封装库

目前实现了简单的发送消息功能，后序按照业务继续增加其他接口

- Github: https://github.com/mouday/work-weixin-api
- Pypi: https://pypi.org/project/work-weixin-api

## install
 
```bash
pip install work-weixin-api
```

## demo
```python
# -*- coding: utf-8 -*-

from work_weixin_api import WorkWeixinClient


class CustomWorkWeixinClient(WorkWeixinClient):
    """配置自己企业的信息"""
    # 企业id
    corpid = ""

    # 秘钥
    corpsecret = ""

    # 应用id
    agent_id = "100000"


if __name__ == '__main__':
    client = CustomWorkWeixinClient()

    print(client.user_simplelist(department_id=1))
    
    # 发送消息
    print(client.message_send_text(
        agentid=client.agent_id,
        content='hi',
        touser="PengShiYu"
    ))

```

WorkWeixinClient 缓存默认使用了mo_cache的文件缓存FileCache，可以替换redis,或内存缓存

## 说明

核心类继承关系：

```python
class WorkWeixinApi(object):
    """
    实现了最基础的企业微信接口函数
    """
    
class WorkWeixinClient(WorkWeixinApi):
    """
    扩展了基本的接口函数
    1、对access_token 进行了缓存
    2、简化了接口调用操作
    """

```
