def saludo():
    hora = 8
    if hora > 6 and hora < 12:
        print("Good Morning")
    elif hora >= 12 and hora < 18:
        print("Good Afternoon") 
    else:
        print("Good Nigth")