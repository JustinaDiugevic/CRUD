autoriai = [
    {
        'id': 1,
        "name": "Jonas",
        "surname": "Jonaitis",
    },
    {
        'id': 2,
        "name": "Petras",
        "surname": "Petraitis",
    },
    {
        'id': 3,
        "name": "Antanas",
        "surname": "Antanaitis",
    }
]
id_counter = 4


while True:
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti autorius")
    print("2. Įtraukti autorius i sarasa")
    print("3. koreguoti autorius")
    print("4. šalinti autorius")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")

    pasirinkimas = input()

    match pasirinkimas:
        case "1":
            for aut in autoriai:
                print(f"{aut['id']}. Autorius {aut['name']} {aut['surname']}")
            print("-----------------------------------------------------------------")

        case "2":
            print("Autoriaus pridėjimas:")
            print("Įveskite vardą:")
            vardas = input()
            print("Įveskite pavardę:")
            pavarde = input()

            naujas_autorius = {
            'id': id_counter,
            "name": vardas,
            "surname": pavarde
            }
            autoriai.append(naujas_autorius)
            id_counter += 1

        case "3":
            print("Autoriu redagavimas.Pasirinkite ID įrašo kurį norite redaguoti.")
            id = input()
            for aut in autoriai:
                if id == str(aut['id']):
                    print(f"{aut['id']}. Autorius {aut['name']} {aut['surname']}")
                    print("Įveskite vardą:")
                    aut['name'] = input()
                    print("Įveskite pavardę:")
                    aut['surname'] = input()
                    break

        case "4":
            print("Autoriu salinimas. Pasirinkite ID įrašo kurį norite istrinti.")
            id = input()
            for aut in autoriai:
                if id == str(aut['id']):
                    print(f"{aut['id']}. Autorius {aut['name']} {aut['surname']}")
                    autoriai.remove(aut)

        case "5":
            print("Sustabdyta")
            break