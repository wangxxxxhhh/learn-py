import json
from pyecharts.charts import Line
from pyecharts.options import LabelOpts
f = open("C:/pyfile/美国.txt", "r", encoding="UTF-8")
f_data = f.read()
f_data = f_data.replace("jsonp_1629344292311_69436(", " ")
f_data = f_data[:-2]
f_dict = json.loads(f_data)
us_x = f_dict['data'][0]['trend']['updateDate']
us_yaxis = f_dict['data'][0]['trend']['list'][0]['data']
f__india = open("C:/pyfile/印度.txt", "r", encoding="UTF-8")
f_india = f__india.read()
f_india_data = f_india.replace("jsonp_1629350745930_63180(", ' ')
f_india_data = f_india_data[:-2]
f_india_dict = json.loads(f_india_data)
india_yaxis = f_india_dict['data'][0]['trend']['list'][0]['data']
f__Japan = open("C:/pyfile/日本.txt", "r", encoding="UTF-8")
f_Japan = f__Japan.read()
f_Japan_data = f_Japan.replace("jsonp_1629350871167_29498(", ' ')
f_Japan_data = f_Japan_data[:-2]
f_Japan_dict = json.loads(f_Japan_data)
Japan_yaxis = f_Japan_dict['data'][0]['trend']['list'][0]['data']
line = Line()
line.add_xaxis(us_x)
line.add_yaxis("美国确诊人数", us_yaxis, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", india_yaxis, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", Japan_yaxis, label_opts=LabelOpts(is_show=False))
line.render()
f.close()
f__Japan.close()
f__india.close()

