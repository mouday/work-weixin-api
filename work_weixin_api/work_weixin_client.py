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

            self.cache.set(cache_key, token, expire=self.cache_expire)

        return token

    def user_simplelist(self, department_id, fetch_child=None, **kwargs):
        res = super().user_simplelist(department_id=department_id, fetch_child=fetch_child)
        return res['userlist']
