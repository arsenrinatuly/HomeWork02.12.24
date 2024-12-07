import random
import json
# 1
# def shifr_cezar():
#     alfavit_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#     alfavit_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    
#     try:
#         smeshenie = int(input("Шаг шифровки: "))
#     except ValueError:
#         print("Ошибка: шаг шифровки должен быть числом!")
#         return

#     message = input("Введите сообщение для шифровки: ")
#     choose = input("Выбери вариант шифрования RU/ENG?: ").upper()
    
#     itog = ""
    
#     if choose == "ENG":
#         alfavit = alfavit_eng
#     elif choose == "RU":
#         alfavit = alfavit_rus
#     else:
#         print("Ошибка: выберите ENG или RU!")
#         return
    
#     for i in message:
#         if i in alfavit:
#             mesto = alfavit.find(i)
#             new_mesto = (mesto + smeshenie) % len(alfavit)
#             itog += alfavit[new_mesto]
#         else:
#             itog += i  
    
#     print("Результат шифрования:", itog)

# shifr_cezar()

#2
# def slova_naoborot():
#     user_message = input("Введите сообщение 5 слова ОБЯЗАТЕЛЬНО : ")
#     user_message_reverse = [word[::-1] for word in user_message.split()]
#     random.shuffle(user_message_reverse)
#     user_message_dict = {"first_word": user_message_reverse[0], 
#                         "second_word": user_message_reverse[1],
#                         "third_word": user_message_reverse[2],
#                         "fourth_word": user_message_reverse[3],
#                         "fifth_word": user_message_reverse[4]}

#3

# def biggest_dict(**kwargs):
#     try:
#         with open('my_dict.json', 'r', encoding='utf-8') as file:
#             my_dict = json.load(file)
#     except FileNotFoundError:
#         my_dict = {"first_one": "we can do it"}
#     my_dict.update(kwargs)

#     with open('my_dict.json', 'w', encoding='utf-8') as file:
#         json.dump(my_dict, file, ensure_ascii=False, indent=4)
#     print("Обновленный словарь:", my_dict)

# biggest_dict(new_key="new_value", another_key="another_value")


#4

# FILE_NAME = "eng_rus_dict.json"

# def load_dictionary():
#     try:
#         with open(FILE_NAME, "r", encoding="utf-8") as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {}  


# def save_dictionary(dictionary):
#     with open(FILE_NAME, "w", encoding="utf-8") as file:
#         json.dump(dictionary, file, ensure_ascii=False, indent=4)


# def add_word(dictionary):
#     eng_word = input("Введите слово на английском: ").strip()
#     rus_word = input("Введите перевод на русский: ").strip()
#     if eng_word in dictionary:
#         print("Это слово уже есть в словаре. Оно будет обновлено.")
#     dictionary[eng_word] = rus_word
#     save_dictionary(dictionary)
#     print(f"Слово '{eng_word}' добавлено или обновлено.")


# def delete_word(dictionary):
#     eng_word = input("Введите слово на английском, которое нужно удалить: ").strip()
#     if eng_word in dictionary:
#         del dictionary[eng_word]
#         save_dictionary(dictionary)
#         print(f"Слово '{eng_word}' удалено.")
#     else:
#         print("Такого слова нет в словаре.")


# def find_word(dictionary):
#     eng_word = input("Введите слово на английском для поиска: ").strip()
#     if eng_word in dictionary:
#         print(f"Перевод: {dictionary[eng_word]}")
#     else:
#         print("Такого слова нет в словаре.")


# def update_word(dictionary):
#     eng_word = input("Введите слово на английском для замены перевода: ").strip()
#     if eng_word in dictionary:
#         new_rus_word = input("Введите новый перевод: ").strip()
#         dictionary[eng_word] = new_rus_word
#         save_dictionary(dictionary)
#         print(f"Перевод для слова '{eng_word}' обновлен.")
#     else:
#         print("Такого слова нет в словаре.")


# def main():
#     dictionary = load_dictionary()  
#     while True:
#         print("\n--- Англо-русский словарь ---")
#         print("1. Добавить слово")
#         print("2. Удалить слово")
#         print("3. Найти перевод")
#         print("4. Заменить перевод")
#         print("5. Показать весь словарь")
#         print("6. Выход")
#         choice = input("Выберите действие: ")

#         if choice == "1":
#             add_word(dictionary)
#         elif choice == "2":
#             delete_word(dictionary)
#         elif choice == "3":
#             find_word(dictionary)
#         elif choice == "4":
#             update_word(dictionary)
#         elif choice == "5":
#             print("\nТекущий словарь:")
#             for eng, rus in dictionary.items():
#                 print(f"{eng} - {rus}")
#         elif choice == "6":
#             print("Выход из программы.")
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")

# if __name__ == "__main__":
#     main()







