from main import *

autoriai = load_default_data()
id_counter = 3


def prideti_autoriu(id_counter):
    pass

def print_autoriai(autoriai):
    pass

def redaguoti_autoriu(hollidays):
    pass

def istrinti_autoriu(hollidays):
    pass


while True:
    print_info()
    choise = input()

    match choise:
        case '1':
           print_autoriai(autoriai)
        case '2':
            id_counter +=1
            autoriai.append(prideti_autoriu(id_counter))
        case '3':
           redaguoti_autoriu(autoriai)
        case '4':
           istrinti_autoriu(autoriai)
        case '5':
            print("programa sustabdyta")
            break