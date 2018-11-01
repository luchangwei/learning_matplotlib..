import pygal
import json

dates,months,weeks,weekdays,closes = [],[],[],[],[]
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    closes.append(int(float(btc_dict['close'])))


line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title = '收盘价 （￥）'
line_chart.x_labels = dates
line_chart.x_labels_major = dates[::20]
line_chart.add('收盘价',closes)
line_chart.render_to_file('收盘价折线图 （￥）.svg')