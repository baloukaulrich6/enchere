# TODO 1 : le dictionnaire en python
dictionnaire = {"bug" : "value"}
print(dictionnaire["bug"])

# # TODO 2: equation du second degre
# from  math import *
# a = int(input("entre la valeur de a: "))
# b = int(input("entre la valeur de b: "))
# c = int(input("entre la valeur de c: "))
#
# x = 0
# valeur = 0
# def fonction(a, b, c, x, valeur):
#
#     if a!= 0 and b!= 0:
#         delta = 0
#         delta = (b*b) - 4*(a*c)
#
#     print(f"lea valeur de delta est {delta}")
#     if delta > 0 :
#
#        eqaution_1 = float(-b - (sqrt(delta)) / (2*a))
#        eqaution_2 = -b + (sqrt(delta)) / (2*a)
#        eqaution_1 = round(eqaution_1, 2)
#        eqaution_2 = round(eqaution_2, 2)
#        print(f"la solution de l'equation sont {eqaution_1, eqaution_2}")
#     elif delta == 0 :
#         b *= -1
#         x = b / (2 * a)
#         print(f"la solution de l'equation est {x}")
#     elif a != 0 and b == 0:
#         x = b / a
#         valeur = x
#         print (f"la solution est {valeur}")
#
#     else:
#         print("il n'y a pas de solution")
# fonction(a, b, c, x, valeur)


studend_score = {
    "harry": 81,
    "balouka": 78,
    "hermine" : 99,
    "draco": 74,
    "neville" :62,
}
# Don't change the code adove
# TODO-2 create an empty dictionary called student
studend_grade = {}

# TODO-3 write your code below to add grades
for studend in studend_score :
  score = studend_score[studend]
  if score > 90:
      studend_grade[studend] = "Outsanding"
  elif score > 80 :
      studend_grade[studend] = "Exceeds Expectations"
  elif score > 70 :
      studend_grade[studend] = "Acceptable"
  else :
      studend_grade[studend] = "Fail"
print(studend_grade)

# TODO LES IMBRIC ATION DE DICTIONNAIRE
# {
# KEY : [LIST],
# kEY2: {DIST}
#  }
# ici KEY a pour valeur une liste [LIST], et KEY2 a pour valeur un dictionnaire {DICT}

pays = {
    "cameroun": "yaounde",
    "France"  : "paris"
}
tranvel_log = {
    "cameroun": {"citie_visiter":["douala", "yaounde","ebomowa"],"total_visit":12},
    "france":{"cites_visiter": ["paris", "lille", "dijon"],"total_visiter" : 5}
}
# pour le dictionnaire imbrique utilisez la cle citie_visited
tranvel_log = [
    {
    "country":"cameroun",
    "citie_visiter": ["douala", "yaounde", "ebomowa"],
    "total_visit": 12
    },
    {
        "country":"france",
        "cites_visiter": ["paris", "lille", "dijon"],
        "total_visiter": 5
    }
]
def add_new_country(country_visited, times_visiter, citi_visiter):
    new_contry = {}
    new_contry["country"]= country_visited
    new_contry["cites_visiter"] = times_visiter
    new_contry["total_visiter"] = citi_visiter
    tranvel_log.append(new_contry)

add_new_country('russia',2, ["moscow", "saint petersbur"])

print(tranvel_log)

