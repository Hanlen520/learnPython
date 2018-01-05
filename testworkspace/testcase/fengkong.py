#!/user/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb
from sshtunnel import SSHTunnelForwarder
from configData import *
import json
import xlwt

def mysql_connection():
    with SSHTunnelForwarder(
            ssh_address_or_host=('118.31.70.164', 9998),
            ssh_username='3602d0_root',
            ssh_password='Yfb111qqq',
            remote_bind_address=('rm-bp1qb3etnt3zb55oc.mysql.rds.aliyuncs.com', 3306)) as server:
        conn = MySQLdb.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                               port=server.local_bind_port,
                               user='kld',
                               passwd='Kld123456')
        cursor = conn.cursor()
        # 平均每月主叫次数
        sql1 = '''
            SELECT
                AVG(DIALING_COUNT_) AS '平均每月主叫次数',
                AVG(DIALED_COUNT_) AS '平均每月被叫次数',
                AVG(TELEPHONE_CHARGE_) AS '平均每月的话费',
                SUM(DIALING) / SUM(DIALING_COUNT_) AS '每次主叫时长',
                SUM(DIALED) / SUM(DIALED_COUNT_) AS '每次被叫时长',
                SUM(TELEPHONE_CHARGE_) / SUM(DIALING_COUNT_) AS '平均每次通话的主叫金额',
                (SUM(DIALED) / SUM(DIALED_COUNT_)) / AVG(DIALING_COUNT_) AS 'avg_beijiao',
                AVG(TELEPHONE_CHARGE_) / (SUM(DIALING) / SUM(DIALING_COUNT_)) AS 'avg_zhujiao_money'
            FROM
                (
                    SELECT
                        *
                    FROM
                        kld_caifu_wealth.operator_data_statistics_
                    WHERE
                        USER_IDENTIFIER_ IN (
                            SELECT
                                userIdentifier
                            FROM
                                kld_caifu_wealth.users
                            WHERE
                                cellphone IN ('13572489850')
                        )
                    GROUP BY
                        MONTH_
                ) a
        '''

        result = cursor.execute(sql1)
        # 打印表中的多少数据
        info1 = cursor.fetchall()
        for ii in info1:
            print '平均每月主叫次数:',ii[0]
            avgTelephoneCharge = ii[2]
            print '平均每月的话费:', ii[2]

        sql2='''
          SELECT RISK_ARGS FROM kld_risk_manage.risk_evaluation 
          WHERE USER_IDENTIFIER IN (SELECT userIdentifier FROM kld_caifu_wealth.users WHERE cellphone IN ('13572489850'));
        '''
        total = cursor.execute(sql2)
        info2 = cursor.fetchall()
        avg_info = info2[0][0]
        # for ii in info2:
        #     print ii[0]
        cursor.close()
        conn.commit()
        conn.close()
        print avg_info
        return avgTelephoneCharge,avg_info

def get_zhima(type,zhima_score):
    datas = risk_control_attribute_data.get(type)
    return getscore(datas,zhima_score)

def getscore(datas,value):
    for info in datas:
        max = info.get("max")
        min = info.get('min')
        score = info.get('score')
        if max is not None and min is not None:
            if value <= max and value > min:
                res= score
                break
        if min is None and value <= max:
            res= score
            break
        if max is None and value > min:
            res= score
            break
    return res

if __name__ == '__main__':
    results =mysql_connection()
    avgTelephoneCharge= results[0]
    avg_info = json.loads(results[1])

    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet(u"结果")
    print 'avgTelephoneCharge:', get_zhima('avgTelephoneCharge', avg_info.get('avgTelephoneCharge'))
    sheet.write(0,0,'avgTelephoneCharge')
    sheet.write(0, 1, avg_info.get('avgTelephoneCharge'))
    sheet.write(0, 2, get_zhima('avgTelephoneCharge', avg_info.get('avgTelephoneCharge')))
    print 'age:', get_zhima('age', avg_info.get('age'))
    sheet.write(1,0,'age')
    sheet.write(1, 1, avg_info.get('age'))
    sheet.write(1, 2, get_zhima('age', avg_info.get('age')))
    print 'zhimaScore:',get_zhima('zhimaScore',avg_info.get('zhimaScore'))
    sheet.write(2,0,'zhimaScore')
    sheet.write(2, 1, avg_info.get('zhimaScore'))
    sheet.write(2, 2, get_zhima('zhimaScore', avg_info.get('zhimaScore')))
    print 'validAddress:', get_zhima('validAddress', avg_info.get('validAddress'))
    sheet.write(3,0,'validAddress')
    sheet.write(3, 1, avg_info.get('validAddress'))
    sheet.write(3, 2, get_zhima('validAddress', avg_info.get('validAddress')))
    print 'addressPhoneNums:', get_zhima('addressPhoneNums', avg_info.get('addressPhoneNums'))
    sheet.write(4,0,'addressPhoneNums')
    sheet.write(4, 1, avg_info.get('addressPhoneNums'))
    sheet.write(4, 2, get_zhima('addressPhoneNums', avg_info.get('addressPhoneNums')))
    print 'addressPhoneRates:', get_zhima('addressPhoneRates', avg_info.get('addressPhoneRates'))
    sheet.write(5,0,'addressPhoneRates')
    sheet.write(5, 1, avg_info.get('addressPhoneRates'))
    sheet.write(5, 2, get_zhima('addressPhoneRates', avg_info.get('addressPhoneRates')))
    print 'networkDuration:', get_zhima('networkDuration', avg_info.get('networkDuration'))
    sheet.write(6,0,'networkDuration')
    sheet.write(6, 1, avg_info.get('networkDuration'))
    sheet.write(6, 2, get_zhima('networkDuration', avg_info.get('networkDuration')))
    print 'phoneNumMatchs:', get_zhima('phoneNumMatchs', avg_info.get('phoneNumMatchs'))
    sheet.write(7,0,'phoneNumMatchs')
    sheet.write(7, 1, avg_info.get('phoneNumMatchs'))
    sheet.write(7, 2, get_zhima('phoneNumMatchs', avg_info.get('phoneNumMatchs')))

    wbk.save('test.xls')