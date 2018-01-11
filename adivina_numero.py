

number_to_guess = (6+2)

print("Este juego se llama Adivina el numero,Cuentas de tres oportunidades")

user_number = int(input("Adivina el numero:  "))

if number_to_guess == user_number:
    print("Has ganado")

else:
    print("Has fallado, intentalo otra vez")

    number_user_1 = int(input("Adivina el número: "))
    if number_to_guess == number_user_1:
        print("Has ganado")

    else:
        print("Has fallado, intentalo otra vez")

        number_user = int(input("Adivina el número: "))

        if number_to_guess == number_user:
            print("Has ganado!!")

        else:
            print("Has perdido, Mas suerte para la proxima")







