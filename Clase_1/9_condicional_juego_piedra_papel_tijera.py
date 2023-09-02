import random

presentacion = '''

***************JUEGO DE NICO 👨‍💻********************
*********Piedra Papel Tijeras***********
         🧻  🪨   ✂️

'''

print(presentacion)
user_option = input('Por favor elija Piedra, papel o tijeras : ')
options = ['piedra','papel','tijeras']
random_options = (random.randint(0,2))
computer_option = options[random_options]
# print(computer_option)

'''
piedra y piedra empate
piedra gana tijeras
papel gana a piedra

papel y papel empate
papel gana a piedra
tijeras gana a papel


tijeras y tijeras empate
tijeras gana a papel
piedra gana a tijeras

'''

print(f"Eleccion usuario 👨‍🦰: {user_option}")
print(f"Eleccion computador 🤖: {computer_option}")


if user_option.lower() == computer_option:
    print("!!Empate!! ")

elif user_option == "piedra":
    if computer_option=="tijeras":
        print("Usuario Gana Piedra rompe tijeras")
    else :
        print("Computador Gana papel tapa a piedra ☹️")

elif user_option == "papel":
    if computer_option == "tijeras":
        print("Computador gana tijeras corta a papel☹️")
    else :
        print("Usuario Gana papel tapa a piedra") 

elif user_option == "tijeras":
    if computer_option == "piedra":
        print("Computador gana piedra rompe tijeras ☹️")
    else :
        print("Usuario Gana tijeras corta papel")


