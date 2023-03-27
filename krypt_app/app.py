from code_class import CodeTypes

def app():
    print("Rodzaje obsługiwanych szyfrów: Szyfr Cezara/Szyfr płotkowy/Szyfr modułowy/Modułowy podwójny")
    ask = input("Wpisz rodzaj kodu do szyfrowania: ").lower()
    codes = CodeTypes()
    match ask:
        case "szyfr cezara":
            rodzaj = input("Zaszyfrować hasło czy odszyfrować?: ").lower()
            if rodzaj == 'zaszyfrować':
                message = input("Wprowadź hasło: ").upper()
                b = input("Wprowadź przesunięcie: ")
                codes.encode_cezar_code(message,int(b))
            elif rodzaj == "odszyfrować":
                message = input("Wprowadź hasło: ").upper()
                b = input("Wprowadź przesunięcie: ")
                codes.decode_cesar_code(message, int(b))
            else:
                print("Błędna akcja")
                repeat = input("Zacząć od nowa?: ").lower()
                if repeat == 'tak':
                    app()

        case "szyfr płotkowy":
            message = input("Wprowadź hasło do zaszyfrowania: ").upper()
            height = input("Wprowadź wysokość płotu: ")
            codes.encode_fence_code(message, int(height))

        case "szyfr modułowy":
            rodzaj = input("Zaszyfrować hasło czy odszyfrować?: ").lower()
            if rodzaj == 'zaszyfrować':
                message = input("Wprowadź hasło: ").upper()
                b = input("Wprowadź przesunięcie b: ")
                codes.encode_modulo(message, int(b))
            elif rodzaj == "odszyfrować":
                message = input("Wprowadź hasło: ").upper()
                b = input("Wprowadź przesunięcie: ")
                codes.decode_modulo(message, int(b))
            else:
                print("Błędna akcja")
                repeat = input("Zacząć od nowa?: ").lower()
                if repeat == 'tak':
                    app()
        case "modułowy podwójny":
            message = input("Wprowadź hasło: ").upper()
            a = input("Wprowadź przesunięcie a: ")
            b = input("Wprowadź przesunięcie b: ")
            codes.encode_decode_module_keys(message, int(a), int(b))
        case _ :
            reapet = input("Błędny typ szyfru, czy chcesz  spróbować ponownie?: ").lower()
            if reapet == "tak":
                app()
            else:
                print("Pal wroty")

app()