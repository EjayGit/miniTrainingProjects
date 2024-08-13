import pprint
programming_language = [
    {"user_name" : "Elshad",
     "favorite_languages" : ["Python", "Java", "C#"],
     "experience": 10 
    },
    {"user_name":"Renad",
     "favorite_languages" : ["Scratch","Python"],
     "experience" : 2
    },
]

def add_new_user(name, fav_langs, exp):
    newUser = {}
    newUser["user_name"] = name
    newUser["favorite_languages"] = fav_langs
    newUser["experience"] = exp
    programming_language.append(newUser)
    pprint.pprint(programming_language)

add_new_user("Edy", ["Java", "Kotlin", "Swift"], 10)