from main import *

autoriai = load_default_data()
id_counter = 3



while True:

    choise =  print_info()

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