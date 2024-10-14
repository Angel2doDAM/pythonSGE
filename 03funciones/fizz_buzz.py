
def texto_a_numero(fizz:str, buzz:str):
    veces_fizz = 0
    veces_buzz = 0
    for i in range(1, 101):
        if(i%3==0 and i%5==0):
            print(fizz + buzz)
            veces_fizz += 1
            veces_buzz += 1
        elif(i%3==0):
            print(fizz)
            veces_fizz += 1
        elif(i%5==0):
            print(buzz)
            veces_buzz += 1
        else:
            print(i)
    print(f"Se ha mostrado 'fizz' un total de {veces_fizz} veces")
    print(f"Se ha mostrado 'buzz' un total de {veces_buzz} veces")

texto_a_numero("fizz", "buzz")
