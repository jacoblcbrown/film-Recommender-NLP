# ========= SE T38 - Compulsory Task 2 ===========

# === Importing modules ===
# sPaCy module.
import spacy
nlp = spacy.load('en_core_web_md')


# === Functions ===
# Function which takes an input film description and uses the sPaCy similarity model to find the best recommended film
# from a list of films.
def film_decider(film_desc):
    target_desc = nlp(film_desc)

    # Looping through each potential film, finding the similarity rating and adding it to a list.
    for film in film_desc_list:
        similarity = nlp(film_desc_list[film]).similarity(target_desc)
        film_similarity_list.append((film, similarity))

    # Using a conditional check to find the highest similarity rating in the list.
    highest_film = film_similarity_list[0][0]
    highest_score = film_similarity_list[0][1]

    for film in film_similarity_list:
        if film[1] > highest_score:
            highest_film = film[0]
            highest_score = film[1]

    recommended_film = f"Based on you liking {watched_film[0]}, we recommend you watch {highest_film}!"

    return recommended_film


# Declaring film for comparison and empty lists which will be filled with the potential films the user may watch.
watched_film = ["Planet Hulk", "Will he save their world or destroy it? When the Hulk becomes too dangerous for the "
                              "Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet "
                              "where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he"
                              " is sold into slavery and trained as a gladiator"]
film_desc_list = {}
film_similarity_list = []

# Reading through the text file which contains the list of films the user may watch and adding them to a dictionary.
with open('movies.txt', 'r') as movies:
    for line in movies:
        line = line.strip().split(":")

        film_desc_list[line[0].strip()] = line[1]

# Calling the function and printing the results.
print(film_decider(watched_film[1]))
