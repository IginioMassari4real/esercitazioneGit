print("Inserisci numeri interi. Inserisci 0 per terminare e visualizzare la somma.")
somma = 0

while True:
    numero = int(input("Inserisci un numero: "))
    
    if numero == 0:
        break
    somma += numero

print("La somma dei numeri inseriti è:", somma)