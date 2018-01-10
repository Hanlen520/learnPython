#!/user/bin/env python
# -*- coding:utf-8 -*-

import requests
import getToken
import unittest
from config import *

class UploadUserInfo(unittest.TestCase):
    ##初始化工作
    def setUp(self):
        self.token = getToken.getToken()

    # 通讯录上传
    def test_putUserAddressBook(self):
        url = URL + '/caifu/userAddressBook/putUserAddressBook'
        contacts = [{"name": "OPPO官方客服", "phone": "4001666888"}, {"name": "自己", "phone": "13572489850"},
         {"name": "三顾冒菜", "phone": "18092051314"}, {"name": "孙力", "phone": "8617730600729"},
         # {"name": "盛伟1", "phone": "17089602464"}, {"name": "lwld隔壁", "phone": "18691082172"},
         # {"name": "郑小红健", "phone": "8615109226928"}, {"name": "饺子馆", "phone": "029,88262120"},
         # {"name": "刘晨", "phone": "8618292825591"}, {"name": "张静媛招商", "phone": "15891440252"},
         # {"name": "钉钉免费电话", "phone": "057188157855,4001696188,4000966288,4008287660"},
         # {"name": "赵亚光", "phone": "13679277905"}, {"name": "李娜", "phone": "15029574201"},
         # {"name": "张聚合", "phone": "18202944180"}, {"name": "陈彬彬", "phone": "13759962993"},
         # {"name": "高千里", "phone": "15929963730"}, {"name": "王远", "phone": "15771977731"},
         # {"name": "长城宽带", "phone": "18629421205"}, {"name": "王亚路", "phone": "13379226031"},
         # {"name": "董宁", "phone": "13227886879"}, {"name": "卞峰峰", "phone": "13032966519"},
         # {"name": "盛伟置业", "phone": "02962550317"}, {"name": "王", "phone": "18192692314"},
         # {"name": "妈", "phone": "13991551597"}, {"name": "胡少隐2", "phone": "18192897196,18729329877"},
         # {"name": "中软向甜HR", "phone": "18189251951"}, {"name": "明德门派", "phone": "02985410027"},
         # {"name": "张元珍", "phone": "15202433789"}, {"name": "刘先梅", "phone": "15829720602"},
         # {"name": "崔征", "phone": "18629379527"}, {"name": "中软刘婷助理", "phone": "89633905"},
         # {"name": "中软任翔PM", "phone": "18192627526"}, {"name": "林丹", "phone": "13892897969"},
         # {"name": "中软刘波PM", "phone": "18092311886"}, {"name": "任翔", "phone": "18192627526"},
         # {"name": "自己电信", "phone": "18192496382"}, {"name": "中软龙白彦组长", "phone": "18691955878"},
         # {"name": "中软卓兴UI", "phone": "18629408987"}, {"name": "中软蕾蕾", "phone": "13519121150"},
         # {"name": "巴士6593师傅", "phone": "15619253359"}, {"name": "賈", "phone": "13720529421"},
         # {"name": "徐xx", "phone": "13571496627"}, {"name": "马房东", "phone": "13909290085"},
         # {"name": "胡永居主业", "phone": "13772116929"}, {"name": "搬家公司", "phone": "88248888"},
         # {"name": "高电信", "phone": "18009183803"}, {"name": "相鹏飞", "phone": "18091883928"},
         # {"name": "京东快递", "phone": "02968829359"}, {"name": "papa", "phone": "13571449991"},
         # {"name": "中软马慧琴", "phone": "15991737693"}, {"name": "张空调安装", "phone": "15029068207"},
         # {"name": "瑞恩1", "phone": "02989561328"}, {"name": "瑞恩2", "phone": "02989183895"},
         # {"name": "小潇", "phone": "13572490791"}, {"name": "吴租", "phone": "18267999694"},
         # {"name": "链川刘瑞兰", "phone": "15995438286"}, {"name": "链川司小玲", "phone": "18602997967"},
         {"name": "物流", "phone": "057187750556"}, {"name": "汪", "phone": "18668120572"}]
        data = {
            'contacts':contacts,
            'token': self.token
        }
        response = requests.post(url=url, data=data)
        self.assertEqual(response.status_code, 200, 'putUserAddressBook OK')
        print u"通讯录上传:", response.content

    # 退出清理工作
    def tearDown(self):
        pass