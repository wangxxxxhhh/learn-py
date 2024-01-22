from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
import json
with open('C:/pyfile/疫情.txt', 'r', encoding='UTF-8') as f:
    f_json = f.read()
f_dict = json.loads(f_json)
province_data = f_dict['areaTree'][0]['children']
date = []
date.append(('重庆市', 10))
date.append(('新疆维吾尔自治区', 100))
date.append(('广西壮族自治区', 1000))
date.append(('宁夏回族自治区', 10000))
date.append(('内蒙古自治区', 100000))
date.append(('西藏自治区', 9))
for province_all in province_data:
    province_name = province_all['name'] + "省"
    province_confirm = province_all['total']['confirm']
    date.append((province_name, province_confirm))
map = Map()
map.add('全国疫情地图', date, 'china')
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#3adbe9"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#e9e33a"},
            {"min": 100, "max": 499, "label": "100-499", "color": "#e9a33a"},
            {"min": 500, "max": 999, "label": "500-999", "color": "#f36516"},
            {"min": 1000, "max": 9999, "label": "1000-9999", "color": "#e9683a"},
            {"min": 10000, "max": 999999999, "label": "10000-999999999", "color": "#e93f3a"},
        ]
    )
)
map.render("全国疫情地图.html")