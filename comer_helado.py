

apetece_helado_input = input("¿Te apetece un helado? (Si/No): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True

elif apetece_helado_input == "NO":
    apetece_helado = False

else:
    print("Te he dicho que me digas si o no, no se que me has dicho pero cuento como que no")
    apetece_helado = False

tiene_dinero_input = input("¿Tienes dinero para un helado (Si/No): ").upper()

if tiene_dinero_input == "SI":
    puedes_permitirtelo = True

elif tiene_dinero_input == "NO":
    puedes_permitirtelo = False

else:
    print("Te he dicho que me digas si o no, no se que me has dicho pero cuento como que no")
    puedes_permitirtelo = False


esta_el_senior_de_los_helados_input = input("¿Esta el señor de los helados? (Si/No): ").upper()

if esta_el_senior_de_los_helados_input == "SI":
    esta_el_senior_de_los_helados = True

elif esta_el_senior_de_los_helados_input == "NO":
    esta_el_senior_de_los_helados = False

else:
    print("Te he dicho que me digas si o no, no se que me has dicho pero cuento como que no")
    esta_el_senior_de_los_helados = False

esta_tu_tia_input = input("¿Estás con tu tía (Si/No): ").upper()

if esta_tu_tia_input == "SI":
    puedes_permitirtelo = True

elif esta_tu_tia_input == "NO":
    puedes_permitirtelo = False

else:
    print("Te he dicho que me digas si o no, no se que me has dicho pero cuento como que no")
    puedes_permitirtelo = False



#verdadero(True) * verdadero(True) = verdadero
#falso(False) * verdadero(True) = verdadero
#verdadero(True) * falso(False) = verdadero
#falso(False) * falso(False) = falso

if apetece_helado and puedes_permitirtelo and esta_el_senior_de_los_helados:
    print("Pues comete un helado")
else:
    print("Pues nada")