#5
# def chetnost():
#     usernumber: int = int(input("Введите ваше число: "))
#     if usernumber % 2 == 0:
#         return True
#     else:
#         return False

# result = chetnost()
# print("Результат:", result)


#6
# def changecash():
#     try:
#         user_cash = int(input("Введите вашу сумму денег в KZT: "))
#         if user_cash < 0:
#             print("Сумма денег должна быть положительной.")
#             return
#         user_choose = input("Введите в какую валюту хотите перевести? USD, RUB, YEN: ")
#         result = 0
#         if user_choose == "USD":
#             result = user_cash // 500
#             print(f"Ваш перевод составил {result} USD.")
#         elif user_choose == "RUB":
#             result = user_cash // 6
#             print(f"Ваш перевод составил {result} RUB.")
#         elif user_choose == "YEN":
#             result = user_cash // 70
#             print(f"Ваш перевод составил {result} YEN.")
#         else:
#             print("К сожалению, такой валюты нет.")
#     except ValueError:
#         print("Пожалуйста, введите корректные данные.")

# changecash()

#7 
# def ticket(sixcifr):
#     sixcifr_in_list = [int(digit) for digit in str(sixcifr)]
    
#     left_side = sixcifr_in_list[:3]
#     right_side = sixcifr_in_list[3:]
#     sum_leftside = left_side[0]+left_side[1]+left_side[2]
#     sum_rightside = right_side[0]+right_side[1]+right_side[2]
#     if sum_leftside == sum_rightside:
#         print("Вы выиграли!")
#     else:
#         print("Вы проиграли!")

#8
# def factorial():
#     user = int(input("Введите число"))
#     if user<0:
#         print("Должно быть положительное число")
#     else:
#         result = 1    
#         for i in range(1, user+1 ):
#             result *= i
#         print(f"Результат: {result}")

# factorial()

# sixcifrr = 123321
# ticket(sixcifrr)


#9
# def recurs(n):
#     if n == 0 or n==1:
#         return 1
#     return n*recurs(n-1)





#10 
# board: list = []
# def create_board(board: list):
#     for i in range(9):
#         board.append(" ")
#     return board
# def show_board(board: list):
#     print(f"""
#     {board[0]} | {board[1]} | {board[2]}
#     {board[3]} | {board[4]} | {board[5]}
#     {board[6]} | {board[7]} | {board[8]}  
#     """)
# board = create_board(board)


# def winner_check(user):
#     possible_wins: list = [
#         [0,1,2], [3,4,5], [6,7,8],
#         [0,3,6], [1,4,7], [2,5,8],
#         [0,4,8], [6,4,2]
#     ]
#     for variant in possible_wins:
#         temp: bool = True
#         for j in variant:
#             if board[j] != user:
#                 temp = False
#                 break
#         if temp:
#             return True
#     return False


# def draw(user):
#     if ' ' in board:
#         return False 
#     else:
#         return True



# def play_game():
#     user = 'X'
#     while True:
#         show_board(board)
#         user_turn = int(input('Укажите номер клетки, куда поставить крестик: ')) - 1 
#         if board[user_turn] == ' ':
#             board[user_turn] = user
#             if winner_check(user):
#                 show_board(board)
#                 print(f'В данной борьбе победил {user}')
#                 break
#             if draw(user):
#                 show_board(board)
#                 print('haahhah draw')
#                 break
#             if user == 'X':
#                 user = 'O'
#             else:
#                 user = 'X'
#         else:
#             print('Это поле уже занято')
# play_game()


#11
# def anagramma(firststroka: str, secondstroka: str):
#     firststroka = firststroka.replace(" ", "").lower()
#     secondstroka = secondstroka.replace(" ", "").lower()
    
#     if sorted(firststroka) == sorted(secondstroka):
#         print("Анаграмма")
#     else:
#         print("Не анаграмма")

# firststroka = "Прив"
# secondstroka = "Врип"
# anagramma(firststroka, secondstroka)

#12
# def convert_first(num):
#     print(f"Двоичное: {bin(num)[2:]}")
#     print(f"Восьмеричное: {oct(num)[2:]}")
#     print(f"Шестнадцатеричное: {hex(num)[2:]}")

# def convert_second():
#     num_bin = input("Введите двоичное число: ")
#     num_oct = input("Введите восьмеричное число: ")
#     num_hex = input("Введите шестнадцатеричное число: ")

#     dec_bin = int(num_bin, 2)
#     dec_oct = int(num_oct, 8)
#     dec_hex = int(num_hex, 16)

#     print(f"Десятичное из двоичного: {dec_bin}")
#     print(f"Десятичное из восьмеричного: {dec_oct}")
#     print(f"Десятичное из шестнадцатеричного: {dec_hex}")

# def main():
#     num = int(input("Введите целое число: "))
#     convert_first(num)
#     convert_second()

# main()

