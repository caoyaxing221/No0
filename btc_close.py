import json
import time
import pygal
import math
from itertools import groupby 
import datetime
with open('btc_2000.json') as file:
    btc_data = json.load(file)
    # print(btc_data)
dates = []
closes = []
months = []
weeks = []
weekdays = []
for btc_dict in btc_data['data']:
    """{'id': 1609084800, 'open': 27360.51, 'close': 27154.03, 'low': 25838.46, 'high': 27522.01, 'amount': 39669.32112657491, 'vol': 1066035639.1061714, 'count': 1335225}"""
    # print(btc_dict)
    timeStamp = btc_dict['id']
    timeArray = time.localtime(timeStamp)
    date = time.strftime('%Y-%m-%d', timeArray)
    close = btc_dict['close']
    month = timeArray.tm_mon
    week = time.strftime("%W",timeArray)
    weekday = time.strftime('%w',timeArray)
    print(date,close,month,int(week),weekday)
    dates.append(date)
    closes.append(close)
    months.append(month)
    weeks.append(int(week))
    weekdays.append(weekday)
dates.reverse()
closes.reverse()
months.reverse()
weeks.reverse()
weekdays.reverse()
line_chart = pygal.Line(x_label_rotation = 20,show_minor_x_labels = False)#x 轴角度 不显示x轴最小刻度
line_chart.title = '收盘价($)'
line_chart.x_labels = dates
N = 150 #x轴坐标每20天显示一次
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价',closes)
line_chart.render_to_file('收盘价折线图($).svg')
##对数变换
line_chart = pygal.Line(x_label_rotation = 20,show_minor_x_labels = False)#x 轴角度 不显示x轴最小刻度
line_chart.title = '收盘价对数变换($)'
line_chart.x_labels = dates
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in closes]
line_chart.add('log收盘价',close_log)
line_chart.render_to_file('收盘价对数变换折线图($).svg')
def draw_line(x_data,y_data,title,y_legend):
    """需要将数据按月份、周数、周几分组，再计算每组的均值"""
    xy_map = []
    #将x轴与y轴的数据合并、排序，再用函数groupby分组
    for x,y in groupby (sorted(zip(x_data,y_data)),key = lambda _:_[0]):
        y_list = [v for _,v in y]
        #分组之后，求出每组的均值，存储到xy_map变量中
        xy_map.append([x,sum(y_list)/len(y_list)])

    x_unique,y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart
idx_month = dates.index('2020-12-01')
idx2_month = dates.index('2020-01-01')
line_chart_month = draw_line(months[idx2_month:idx_month],closes[idx2_month:idx_month],'收盘价月日均值($)','月日均值')
idx_week = dates.index('2020-12-27')
idx_week2 = dates.index('2020-01-06')
line_chart_week = draw_line(weeks[idx_week2:idx_week],closes[idx_week2:idx_week],'收盘价周日均值($)','周日均值')
idx_week2 = dates.index('2020-01-05')
weekdays_int = [ int(w) for w in weekdays[idx_week2:idx_week]]
line_chart_weekday = draw_line(weekdays_int,closes[idx_week2:idx_week],'收盘价星期均值($)','星期均值')
line_chart_weekday.x_labels = ['周日','周一','周二','周三','周四','周五','周六']
line_chart_weekday.render_to_file('收盘价星期均值($).svg')

with open('收盘价Dashboard.html','w',encoding = 'utf-8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta charset = "utf-8"></head><body>\n')
    for svg in ['收盘价折线图($).svg','收盘价对数变换折线图($).svg','收盘价月日均值($).svg','收盘价周日均值($).svg','收盘价星期均值($).svg']:
        html_file.write('<object type ="image/svg+xml" data = "{0}" height = 500></object>\n'.format(svg))
    html_file.write('</body></html>')



