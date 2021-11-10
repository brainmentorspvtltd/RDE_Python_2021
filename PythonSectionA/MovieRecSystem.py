dataset = {
    "action" : ["Ironman","Thor","KGF", "Batman","Superman","Aquaman","Hulk",
                "Baahubali","Master","Avengers"],
    "comedy" : ["Thor","Golmaal","Hera Pheri", "Dhamaal", "Yes man", "The mask"],
    "sci-fi" : ["Ironman","Interstellar", "Gravity"],
    "thriller" : ["Oculus","KGF","Superman","Master","Avengers","It","Kahani"],
    "horror" : ["Oculus","It","The Nun"]
}

user_1 = {'Ironman','KGF','Dhamaal','Yes man','Aquaman','Oculus'}

# Jaccard Distance
scores = {}

for key in dataset:
    movies = set(dataset[key])
    intersection = user_1.intersection(movies)
    union = user_1.union(movies)
    score = len(intersection) / len(union)
    scores[key] = round(score,2)

print(scores)

max_val = max(scores.values())

for key in scores:
    if max_val == scores[key]:
        category = key
        break

rec_movies = set(dataset[category]) - user_1
print("Recommended Movies :",rec_movies)