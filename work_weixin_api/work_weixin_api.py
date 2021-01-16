# -*- coding: utf-8 -*-

from clask import Clask


class WorkWeixinApi(object):
    """企业微信 API"""

    BASE_URL = 'https://qyapi.weixin.qq.com/cgi-bin'

    api = Clask(base_url=BASE_URL)

    def __init__(self):
        self.api.before_request(self._before_request)
        self.api.after_request(self._after_request)

    def _before_request(self, **kwargs):
        return kwargs

    def _after_request(self, response):
        return response.json()

    @api.get('/gettoken')
    def gettoken(self, corpid=None, corpsecret=None):
        """
        获取access_token
        https://open.work.weixin.qq.com/api/doc/90000/90135/91039

        corpid	    是	企业ID，获取方式参考：术语说明-corpid
        corpsecret	是	应用的凭证密钥，获取方式参考：术语说明-secret

        """
        return {
            'query': {
                'corpid': corpid,
                'corpsecret': corpsecret
            }
        }

    @api.get('/user/simplelist')
    def user_simplelist(self, department_id,
                        fetch_child=None,
                        access_token=None):
        """
        获取部门成员

        department_id	是	获取的部门id
        fetch_child	    否	是否递归获取子部门下面的成员：1-递归获取，0-只获取本部门
        access_token	是	调用接口凭证

        """
        return {
            'query': {
                'access_token': access_token,
                'department_id': department_id,
                'fetch_child': fetch_child
            }
        }

    #####################################################
    # 消息推送
    #####################################################

    @api.post('/appchat/create')
    def appchat_create(self, userlist,
                       name=None,
                       owner=None,
                       chatid=None,
                       access_token=None):
        """
        创建群聊会话
        https://open.work.weixin.qq.com/api/doc/90000/90135/90245

        access_token	是	调用接口凭证
        userlist	    是	群成员id列表。至少2人，至多2000人
        name	        否	群聊名，最多50个utf8字符，超过将截断
        owner	        否	指定群主的id。如果不指定，系统会随机从userlist中选一人作为群主
        chatid	        否	群聊的唯一标志，不能与已有的群重复；字符串类型，最长32个字符。只允许字符0-9及字母a-zA-Z。如果不填，系统会随机生成群id

        """
        return {
            'query': {
                'access_token': access_token
            },
            'json': {
                "name": name,
                "owner": owner,
                "userlist": userlist,
                "chatid": chatid
            }
        }

    @api.post('/appchat/send')
    def appchat_send(self, chatid, msgtype, msgdata,
                     safe=None,
                     access_token=None):
        """
        应用推送消息
        https://open.work.weixin.qq.com/api/doc/90000/90135/90248

        chatid	        是	群聊id

        msgtype	        是	消息类型:
            文本消息     text
            图片消息     image
            语音消息     voice
            视频消息     video
            文件消息     file
            文本卡片     textcard
            图文消息     news
            图文消息     mpnews
            markdown    markdown
        msgdata         是  消息体
        safe	        否	表示是否是保密消息，0表示否，1表示是，默认0
        access_token	是	调用接口凭证
        """
        return {
            'query': {
                'access_token': access_token
            },
            'json': {
                "chatid": chatid,
                "msgtype": msgtype,
                msgtype: msgdata,
                'safe': safe
            }
        }

    @api.post('/message/send')
    def message_send(self, agentid, msgtype, msgdata,
                     touser=None,
                     toparty=None,
                     totag=None,
                     safe=None,
                     enable_id_trans=None,
                     enable_duplicate_check=None,
                     duplicate_check_interval=None,
                     access_token=None):
        """
        发送应用消息
        https://open.work.weixin.qq.com/api/doc/90000/90135/90236

        agentid	是	企业应用的id
        msgtype	是	消息类型
            文本消息
            图片消息
            语音消息
            视频消息
            文件消息
            文本卡片消息
            图文消息
            图文消息（mpnews）
            markdown消息
            小程序通知消息
            任务卡片消息
        msgdata 是  消息体

        touser	否	指定接收消息的成员，成员ID列表（多个接收者用‘|’分隔，最多支持1000个）。
                    特殊情况：@all全员发送
        toparty	否	指定接收消息的部门，部门ID列表，多个接收者用‘|’分隔，最多支持100个。
                    当touser为”@all”时忽略本参数
        totag	否	指定接收消息的标签，标签ID列表，多个接收者用‘|’分隔，最多支持100个。
                    当touser为”@all”时忽略本参数

        safe	否	表示是否是保密消息，0表示可对外分享，1表示不能分享且内容显示水印，默认为0
        enable_id_trans	            否	表示是否开启id转译，0表示否，1表示是，默认0。仅第三方应用需要用到，企业自建应用可以忽略。
        enable_duplicate_check	    否	表示是否开启重复消息检查，0表示否，1表示是，默认为0
        duplicate_check_interval	否	表示是否重复消息检查的时间间隔，默认1800s，最大不超过4小时

        access_token	是	调用接口凭证
        :return: 
        """
        return {
            'query': {
                'access_token': access_token
            },
            'json': {
                "agentid": agentid,
                "msgtype": msgtype,
                msgtype: msgdata,
                'safe': safe,
                'touser': touser,
                'toparty': toparty,
                'totag': totag,
                'enable_id_trans': enable_id_trans,
                'enable_duplicate_check': enable_duplicate_check,
                'duplicate_check_interval': duplicate_check_interval
            }
        }

    @api.post('/media/upload')
    def media_upload(self, file, type, access_token=None):
        """
        上传临时素材
        https://open.work.weixin.qq.com/api/doc/90000/90135/90253

        access_token	是	调用接口凭证
        type	        是	媒体文件类型，分别有图片（image）、语音（voice）、视频（video），普通文件（file）
        file            是  file like object 大小限制  5B ~ 2MB 之间
        :return:
        """

        return {
            'query': {
                'access_token': access_token,
                'type': type
            },

            'files': {
                'file': file
            }
        }
