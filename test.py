import requests
import html

# # amount='aantal vragen' category='category id'(zie onderaan)
# response = requests.get("https://opentdb.com/api.php?amount=2&category=9").json() # .json() maakt er een dict van

# print(response) # als de response_code 0 is is alles goed gegaan, voor andere codes zie de documentatie
# print()

# # response = requests.get("https://opentdb.com/api_token.php?command=request").json()['token']
# # met code hierboven kan je een api token aanvragen, als je dit doet kan je 6 uur lang requests maken aan de API en onthoud
# # het welke vragen je al hebt gehad zodat je niet weer dezelfde krijgt

# # de vragen
# questions = response['results']
# # zo zien die er uit
# i=1
# for question in questions:
#     print(i, question)
#     print()
#     i+= 1

# # html.unescape() maakt text van gecodeerde leestekens zoals die voorkomen in sommige vragen
# print("voor: &quot;The Sims&quot;?")
# print("na: " + html.unescape("&quot;The Sims&quot;?"))
# print()

# categorieen = requests.get("https://opentdb.com/api_category.php").json()['trivia_categories'] # hierin staan ook de catagory IDs als je die nog wilt zien

# er waren best veel categorieen met tussen de 45 en 50 vragen en t verschil lijkt me niet relevant dus ik heb een lijstje gemaakt van categorieen
# waar meer dan 45 vragen in zitten, ik denk dat we uit deze moeten kiezen
# print('aantal vragen per catagorie')
# print('ID  Total, ez, med, hard')
# meerDan45 = []
# for i in range(9, 33):
#     r = requests.get("https://opentdb.com/api_count.php?category=" + str(i)).json()
#     c = r['category_question_count']
#     print(str(r['category_id']) + '    ', c['total_question_count'], c['total_easy_question_count'], c['total_medium_question_count'], c['total_hard_question_count'])
#     if c['total_question_count'] > 45:
#         meerDan45.append(r['category_id'])
# print()
# print('categorieen met meer dan 45 vragen:')
# categorieenMeerDan45 = []
# for categorie in categorieen:
#     if categorie['id'] in meerDan45:
#         print(categorie['name'])
# General Knowledge(267), Science: Computers(137), geography(250), history(260), animals(69)

a = requests.get("https://opentdb.com/api.php?amount=50&category=9").json()['results'] # general knowledge
b = requests.get("https://opentdb.com/api.php?amount=50&category=18").json()['results'] # computer science
c = requests.get("https://opentdb.com/api.php?amount=50&category=22").json()['results'] # geopraphy
d = requests.get("https://opentdb.com/api.php?amount=50&category=23").json()['results'] # history
e = requests.get("https://opentdb.com/api.php?amount=50&category=27").json()['results'] # animals
questions = []
for i in range(50):
    questions.append(a[i])
    questions.append(b[i])
    questions.append(c[i])
    questions.append(d[i])
    questions.append(e[i])
print(questions[:1][0])
# return render_template('quiz.html', questions)