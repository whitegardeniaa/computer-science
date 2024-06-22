##統計116
##鄭雅云 H24126078

###第一題
all_data = []
with open('IMDB-Movie-Data.csv', 'r') as file:
	for line in file:
		datalist = line.strip().split(",")
		all_data.append(datalist)

	first = second = third = 1000
	first_movie = ""
	second_movie = ""
	third_movie = ""

	for data in all_data:
		if data[5] == "2016":

			if int(data[0]) < first:
				third = second
				third_movie = second_movie
				second = first
				second_movie = first_movie
				first = int(data[0])
				first_movie = data[1]

			elif int(data[0]) < second:
				third = second
				third_movie = second_movie
				second = int(data[0])
				second_movie = data[1]

			elif int(data[0]) < third:
				third = int(data[0])
				third_movie = data[1]
	print()
	print("Q1:")
	print("The top three movie are : first:\"%s\", second:\"%s\", third:\"%s\" " %(first_movie, second_movie, third_movie))




###第二題
all_data = []
with open('IMDB-Movie-Data.csv', 'r') as file:
	for line in file:
		datalist = line.strip().split(",")
		all_data.append(datalist)

	director_count = {}
	for data in all_data:
		director = data[3]
		if director in director_count:
			director_count[director] += 1
		else:
			director_count[director] = 1

	max_count = 0
	most_frequent_director = ""

	for director, count in director_count.items():
		if count > max_count:
			max_count = count
			most_frequent_director = director
	print()
	print("Q2:")
	print(director)



###第三題
all_data = []
with open('IMDB-Movie-Data.csv', 'r') as file:
    header = file.readline().strip().split(",")  # Skip the header
    for line in file:
        datalist = line.strip().split(",")
        all_data.append(datalist)

director_revenue = {}
for data in all_data:
    director = data[3]
    revenue = data[9]
    
    if revenue == '' or revenue == 'N/A':
        revenue = 0.0
    else:
        revenue = float(revenue.replace(',', ''))

    if director in director_revenue:
        director_revenue[director] += revenue
    else:
        director_revenue[director] = revenue

max_revenue = 0.0
the_highest_revenue_director = ""
for director, revenue in director_revenue.items():
    if revenue > max_revenue:
        max_revenue = revenue
        the_highest_revenue_director = director
print()
print("Q3:")
print("The director generating the highest total revenue is %s, and the revenue is %.2f" % (the_highest_revenue_director, max_revenue))




##第四題
all_data = []
with open('IMDB-Movie-Data.csv', 'r') as file:
    header = file.readline().strip().split(",")  # Skip the header
    for line in file:
        datalist = line.strip().split(",")
        all_data.append(datalist)

    total_rate = 0
    movie_count = 0
    for data in all_data:
    	actors = data[4].split("|")
    	rate = float(data[7])

    	for actor in actors:
    		if actor == "Emma Watson":
    			total_rate += rate
    			movie_count += 1
    average_rating = total_rate/movie_count
    print()
    print("Q4:")
    print("The average rating of Emma Watson’s movies is %s" %average_rating )




###第五題
all_data = []
with open('IMDB-Movie-Data.csv', 'r') as file:
	header = file.readline().strip().split(",")  # Skip the header
	for line in file:
		datalist = line.strip().split(",")
		all_data.append(datalist)

	actor_dic = {}
	for data in all_data:
		actors = data[4].split("|")

		for actor in actors:
			if actor in actor_dic:
				actor_dic[actor] += 1
			else:
				actor_dic[actor] = 1

	first = second = third = fourth = 0
	first_actor = ""
	second_actor = ""
	third_actor = ""
	fourth_actor = ""

	for actor, movie_count in actor_dic.items():
		if movie_count > first:
			fourth = third
			fourth_actor = third_actor
			third = second
			third_actor = second_actor
			second = first
			second_actor = first_actor
			first = movie_count
			first_actor = actor
		elif movie_count > second:
			fourth = third
			fourth_actor = third_actor
			third = second
			third_actor = second_actor
			second = movie_count
			second_actor = actor
		elif movie_count > third:
			fourth = third
			fourth_actor = third_actor
			third = movie_count
			third_actor = actor
		elif movie_count > fourth:
			fourth = movie_count
			fourth_actor = actor

