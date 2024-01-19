movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


# 1
def IMDB_to_Rating(name):
    for i in range(len(movies)):
        if movies[i]["name"] == name:
            print(movies[i]["imdb"] >= 5.5)


# IMDB_to_Rating("Exam")

# 2
def top_rating(lst):
    sublist = []
    for i in lst:
        for j in range(len(movies)):
            if movies[j]["name"] == i:
                if movies[j]["imdb"] >= 5.5:
                    sublist.append(i)
    print(sublist)


# top_rating(["We Two", "Exam", "Detective", "AlphaJet"])

# 3
def by_category(cat):
    lst = []
    for i in range(len(movies)):
        if movies[i]["category"] == cat:
            lst.append(movies[i]["name"])
    print(lst)


# by_category("Suspense")
# 4
def average_rating(lst):
    sum, cnt = 0, 0
    for i in lst:
        for j in range(len(movies)):
            if movies[j]["name"] == i:
                sum += movies[j]["imdb"]
                cnt += 1
    print(sum / cnt)


# average_rating(["AlphaJet", "Ringing Crime", "Exam", "We Two"])
# 5
def average_rating_by_category(cat):
    sum, cnt = 0, 0
    for i in range(len(movies)):
        if movies[i]["category"] == cat:
            sum += movies[i]["imdb"]
            cnt += 1
    print(sum / cnt)


# average_rating_by_category("Romance")
