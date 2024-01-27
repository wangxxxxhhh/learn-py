from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
f = open('C:/pyfile/1960-2019全球GDP数据.csv', 'r', encoding="GB2312")
lines = f.readlines()
lines.pop(0)
data_dict = {}
for line in lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])


sorted_years_list = sorted(data_dict.keys())
timeline = Timeline({"theme": ThemeType.LIGHT})
for year in sorted_years_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][0:8]
    countrys = []
    gdps = []
    for country_gdp in year_data:
        countrys.append(country_gdp[0])
        gdps.append(country_gdp[1] / 100000000)
    bar = Bar()
    countrys.reverse()
    gdps.reverse()
    bar.set_global_opts(title_opts=TitleOpts(title=f"{year}年全球前8 GDP国家"))
    bar.add_xaxis(countrys)
    bar.add_yaxis("GDP(亿)", gdps, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    timeline.add(bar, str(year))


timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

timeline.render("1960-2019动态gdp柱状图.html")
f.close()
