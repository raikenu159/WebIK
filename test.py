import requests
import html

# amount='aantal vragen' category='category id'(zie onderaan)
response = requests.get("https://opentdb.com/api.php?amount=2&category=9").json() # .json() maakt er een dict van

print(response) # als de response_code 0 is is alles goed gegaan, voor andere codes zie de documentatie
print()

# response = requests.get("https://opentdb.com/api_token.php?command=request").json()['token']
# met code hierboven kan je een api token aanvragen, als je dit doet kan je 6 uur lang requests maken aan de API en onthoud
# het welke vragen je al hebt gehad zodat je niet weer dezelfde krijgt

# de vragen
questions = response['results']
# zo zien die er uit
for question in questions:
    print(question)
    print()

# html.unescape() maakt text van gecodeerde leestekens zoals die voorkomen in sommige vragen
print("voor: &quot;The Sims&quot;?")
print("na: " + html.unescape("&quot;The Sims&quot;?"))
print()

# categorieen
categorieen = [{'id': 9, 'name': 'General Knowledge'}, {'id': 10, 'name': 'Entertainment: Books'},
{'id': 11, 'name': 'Entertainment: Film'}, {'id': 12, 'name': 'Entertainment: Music'}, {'id': 13, 'name': 'Entertainment: Musicals & Theatres'},
{'id': 14, 'name': 'Entertainment: Television'}, {'id': 15, 'name': 'Entertainment: Video Games'}, {'id': 16, 'name': 'Entertainment: Board Games'},
{'id': 17, 'name': 'Science & Nature'}, {'id': 18, 'name': 'Science: Computers'}, {'id': 19, 'name': 'Science: Mathematics'},
{'id': 20, 'name': 'Mythology'}, {'id': 21, 'name': 'Sports'}, {'id': 22, 'name': 'Geography'}, {'id': 23, 'name': 'History'},
{'id': 24, 'name': 'Politics'}, {'id': 25, 'name': 'Art'}, {'id': 26, 'name': 'Celebrities'}, {'id': 27, 'name': 'Animals'},
{'id': 28, 'name': 'Vehicles'}, {'id': 29, 'name': 'Entertainment: Comics'}, {'id': 30, 'name': 'Science: Gadgets'},
{'id': 31, 'name': 'Entertainment: Japanese Anime & Manga'}, {'id': 32, 'name': 'Entertainment: Cartoon & Animations'}]

# er waren best veel categorieen met tussen de 45 en 50 vragen en t verschil lijkt me niet relevant dus ik heb een lijstje gemaakt van categorieen
# waar meer dan 45 vragen in zitten, ik denk dat we uit deze moeten kiezen
meerDan45 = []
for i in range(9, 33):
    r = requests.get("https://opentdb.com/api_count.php?category=" + str(i)).json()
    c = r['category_question_count']
    # print(str(r['category_id']) + '    ', c['total_question_count'], c['total_easy_question_count'], c['total_medium_question_count'], c['total_hard_question_count'])
    if c['total_question_count'] > 45:
        meerDan45.append(r['category_id'])

categorieenMeerDan45 = []
for categorie in categorieen:
    if categorie['id'] in meerDan45:
        print(categorie['name'])
