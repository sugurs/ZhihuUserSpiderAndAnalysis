# !/usr/bin/python
# coding=utf-8
'''
['\ufeff_id', 'url_token', 'allow_message', 'answer_count', 'articles_count',
 'avatar_url', 'avatar_url_template', 'badge', 'business', 'columns_count',
  'educations', 'companies', 'favorite_count', 'favorited_count', 'follower_count',
  'following_columns_count', 'following_count', 'following_favlists_count', 'following_question_count', 'following_topic_count',
  'gender', 'headline', 'hosted_live_count', 'id', 'is_advertiser',
  'is_blocking', 'is_followed', 'is_following', 'is_org', 'locations',
  'name', 'participated_live_count', 'pins_count', 'question_count', 'thank_from_count',
  'thank_to_count', 'thanked_count', 'type', 'url', 'user_type',
    'vote_from_count', 'vote_to_count', 'voteup_count']
'''
import csv
from matplotlib import pyplot as plt
import json
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from scipy.misc import imread
from PIL import Image
import numpy as np
import jieba

#指定默认字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False


# 定义列表存储数据
gender = []
locations = []
name = []
follower_count = []
following_count = []
voteup_count = []
thanked_count = []
answer_count = []
question_count = []
articles_count = []
educations = []
companies = []
jobs = []
business = []

file = open('..\data.json', 'r', encoding='utf-8')
for line in file.readlines():
    dic = json.loads(line)
    # 地理位置
    if len(dic['locations']):
        locations.append(dic['locations'][0]['name'])
    # 性别
    gender.append(dic['gender'])
    # 知乎名字
    name.append(dic['name'])
    # 粉丝数
    follower_count.append(dic['follower_count'])
    # 关注他人数
    following_count.append(dic['following_count'])
    # 获得赞同数
    voteup_count.append(dic['voteup_count'])
    # 获得感谢数
    thanked_count.append(dic['thanked_count'])
    # 回答问题数
    answer_count.append(dic['answer_count'])
    # 提出问题数
    question_count.append(dic['question_count'])
    # 写文章数
    articles_count.append(dic['articles_count'])
    # 教育情况
    try:
        edu_place = dic['educations'][0]['school']['name']
    except:
        continue
    educations.append(edu_place)
    # 公司情况
    try:
        company_name = dic['employments'][0]['company']['name']
    except:
        continue
    companies.append(company_name)
    # 职业情况
    try:
        job_name = dic['employments'][0]['job']['name']
    except:
        continue
    jobs.append(job_name)
    # 行业情况
    try:
        business_name = dic['business']['name']
    except:
        continue
    business.append(business_name)

# 男女比例作图
count_male = 0
count_female = 0
count_sex_unknow = 0
for i in gender:
    if i == 1:
        count_male+=1
    elif i == 0:
        count_female+=1
    else:
        count_sex_unknow+=1
plt.figure(figsize=(6,9))
labels = [u'男性', u'女性', u'性别不详']
sizes = [count_male, count_female ,count_sex_unknow]
colors = ['red','yellowgreen','lightskyblue']
explode = (0.05,0,0)
patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
for t in l_text:
    t.set_size=(30)
for t in p_text:
    t.set_size=(20)
plt.title('男女比例分布—Top15')
plt.axis('equal')
plt.legend()
plt.savefig("sexual.jpg")
plt.show()
with open("sexual.txt", "w") as f:
    for j in range(3):
        f.write(str(labels[j]) + ' ' + str(sizes[j]) + '\n')


# 地理位置分布 作图
locations_name = []
locations_count = []
for i in range(30):
    locations_name.append(Counter(locations).most_common(30)[i][0].strip('市'))
    locations_count.append(Counter(locations).most_common(30)[i][1])
data = locations_count
labels = locations_name
plt.xticks(rotation=90)
plt.title('地理位置分布—Top30')
plt.bar(range(len(data)), data, tick_label=labels, align='center')
plt.savefig("locations.jpg")
plt.show()
with open("locations.txt", "w") as f:
    for j in range(len(labels)):
        f.write(str(labels[j]) + ' ' + str(data[j]) + '\n')

# 关注数最多
dict_name_follower_count = dict(zip(name,follower_count))
dict_name_follower_count = dict(sorted(dict_name_follower_count.items(), key=lambda d: d[1], reverse=True))
m_name = []
m_count = []
cnt = 0
for k, v in dict_name_follower_count.items():
    m_name.append(k)
    m_count.append(v)
    cnt += 1
    if cnt == 30:
        break
data = m_count
labels = m_name
plt.title('关注数—Top30')
plt.xticks(rotation=90)
plt.bar(range(len(data)), data, tick_label=labels, align='center')
plt.savefig("follower_count.jpg")
plt.show()
with open("follower_count.txt", "w") as f:
    for j in range(len(labels)):
        f.write(str(labels[j]) + ' ' + str(data[j]) + '\n')

# 关注他人数最多
dict_name_following_count = dict(zip(name,following_count))
dict_name_following_count = dict(sorted(dict_name_following_count.items(), key=lambda d: d[1], reverse=True))
m_name = []
m_count = []
cnt = 0
for k, v in dict_name_following_count.items():
    m_name.append(k)
    m_count.append(v)
    cnt += 1
    if cnt == 30:
        break
