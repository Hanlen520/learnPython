#!/user/bin/env python
# -*- coding:utf-8 -*-
import xlsxwriter
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    workbook = xlsxwriter.Workbook('report.xlsx')
    worksheet = workbook.add_worksheet('测试')
    worksheet2 = workbook.add_worksheet("测试接口")

    workbook.close()