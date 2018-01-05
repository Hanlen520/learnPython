#!/user/bin/env python
# -*- coding:utf-8 -*-
import xlwt

def write_excel():
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet(u"结果")
    sheet.write(0, 1, 'test text')  # 第0行第一列写入内容

    wbk.save('test.xls')
if __name__ == '__main__':
    write_excel()