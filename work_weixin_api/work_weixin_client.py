# -*- coding: utf-8 -*-

from mo_cache import FileCache

from .work_weixin_api import WorkWeixinApi


class WorkWeixinClient(WorkWeixinApi):
    # 企业id
    corpid = None

    # 企业秘钥
    corpsecret = None

    # 缓存引擎
    cache_class = FileCache

    # 缓存时间：秒
    cache_expire = 7200

    # 缓存前缀
    cache_key_prefix = 'access_token'

    def __init__(self):
        super().__init__()

        self.cache = self.cache_class()

    def _before_request(self, **kwargs):

        if kwargs['url'] != '/gettoken':
            if kwargs['query'] is None:
                kwargs['query'] = {}

            if kwargs['query'].get('access_token') is None:
                kwargs['query']['access_token'] = self.gettoken()

        return kwargs

    def _get_cache_key(self):
        return self.cache_key_prefix + '.' + self.corpid

    def gettoken(self, *args):
        """对token进行缓存"""

        cache_key = self._get_cache_key()

        token = self.cache.get(cache_key)

        if not token:
            res = super().gettoken(corpid=self.corpid, corpsecret=self.corpsecret)
            token = res['access_token']

            self.cache.set(key=cache_key, value=token, expire=self.cache_expire)

        return token

    def user_simplelist(self, department_id, fetch_child=None, **kwargs):
        res = super().user_simplelist(department_id=department_id, fetch_child=fetch_child)
        return res['userlist']

    def media_upload(self, file, type, **kwargs):
        """
        :return: media_id
        """
        res = super().media_upload(file=file, type=type)
        return res['media_id']

    #####################################################
    # 发送群消息
    #####################################################
    def appchat_create(self, userlist, **kwargs):
        """
        创建群聊会话

        :param userlist: List

        :return: chatid
        """
        return super().appchat_create(userlist=userlist, **kwargs)['chatid']

    def appchat_send_text(self, chatid, content, **kwargs):
        """文本消息"""
        return super().appchat_send(
            chatid=chatid,
            msgtype='text',
            msgdata={'content': content},
            **kwargs)

    def appchat_send_image(self, chatid, media_id, **kwargs):
        """图片消息"""
        return super().appchat_send(
            chatid=chatid,
            msgtype="image",
            msgdata={'media_id': media_id},
            **kwargs)

    def appchat_send_markdown(self, chatid, content, **kwargs):
        """markdown消息"""
        return super().appchat_send(
            chatid=chatid,
            msgtype='markdown',
            msgdata={'content': content},
            **kwargs)

    #####################################################
    # 发送应用消息
    #####################################################
    def message_send_text(self, agentid, content,
                          touser=None,
                          toparty=None,
                          totag=None,
                          **kwargs
                          ):
        """文本消息"""
        return super().message_send(
            agentid=agentid,
            msgtype='text',
            msgdata={'content': content},
            touser=touser,
            toparty=toparty,
            totag=totag,
            **kwargs)

    def message_send_image(self, agentid, media_id,
                           touser=None,
                           toparty=None,
                           totag=None,
                           **kwargs
                           ):
        """图片消息"""
        return super().message_send(
            agentid=agentid,
            msgtype='image',
            msgdata={'media_id': media_id},
            touser=touser,
            toparty=toparty,
            totag=totag,
            **kwargs)

    def message_send_markdown(self, agentid, content,
                              touser=None,
                              toparty=None,
                              totag=None,
                              **kwargs
                              ):
        """markdown消息"""
        return super().message_send(
            agentid=agentid,
            msgtype='markdown',
            msgdata={'content': content},
            touser=touser,
            toparty=toparty,
            totag=totag,
            **kwargs)
