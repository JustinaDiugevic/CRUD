def load_default_data():
    return [
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


def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti autorius")
    print("2. Įtraukti autorius i sarasa")
    print("3. koreguoti autorius")
    print("4. šalinti autorius")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")
    return input()
    pasirinkimas = input()

def print_autoriai(autoriai):
            for aut in autoriai:
                print(f"{aut['id']}. Autorius {aut['name']} {aut['surname']}")
            print("-----------------------------------------------------------------")

def prideti_autoriu(id_counter):
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

            return naujas_autorius

def redaguoti_autoriu(autoriai):
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

def istrinti_autoriu(autoriai):
            print("Autoriu salinimas. Pasirinkite ID įrašo kurį norite istrinti.")
            id = input()
            for aut in autoriai:
                if id == str(aut['id']):
                    print(f"{aut['id']}. Autorius {aut['name']} {aut['surname']}")
                    autoriai.remove(aut)

