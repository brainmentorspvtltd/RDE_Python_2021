dataset = {
    "action" : ["Ironman","Thor","KGF", "Batman","Superman","Aquaman","Hulk",
                "Baahubali","Master","Avengers"],
    "comedy" : ["Thor","Golmaal","Hera Pheri", "Dhamaal", "Yes man", "The mask"],
    "sci-fi" : ["Ironman","Interstellar", "Gravity"],
    "thriller" : ["Oculus","KGF","Superman","Master","Avengers","It","Kahani"],
    "horror" : ["Oculus","It","The Nun"]
}

user = {'Ironman','KGF','Dhamaal','Yes man','Aquaman','Oculus'}

scores = {}

for item in dataset:
    movies = set(dataset[item])
    intersection = user.intersection(movies)
    union = user.union(movies)
    score = len(intersection) / len(union)
    scores[item] = round(score,2)

print(scores)

max_val = max(scores.values())

for item in scores:
    if scores[item] == max_val:
        category = item
        break

rec_movies = set(dataset[category]) - user
print("recommended movies ::",rec_movies)





