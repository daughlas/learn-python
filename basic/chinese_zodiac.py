chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

for year in range(2000, 2018):
    print('%s 年的生肖是 %s' %(year, chinese_zodiac[year % 12]))
