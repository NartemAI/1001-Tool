import functions
from os import system
name_functions = {0: "Список программ", 1: "Монетка"}
kol_functions = 2
kol_functions = len(name_functions)
print("Здраствуйте! Здесь вы найте очень много интересных, веселых и нужных программ!")
print("\t* Введите номер программы\n\t* Введите 0 для просмотра списка программ\n\t* Нажмите Enter для закрытия окна\n\t* Введите -1 для очистки окна")
while True:
@@ -17,3 +17,4 @@
            functions_all.coin_flip()
        case _:
            print("Такой программы нет!🤷")
