import random

pred = int(input("Effettua la tua predizione\n"))
value = random.randint(1, 6)
print("Il numero estratto a caso è: ")
print(value)
if pred == value:
 print("Hai indovinato il nunero estratto a       caso")
elif pred >= 7:
 print("Il numero da te scelto è troppo grande")
 print("Scegli un numero tra l'1 e il 6")
elif pred < 1:
 print("Il numero da te scelto è troppo piccolo")
 print("Scegli un numero tra l'1 e il 6")
else:
 print("Non hai indovinato il numero estratto a caso")