print()
print("Q5:Top‐4 actors playing the most movies?")
print(f"1st: {first_actor} with {first} movies")
print(f"2nd: {second_actor} with {second} movies")
print(f"3rd: {third_actor} with {third} movies")
print(f"4th: {fourth_actor} with {fourth} movies")




###第六題
from collections import defaultdict, Counter

all_data = []
with open('IMDB-Movie-Data.csv', 'r') as file:
    header = file.readline().strip().split(",")
    for line in file:
        datalist = line.strip().split(",")
        all_data.append(datalist)

collaboration_count = defaultdict(int)

for data in all_data:
    director = data[3]
    actors = data[4].split("|")

    for actor in actors:
        collaboration_count[(director, actor)] += 1

top_7_collaborations = Counter(collaboration_count).most_common(7)

print()
print("Q6:Top‐7 frequent collaboration pairs of director & actor?")
for pair, count in top_7_collaborations:
    director, actor = pair
    print(f"{director:<17} & {actor:<17}: {count} times")





###第七題
from collections import defaultdict

all_data = []
with open('IMDB-Movie-Data.csv', 'r') as file:
    header = file.readline().strip().split(",")
    for line in file:
        datalist = line.strip().split(",")
        all_data.append(datalist)

director_actors = defaultdict(set)

for data in all_data:
    director = data[3]
    actors = data[4].split("|")

    for actor in actors:
        director_actors[director].add(actor)

top_3_directors = sorted(director_actors.items(), key=lambda x: len(x[1]), reverse=True)[:3]

print()
print("Q7:Top‐3 directors who collaborate with the most actors?")
for director, actors in top_3_directors:
    print(f"{director:<18}: {len(actors)} actors")




###第八題
from collections import defaultdict

all_data = []
with open('IMDB-Movie-Data.csv', 'r') as file:
    header = file.readline().strip().split(",")
    for line in file:
        datalist = line.strip().split(",")
        all_data.append(datalist)

actor_genres = defaultdict(set)

for data in all_data:
    actors = data[4].split("|")
    genres = data[2].split("|")

    for actor in actors:
        actor_genres[actor].update(genres)

top_6_actors = sorted(actor_genres.items(), key=lambda x: len(x[1]), reverse=True)[:6]

print()
print("Q8:Top‐6 actors playing in the most genres of movies?")
for actor, genres in top_6_actors:
    print(f"{actor:<15}: {len(genres):>2} genres")
    




###第九題
from collections import defaultdict

all_data = []
with open('IMDB-Movie-Data.csv', 'r') as file:
    header = file.readline().strip().split(",")  # 跳過標題行
    for line in file:
        datalist = line.strip().split(",")
        all_data.append(datalist)

# 建立一個字典來記錄每位演員的電影年份
actor_years = defaultdict(list)

for data in all_data:
    actors = data[4].split("|")  # 假設演員在第 5 列，並用 '|' 分隔
    year = int(data[5])  # 假設年份在第 6 列

    for actor in actors:
        actor_years[actor].append(year)

# 計算每位演員電影年份之間的最大差距
max_year_gaps = {}
for actor, years in actor_years.items():
    if len(years) >= 2:
        max_year_gap = max(years) - min(years)
        max_year_gaps[actor] = max_year_gap

# 找出導致最大差距的前 3 位演員
top_3_actors = sorted(max_year_gaps.items(), key=lambda x: x[1], reverse=True)[:3]

print()
print("Q9:Top 3 actors whose movies lead to the largest maximum gap of years:")
for actor, gap in top_3_actors:
    print(f"{actor:<20}: {gap} years")