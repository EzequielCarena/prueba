

apetece_helado_input = input("¿Te apetece un helado? (Si/No): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True

elif apetece_helado_input == "NO":
    apetece_helado = False

else:
    print("Te he dicho que me digas si o no, no se que me has dicho pero cuento como que no")
    apetece_helado = False

tiene_dinero_input = input("¿Tienes dinero para un helado (Si/No): ").upper()
esta_el_senior_de_los_helados_input = input("¿Esta el señor de los helados? (Si/No): ").upper()
esta_tu_tia_input = input("¿Estás con tu tía (Si/No): ").upper()



puedes_permitirtelo = tiene_dinero_input == "Si" or esta_tu_tia_input == "SI"
esta_el_senior_de_los_helados = esta_el_senior_de_los_helados_input == "SI"

if apetece_helado and puedes_permitirtelo and esta_el_senior_de_los_helados:
    print("Pues comete un helado")
else:
    print("Pues nada")
