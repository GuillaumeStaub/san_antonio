import random
quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes!","On doit pouvoir choisir entre s'écouter parler et se faire entendre"]

charachters =["alvin et les Chipmunks","Babar","betty boop","calimero",'casper',"le chat potté","kirikou"]

def show_random_quote(my_list):
    rand_num = random.randint(0,len(my_list)-1)
    item  = my_list[rand_num]
    return item

def capitalize(words):
    for word in words:
        word.capitalize()
    return word

def message(character, quote):
    capitalize(character)
    capitalize(quote)
    return "{} a dit {} ".format(character, quote)

user_answer =input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme").capitalize()


while user_answer != "B":
    print(message(show_random_quote(charachters), show_random_quote(quotes)))
    user_answer =input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme").capitalize()
