import time



while True:


    segundos = int(input("Quantos segundos deseja cronometrar? "))


    while True:
        if segundos == 0:
            segundos = int(input("Erro: Digite outro valor: "))
        if segundos > 0:
            print(f"Cronômetro de {segundos} segundos iniciado!")  
            break   




    while segundos > 0:    
        print(f"* {segundos} *")
        time.sleep(1)
        segundos -= 1
        if segundos == 0:
            print("* 0 *")
            print("** Seu tempo esgotou. **")