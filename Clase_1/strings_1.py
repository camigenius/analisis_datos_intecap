'''
valor_1 =10
valor_2 = 5
total = valor_1 + valor_2

print(f"El valor 1 es {valor_1} y el valor 2 es {valor_2}")
print(f"La suma de los dos valore es {valor_1 + valor_2}")

'''


cadena = '''
Por favor Ingresa una frase
el programa contara el número de
palabras
'''

print(cadena)

frase = input("Ingreesa una frase : ")
frase_con_espacios =  len(frase)
frase_sin_espacios = len(frase.replace(" ",""))
palabras = frase_con_espacios - frase_sin_espacios 

print("Mi frase sin espacios tiene " ,frase_sin_espacios, "caracteres")
print("Mi frase con espacios tiene " ,frase_con_espacios , "caracteres")
print(f"La frase Ingresada Tiene {palabras + 1} palabra(s) ")


