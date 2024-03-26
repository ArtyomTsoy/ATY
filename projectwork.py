#                        number 1
# class Pizza:
#     def __init__(self, dough, sauce, topping):
#         self.dough = dough
#         self.sauce = sauce
#         self.topping = topping
#
#     def prepare(self):
#         print("Подготовка пиццы...")
#
#     def bake(self):
#         print("Печь пиццы...")
#
#     def cut(self):
#         print("Разрезаем пиццу...")
#
#     def pack(self):
#         print("Упаковываем пиццу...")
#
# class Order:
#     def __init__(self):
#         self.pizzas = []
#
#     def add_pizza(self, pizza):
#         self.pizzas.append(pizza)
#
#     def calculate_total(self):
#         total = 0
#         for pizza in self.pizzas:
#             total += 2300  # Примерно каждая пицца стоит 2300
#         return total
#
# class Terminal:
#     def __init__(self):
#         self.menu = {
#             1: "Пепперони",
#             2: "Барбекю",
#             3: "Дары Моря"
#         }
#
#     def display_menu(self):
#         print("Меню:")
#         for key, value in self.menu.items():
#             print(f"{key}. {value}")
#
#     def create_order(self):
#         order = Order()
#         while True:
#             self.display_menu()
#             choice = int(input("Введите номер пиццы из меню от 1-3(0 - завершить): "))
#             if choice == 0:
#                 break
#             elif choice in self.menu:
#                 if choice == 1:
#                     pizza = Pizza("тонкое", "томатный", ["пепперони", "сыр"])
#                 elif choice == 2:
#                     pizza = Pizza("толстое", "барбекю соус", ["курица", "лук", "сыр"])
#                 elif choice == 3:
#                     pizza = Pizza("тонкое", "сливочный соус", ["креветки", "кальмары", "сыр"])
#                 order.add_pizza(pizza)
#             else:
#                 print("Введите предложенный номер.")
#         return order
#
#     def confirm_order(self, order):
#         print("Ваш заказ:")
#         for i, pizza in enumerate(order.pizzas, start=1):
#             print(f"{i}. Пицца с {pizza.dough} тестом, {pizza.sauce} соусом и {', '.join(pizza.topping)}")
#         print(f"Общая сумма: KZT{order.calculate_total()}")
#
#     def take_payment(self, order):
#         total = order.calculate_total()
#         payment = float(input(f"Введите сумму для оплаты (${total}): "))
#         if payment >= total:
#             print("Оплата прошла успешно. Спасибо!")
#             return True
#         else:
#             print("Недостаточно средств")
#             return False
#
#     def process_order(self):
#         order = self.create_order()
#         self.confirm_order(order)
#         if self.take_payment(order):
#             for pizza in order.pizzas:
#                 pizza.prepare()
#                 pizza.bake()
#                 pizza.cut()
#                 pizza.pack()
#             print("Ваш заказ готов. Приятного аппетита")
#
# if __name__ == "__main__":
#     terminal = Terminal()
#     terminal.process_order()


#                          number 2
# import random
#
# def welcome_player():
#     print("Сыграем в 'Камень, ножницы, бумага'")
#
# def get_player_choice():
#     while True:
#         choice = input("Твой ход: камень (к), ножницы (н) или бумага (б)? ").lower()
#         if choice in ('к', 'н', 'б'):
#             return choice
#         else:
#             print("Выбери 'к', 'н' или 'б'.")
#
# def get_computer_choice():
#     return random.choice(['к', 'н', 'б'])
#
# def determine_winner(player_choice, computer_choice):
#     if player_choice == computer_choice:
#         return "Ничья"
#     elif (player_choice == 'к' and computer_choice == 'н') or \
#          (player_choice == 'н' and computer_choice == 'б') or \
#          (player_choice == 'б' and computer_choice == 'к'):
#         return "Ты победил"
#     else:
#         return "Компьютер победил"
#
# def play_again():
#     return input("Сыграем еще раз? (да/нет): ").lower() == 'да'
#
# def main():
#     welcome_player()
#     while True:
#         player_choice = get_player_choice()
#         computer_choice = get_computer_choice()
#         print(f"Твой выбор: {player_choice}")
#         print(f"Выбор компьютера: {computer_choice}")
#         print(determine_winner(player_choice, computer_choice))
#         if not play_again():
#             break
#     print("Гуд гейм май браза")
#
# if __name__ == "__main__":
#     main()


#                    number 3(Виселица)
# import random
#
# def choose_word():
#     words = ["авокадо", "ананас", "банан", "мандарин", "клубника", "арбуз"]
#     return random.choice(words)
#
# def display_word(word, guessed_letters):
#     display = ""
#     for letter in word:
#         if letter in guessed_letters:
#             display += letter
#         else:
#             display += "_"
#     return display
#
# def hangman():
#     word = choose_word()
#     guessed_letters = []
#     attempts = 6
#
#     print("Го в виселицу")
#     print(display_word(word, guessed_letters))
#
#     while True:
#         guess = input("Угадай букву: ").lower()
#
#         if guess in guessed_letters:
#             print("Эта буква уже была")
#         elif guess in word:
#             guessed_letters.append(guess)
#             print(display_word(word, guessed_letters))
#             if "_" not in display_word(word, guessed_letters):
#                 print("Ты победил")
#                 break
#         else:
#             attempts -= 1
#             print(f"Неправильно. Осталось попыток: {attempts}")
#             if attempts == 0:
#                 print(f"Ты проиграл. Загаданное слово было '{word}'.")
#                 break
#
# if __name__ == "__main__":
#     hangman()


#                    number 3(Угадывание числа)
# import random
#
# def guess_number():
#     number = random.randint(1, 100)
#     attempts = 0
#
#     print("Угадай число от 1 до 100")
#
#     while True:
#         guess = int(input("Твое предположение: "))
#         attempts += 1
#
#         if guess < number:
#             print("Больше")
#         elif guess > number:
#             print("Меньше")
#         else:
#             print(f"Хорош. Ты угадал число {number} за {attempts} попыток")
#             break
#
# if __name__ == "__main__":
#     guess_number()


#                    number 3(Викторина)
# def quiz():
#     questions = {
#         "Сколько планет в Солнечной системе?": "8",
#         "Сколько будет 54-2?": "52, да здравствует санкт-петербург и это город наш",
#         "Сколько раз за день я сходил в туалет?": "5"
#     }
#
#     score = 0
#
#     print("Только гений ответит на эти вопросы")
#
#     for question, answer in questions.items():
#         user_answer = input(question + " ").capitalize()
#         if user_answer == answer:
#             print("А ты хорош")
#             score += 1
#         else:
#             print("Переделывай")
#
#     print(f"Ты набрал {score} из {len(questions)} очков. Нот бэд")
#
# if __name__ == "__main__":
#     quiz()



#                    number 3(Змейка)
# Я ПОНЯТИЯ НЕ ИМЕЮ КАК ЭТО СДЕЛАТЬ



#                    number 3(Генератор MadLibs)
# def mad_libs():
#     name = input("Введите имя: ")
#     animal = input("Введите название животного: ")
#     verb = input("Введите действие: ")
#     adjective = input("Введите прилагательное: ")
#
#     story = f"{name} пришел к {animal} и решил {verb} с ним. {animal} был {adjective} и прыгал от радости"
#     print(story)
#
# if __name__ == "__main__":
#     mad_libs()