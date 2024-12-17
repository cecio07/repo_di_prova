scelta = -1
while(scelta!=0):

    print("benvenuto nella nostra calcolatrice")
    print("inserisci l'operazione che vuoi effetuare")
    scelta = int(input("1)sottrazione\n2)addizione\n"))

    if scelta == 1: 
        n1 = int(input("inserisci il primo numero: "))
        n2 = int(input("inserisci il secondo numero: "))
        print(f"{n1} - {n2} = {n1-n2}")

    if scelta == 2:
        n1 = int(input("inserisci il primo numero: "))
        n2 = int(input("inserisci il secondo numero: "))
        print(f"{n1} + {n2} = {n1+n2}")
    else:
        print("scelta non correta!")