from pyecharts import Map
from pyecharts import Page
from pyecharts import Bar

provinces = {'北京':84, '江苏':26, '上海':35, '广东':36, '陕西':16,
                         '湖北':39, '辽宁':17, '海南':4, '四川':31, '浙江':33, '江西':5,
                         '湖南':27, '河北':3, '山西':6, '安徽': 6, '山东':11,
                         '香港':4, '甘肃':2, '天津':30, '广西':2, '河南':7, '云南':3,
                         '黑龙江':4, '重庆':11, '吉林':7, '宁夏':1}
provice=list(provinces.keys())
value=list(provinces.values())


page = Page()

map = Map("地图", title_text_size=30)
map.add("中国大学发文分布", provice, value, visual_range=[0, 50], maptype='china', is_visualmap=True,
    visual_text_color='#000', is_label_show=True, label_text_size=20, label_formatter='{b}:{c}', legend_text_size=22)
page.add(map)

map1 = Map("地图", title_text_size=30)
map1.add("国外大学发文分布", ['United Kingdom', 'United States', 'German', 'Italy', 'Russia', 'Netherland'], [2, 6, 3, 1, 1, 1], visual_range=[0, 6],
         maptype="world", is_visualmap=True, visual_text_color='#021', label_text_size=20, label_formatter='{b}:{c}', legend_text_size=22)
page.add(map1)

bar = Bar("统计图", title_text_size=30)
bar.add("机构发文信息（降序排列）", ['中国科学院','中国社科院','中国人民银行','中国农业银行','其他机构（共43篇）'], [23,10,8,5,1],
        is_stack=True, xaxis_interval=0, legend_text_size=22)
page.add(bar)

page.render('map.html')
