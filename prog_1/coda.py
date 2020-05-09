coda = []

while True:
 print("Options:")
 print("Enter 'aggiungi' per aggiungere una persona alla coda")
 print("Enter 'ricambia' per aggiungere una persona alla coda e rimuovere la prima") 
 print("Enter 'quit' to end the program")
 user_input = input(": ")
 
 if user_input == "ricambia":
  y = (input("Enter a name: "))
  coda.append(y)
  del coda[0]
  print(coda)
 elif user_input == "aggiungi":
  z = (input("Enter a name: "))
  coda.append(z)
  print(coda)
 elif user_input =="quit":
  break
else:
  print("Unknown input")
