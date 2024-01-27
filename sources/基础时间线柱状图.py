from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType
bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "日本"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()
bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "日本"])
bar2.add_yaxis("GDP", [60, 25, 15], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()
timeline = Timeline({"theme": ThemeType.LIGHT})
timeline.add(bar1, "2022年GDP")
timeline.add(bar2, "2023年GDP")
# 设置自动播放
timeline.add_schema(
    play_interval=1000,          # 自动播放的时间间隔,单位毫秒
    is_timeline_show=True,      # 是否在自动播放的时候，显示时间线
    is_auto_play=True,          # 是否自动播放
    is_loop_play=True            # 是否循环播放
)
timeline.render("基础时间线柱状图.html")
