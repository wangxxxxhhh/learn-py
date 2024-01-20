from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()
data = [
    ('北京市', 11),
    ('上海市', 22),
    ('广东省', 33),
    ('河南省', 44)]
map.add('地图', data, 'china')
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#e8c726"},
            {"min": 10, "max": 19, "label": "10-19", "color": "#e89526"},
            {"min": 20, "max": 29, "label": "20-29", "color": "#e86826"},
            {"min": 30, "max": 39, "label": "30-39", "color": "#e84226"},
            {"min": 40, "max": 49, "label": "40-49", "color": "#e8262d"},
        ]
    )
)
map.render()
