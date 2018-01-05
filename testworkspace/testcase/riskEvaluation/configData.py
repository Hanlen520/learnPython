#!/user/bin/env python
# -*- coding:utf-8 -*-

zhima_datas = [{"max": 603.0, "score": -42.224765}, {"max": 611.0, "min": 603.0, "score": -2.294080},
         {"max": 619.0, "min": 611.0, "score": 0.892455}, {"max": 626.0, "min": 619.0, "score": 5.943337},
         {"max": 635.0, "min": 626.0, "score": 8.249970}, {"max": 645.0, "min": 635.0, "score": 12.910354},
         {"max": 656.0, "min": 645.0, "score": 15.043622}, {"max": 670.0, "min": 656.0, "score": 18.073304},
         {"max": 690.0, "min": 670.0, "score": 18.693492}, {"min": 690.0, "score": 25.577121}]

risk_control_attribute_data={
    'age':[{"max":24,"score":-0.208830},{"max":27,"min":24,"score":-0.633379},{"max":30,"min":27,"score":-0.819186},{"max":34,"min":30,"score":1.028618},{"min":34,"score":0.878414}],
    'zhimaScore':[{"max": 603.0, "score": -42.224765}, {"max": 611.0, "min": 603.0, "score": -2.294080},
         {"max": 619.0, "min": 611.0, "score": 0.892455}, {"max": 626.0, "min": 619.0, "score": 5.943337},
         {"max": 635.0, "min": 626.0, "score": 8.249970}, {"max": 645.0, "min": 635.0, "score": 12.910354},
         {"max": 656.0, "min": 645.0, "score": 15.043622}, {"max": 670.0, "min": 656.0, "score": 18.073304},
         {"max": 690.0, "min": 670.0, "score": 18.693492}, {"min": 690.0, "score": 25.577121}],
    'avgTelephoneCharge':[{"max":7420.8,"score":-5.188547},{"max":10774.917,"min":7420.8,"score":-2.791310},{"max":13598.625,"min":10774.917,"score":-0.495563},{"max":16390.875,"min":13598.625,"score":-0.338044},{"max":19505.714,"min":16390.875,"score":1.725908},{"max":23408.5,"min":19505.714,"score":0.964504},{"max":29890.0,"min":23408.5,"score":3.149227},{"min":29890.0,"score":4.207469}],
    'validAddress':[{"max":55.0,"score":0.209252},{"max":84.0,"min":55.0,"score":0.196093},
                    {"max":117.0,"min":84.0,"score":0.119287},{"max":157.0,"min":117.0,"score":0.074722},
                    {"max":211.0,"min":157.0,"score":-0.017405},{"max":290.0,"min":211.0,"score":-0.153703},
                    {"max":441.0,"min":290.0,"score":-0.171399},{"min":441.0,"score":-0.365879}],
    'addressPhoneNums':[{"max":55.0,"score":-3.635709},{"max":87.0,"min":55.0,"score":-2.607480},{"max":125.0,"min":87.0,"score":-1.331972},{"max":175.0,"min":125.0,"score":-0.920195},{"max":250.0,"min":175.0,"score":1.480256},{"max":389.0,"min":250.0,"score":2.839328},{"min":389.0,"score":5.751676}],
    'addressPhoneRates':[{"max":91.06,"score":-0.864667},{"max":94.62,"min":91.06,"score":-1.141018},{"max":96.72,"min":94.62,"score":-1.582194},{"max":98.18,"min":96.72,"score":-0.976315},{"max":99.29,"min":98.18,"score":2.188455},{"min":99.29,"score":2.937610}],
    'networkDuration':[{"max":19.0,"score":-5.100915},{"max":33.0,"min":19.0,"score":-3.374960},{"max":44.0,"min":33.0,"score":-1.508066},{"max":56.0,"min":44.0,"score":-0.277974},{"max":70.0,"min":56.0,"score":0.592050},{"max":88.0,"min":70.0,"score":2.102182},{"max":114.0,"min":88.0,"score":3.766286},{"min":114.0,"score":6.605952}],
    'phoneNumMatchs':[{"max":9.0,"score":-3.665810},{"max":12.0,"min":9.0,"score":-1.982148},{"max":13.0,"min":12.0,"score":14.689269},{"max":16.0,"min":13.0,"score":-0.617237},{"min":16.0,"score":-2.022586}]
}

select_sql_one = '''
            SELECT
                AVG(DIALING_COUNT_) AS '平均每月主叫次数',
                AVG(DIALED_COUNT_) AS '平均每月被叫次数',
                AVG(TELEPHONE_CHARGE_) AS '平均每月的话费',
                SUM(DIALING) / SUM(DIALING_COUNT_) AS '每次主叫时长',
                SUM(DIALED) / SUM(DIALED_COUNT_) AS '每次被叫时长',
                SUM(TELEPHONE_CHARGE_) / SUM(DIALING_COUNT_) AS '平均每次通话的主叫金额',
                SUM(DIALED) / SUM(DIALED_COUNT_) AS 'avg_beijiao',
                AVG(TELEPHONE_CHARGE_) / ((SUM(DIALING) / SUM(DIALING_COUNT_))*AVG(DIALING_COUNT_)) AS 'avg_zhujiao_money'
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

select_sql_two = '''
  SELECT RISK_ARGS FROM kld_risk_manage.risk_evaluation 
  WHERE USER_IDENTIFIER IN (SELECT userIdentifier FROM kld_caifu_wealth.users WHERE cellphone IN ('13572489850'));
'''
