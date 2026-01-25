# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 法语加艺术
french_art_set=set()
french_art_set=french_set.intersection(art_set)
print(f" 选了法语和艺术的同学是{french_art_set}")
#    french_art_set=french_set&art_set
set_0 = french_art_set.intersection(basketball_set)
set_four=set_0.intersection(football_set)
print(f"四个都选了的同学是{set_four}")
# set_four=football_set &basketball_set&french_set&are_set
b_nof_set=football_set.difference(basketball_set)
print(f"选了足球没选篮球的同学是{b_nof_set}")
# b_nof_set = football_set - basketball_set


# 每个学生的选课数量
print(f"选了四个课程的是{set_four}")
# all_set = football_set.union(basketball_set).union(french_set).union(art_set)
all_set = football_set | basketball_set | french_set | art_set
print(f"学生的名单是{all_set}")
# 列表可重复
all_list=[*football_set ,* basketball_set ,* french_set ,*art_set]

# 统计次数
for s in all_list:
    print(f"{s}选修了{all_list.count(s)}门课程")