data = m_count
labels = m_name
plt.title('关注他人数—Top30')
plt.xticks(rotation=90)
plt.bar(range(len(data)), data, tick_label=labels, align='center')
plt.savefig("following_count.jpg")
plt.show()
with open("following_count.txt", "w") as f:
    for j in range(len(labels)):
        f.write(str(labels[j]) + ' ' + str(data[j]) + '\n')

# 获得赞同数
voteup_count_count = dict(zip(name,voteup_count))
voteup_count_count = dict(sorted(voteup_count_count.items(), key=lambda d: d[1], reverse=True))
m_name = []
m_count = []
cnt = 0
for k, v in voteup_count_count.items():
    m_name.append(k)
    m_count.append(v)
    cnt += 1
    if cnt == 30:
        break
data = m_count
labels = m_name
plt.title('获得赞同数—Top30')
plt.xticks(rotation=90)
plt.bar(range(len(data)), data, tick_label=labels, align='center')
plt.savefig("voteup_count.jpg")
plt.show()
with open("voteup_count.txt", "w") as f:
    for j in range(len(labels)):
        f.write(str(labels[j]) + ' ' + str(data[j]) + '\n')

# 获得感谢数
thanked_count_count = dict(zip(name,thanked_count))
thanked_count_count = dict(sorted(thanked_count_count.items(), key=lambda d: d[1], reverse=True))
m_name = []
m_count = []
cnt = 0
for k, v in thanked_count_count.items():
    m_name.append(k)
    m_count.append(v)
    cnt += 1
    if cnt == 30:
        break
data = m_count
labels = m_name
plt.title('获得感谢数—Top30')
plt.xticks(rotation=90)
plt.bar(range(len(data)), data, tick_label=labels, align='center')
plt.savefig("thanked_count.jpg")
plt.show()
with open("thanked_count.txt", "w") as f:
    for j in range(len(labels)):
        f.write(str(labels[j]) + ' ' + str(data[j]) + '\n')

# 回答问题数
answer_count_count = dict(zip(name,answer_count))
answer_count_count = dict(sorted(answer_count_count.items(), key=lambda d: d[1], reverse=True))
m_name = []
m_count = []
cnt = 0
for k, v in answer_count_count.items():
    m_name.append(k)
    m_count.append(v)
    cnt += 1
    if cnt == 30:
        break
data = m_count
labels = m_name
plt.title('回答问题数—Top30')
plt.xticks(rotation=90)
plt.bar(range(len(data)), data, tick_label=labels, align='center')
plt.savefig("answer_count.jpg")
plt.show()
with open("answer_count.txt", "w") as f:
    for j in range(len(labels)):
        f.write(str(labels[j]) + ' ' + str(data[j]) + '\n')

# 提出问题数
question_count_count = dict(zip(name,question_count))
question_count_count = dict(sorted(question_count_count.items(), key=lambda d: d[1], reverse=True))
m_name = []
m_count = []
cnt = 0
for k, v in question_count_count.items():
    m_name.append(k)
    m_count.append(v)
    cnt += 1
    if cnt == 30:
        break
data = m_count
labels = m_name
plt.title('提出问题数—Top30')
plt.xticks(rotation=90)
plt.bar(range(len(data)), data, tick_label=labels, align='center')
plt.savefig("question_count.jpg")
plt.show()
with open("question_count.txt", "w") as f:
    for j in range(len(labels)):
        f.write(str(labels[j]) + ' ' + str(data[j]) + '\n')

# 写文章数
articles_count_count = dict(zip(name,articles_count))
articles_count_count = dict(sorted(articles_count_count.items(), key=lambda d: d[1], reverse=True))
m_name = []
m_count = []
cnt = 0
for k, v in articles_count_count.items():
    m_name.append(k)
    m_count.append(v)
    cnt += 1
    if cnt == 30:
        break
data = m_count
labels = m_name
plt.title('写文章数—Top30')
plt.xticks(rotation=90)
plt.bar(range(len(data)), data, tick_label=labels, align='center')
plt.savefig("articles_count.jpg")
plt.show()
with open("articles_count.txt", "w") as f:
    for j in range(len(labels)):
        f.write(str(labels[j]) + ' ' + str(data[j]) + '\n')

# 教育情况
remove_edu_worrds = ['本科', '硕士', '大学', '高中', '初中', '小学', '博士', '研究生']
for i in educations:
    if i in remove_edu_worrds:
        educations.remove(i)
educations_count = []
educations_name = []
for i in range(30):
    educations_name.append(Counter(educations).most_common(30)[i][0])
    educations_count.append(Counter(educations).most_common(30)[i][1])
data = educations_count
labels = educations_name
plt.title('人数最多学校—Top30')
plt.xticks(rotation=90)
plt.bar(range(len(data)), data, tick_label=labels, align='center')
plt.savefig("educations_count.jpg")
plt.show()
with open("educations_count.txt", "w") as f:
    for j in range(len(labels)):
        f.write(str(labels[j]) + ' ' + str(data[j]) + '\n')

