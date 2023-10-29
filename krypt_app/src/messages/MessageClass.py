
class EncodeMessages:

    code_types_info = f"Rodzaje obsługiwanych szyfrów: \n" \
                      "Szyfr Cezara - 1 \n" \
                      "Szyfr Płotkowy - 2 \n" \
                      "Szyfr Prosty Modułowy - 3 \n" \
                      "Szyfr Afiniczny - 4 \n" \
                      "Digram - 5 \n" \
                      "Macierze - 6 \n" \
                      "Playfair - 7 "
    enter_code_type = "Wybierz numer szyfru: "
    choose_action = "Zaszyfrować hasło czy odszyfrować?: "
    encode = "zaszyfrować"
    decode = "odszyfrować"
    input_password = "Wprowadź hasło: "
    input_plaintext = 'Wprowadź klucz do szyfru playfair: '
    input_transition_b = "Wprowadź przesunięcie b: "
    input_transition_a = "Wprowadź przesunięcie a: "
    input_matrix_num1 = "Wprowadź pierwszą wartość w macierzy: "
    input_matrix_num2 = "Wprowadź drugą wartość w macierzy: "
    input_matrix_num3 = "Wprowadź trzecią wartość w macierzy: "
    input_matrix_num4 = "Wprowadź czwartą wartość w macierzy: "
    error_wrong_action = "Błędna akcja"
    restart_question = "Zacząć od nowa?: "
    yes = "tak"
    no = "no"
    input_fence_height = "Wprowadź wysokość płotu: "
    error_type_code = "Błędny typ szyfru, czy chcesz  spróbować ponownie?: "
    message_for_haters = "Niepoprawny wybór"
    message_for_kumpels = "Koksem jesteś B)"
    messege_invalid_type = "Przesunięcia muszą być liczbami!"
    message_invalid_playfair = "Wartości muszą być słowami!"


class SolverMessages:
    solve_message = "Czy chcesz najpierw użyć solvera?: "
    solver_types = "Rodzaje solverów: \n" \
                         "solver do szyfru afinicznego: 1 \n" \
                         "solver do digramu: 2 \n" \
                         "solver do macierzy: 3 "
    choose_solver = "Wpisz numer wybranego solvera: "
    x_input = "Wprowadź pierwszy ciąg liter do zaszyfrowania (x): "
    y_input = "Wprowadź drugi ciąg liter do zaszyfrowania (y): "
    out1_input = "Wprowadź na co one się szyfrują (x): "
    out2_input = "Wprowadź na co one się szyfrują(y): "
    message_invalid_type = "Numery muszą być znakami!"


class AppMessages:
    choose_action = "Wybierz akcję: "
    choose_app = "Solver: 1 \n" \
                 "Szyfrowanie: 2"
    app_error = "Niepoprawna akcja"
