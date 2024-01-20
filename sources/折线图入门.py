from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
line = Line()
line.add_xaxis(["王向辉", "李坤"])
line.add_yaxis("身高", [185, 150])
line.set_global_opts(
    title_opts=TitleOpts(title = "身高比对", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
line.render()