# 公司情况
remove_company_worrds = ['无', '无业游民', '医院', '互联网', '微信', '微信公众号', '浙江大学', '自由职业', '私募', '搬砖']
for i in companies:
    if i in remove_company_worrds:
        companies.remove(i)
companies_count = []
companies_name = []
for i in range(30):
    companies_name.append(Counter(companies).most_common(30)[i][0])
    companies_count.append(Counter(companies).most_common(30)[i][1])
data = companies_count
labels = companies_name
plt.title('人数最多公司—Top30')
plt.xticks(rotation=90)
plt.bar(range(len(data)), data, tick_label=labels, align='center')
plt.savefig("companies_count.jpg")
plt.show()
with open("companies_count.txt", "w") as f:
    for j in range(len(labels)):
        f.write(str(labels[j]) + ' ' + str(data[j]) + '\n')

# 职业情况
remove_jobs_worrds = []
for i in jobs:
    if i in remove_jobs_worrds:
        jobs.remove(i)
jobs_count = []
jobs_name = []
for i in range(30):
    jobs_name.append(Counter(jobs).most_common(30)[i][0])
    jobs_count.append(Counter(jobs).most_common(30)[i][1])
data = jobs_count
labels = jobs_name
plt.title('人数最多职业—Top30')
plt.xticks(rotation=90)
plt.bar(range(len(data)), data, tick_label=labels, align='center')
plt.savefig("jobs_count.jpg")
plt.show()
with open("jobs_count.txt", "w") as f:
    for j in range(len(labels)):
        f.write(str(labels[j]) + ' ' + str(data[j]) + '\n')

# 行业情况
remove_business_worrds = []
for i in business:
    if i in remove_business_worrds:
        business.remove(i)
business_count = []
business_name = []
for i in range(30):
    business_name.append(Counter(business).most_common(30)[i][0])
    business_count.append(Counter(business).most_common(30)[i][1])
data = business_count
labels = business_name
plt.title('人数最多行业—Top30')
plt.xticks(rotation=90)
plt.bar(range(len(data)), data, tick_label=labels, align='center')
plt.savefig("business_count.jpg")
plt.show()
with open("business_count.txt", "w") as f:
    for j in range(len(labels)):
        f.write(str(labels[j]) + ' ' + str(data[j]) + '\n')



"""
词云的实现方式
"""

# # 教育情况
# remove_edu_worrds = ['本科', '硕士', '大学', '高中', '初中', '小学', '博士', '研究生']
# for i in educations:
#     if i in remove_edu_worrds:
#         educations.remove(i)
# educations_count = []
# for i in range(30):
#     educations_count.append(Counter(educations).most_common(30)[i])
# plt.title('教育情况—Top30')
# wl_space_split = " ".join(str(i) for i in educations_count)
# font_path = r':\Workspace\22.small\05.zhihu-user-1000-4.22\simfang.ttf'
# back_coloring = imread('bg.png')# 设置背景图片
# wc = WordCloud(font_path=font_path,  # 设置字体
#                background_color="white",  # 背景颜色
#                max_words=2000,  # 词云显示的最大词数
#                mask=back_coloring,  # 设置背景图片
#                max_font_size=100,  # 字体最大值
#                random_state=42,
#                margin=1,
#                )
# wc.generate(wl_space_split)
# image_colors = ImageColorGenerator(back_coloring)
# plt.imshow(wc.recolor(color_func=image_colors))
# plt.axis("off")
# # 绘制背景图片为颜色的图片
# plt.figure()
# # plt.imshow(back_coloring, cmap=plt.cm.gray)
# plt.axis("off")
# plt.show()
# wc.to_file('educations.png')
#
# # 公司情况
# remove_company_worrds = ['无', '无业游民', '医院', '互联网', '微信', '微信公众号', '浙江大学', '自由职业', '私募', '搬砖']
# for i in companies:
#     if i in remove_company_worrds:
#         companies.remove(i)
# companies_count = []
# for i in range(30):
#     companies_count.append(Counter(companies).most_common(30)[i])
# plt.title('人数最多公司—Top30')
# wl_space_split = " ".join(str(i) for i in companies_count)
# font_path = r':\Workspace\22.small\05.zhihu-user-1000-4.22\simfang.ttf'
# back_coloring = imread('bg.png')# 设置背景图片
# wc = WordCloud(font_path=font_path,  # 设置字体
#                background_color="white",  # 背景颜色
#                max_words=2000,  # 词云显示的最大词数
#                mask=back_coloring,  # 设置背景图片
#                max_font_size=100,  # 字体最大值
#                random_state=42,
#                margin=1,
#                )
# wc.generate(wl_space_split)
# image_colors = ImageColorGenerator(back_coloring)
# plt.imshow(wc.recolor(color_func=image_colors))
# plt.axis("off")
# # 绘制背景图片为颜色的图片
# plt.figure()
# # plt.imshow(back_coloring, cmap=plt.cm.gray)
# plt.axis("off")
# plt.show()
# wc.to_file('companies.png')