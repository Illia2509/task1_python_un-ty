import unittest  # Імпортуємо модуль unittest для тестування

class BankAccount:
    # Конструктор класу, який приймає початковий баланс 9(0)
    def __init__(self, initial_balance=0):
        # Перевірка, чи початковий баланс не є від'ємним; в разі від'ємного значення кидається помилка
        if initial_balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")
        # Ініціалізуємо атрибут балансу з переданим початковим балансом
        self._balance = initial_balance

    # Метод для внесення коштів на рахунок
    def deposit(self, amount):
        # Перевірка, чи сума для внесення є більшою за нуль
        if amount <= 0:
            raise ValueError("Сума депозиту має бути більшою за нуль")
        # Збільшуємо баланс на суму депозиту
        self._balance += amount

    # Метод для зняття коштів з рахунку
    def withdraw(self, amount):
        # Перевірка, чи сума для зняття є більшою за нуль
        if amount <= 0:
            raise ValueError("Сума зняття має бути більшою за нуль")
        # Перевірка, чи на рахунку достатньо коштів для зняття
        if amount > self._balance:
            raise ValueError("Недостатньо коштів на рахунку для зняття")
        # Зменшуємо баланс на суму зняття
        self._balance -= amount

    # Метод для отримання поточного балансу рахунку
    def get_balance(self):
        # Повертає поточний баланс рахунку
        return self._balance


class TestBankAccount(unittest.TestCase):
    # Тест на створення рахунку з початковим балансом
    def test_create_account_with_initial_balance(self):
        # Створюємо об'єкт BankAccount з початковим балансом 100
        account = BankAccount(100)
        # Перевіряємо, чи баланс дорівнює 100
        self.assertEqual(account.get_balance(), 100)

    # Тест на внесення коштів
    def test_deposit_funds(self):
        # Створюємо об'єкт BankAccount з початковим балансом 50
        account = BankAccount(50)
        # Вносимо 25 на рахунок
        account.deposit(25)
        # Перевіряємо, чи баланс дорівнює 75
        self.assertEqual(account.get_balance(), 75)

    # Тест на зняття коштів
    def test_withdraw_funds(self):
        # Створюємо об'єкт BankAccount з початковим балансом 100
        account = BankAccount(100)
        # Знімаємо 30 з рахунку
        account.withdraw(30)
        # Перевіряємо, чи баланс дорівнює 70
        self.assertEqual(account.get_balance(), 70)

    # Тест на обробку зняття більшої суми, ніж є на рахунку
    def test_withdraw_insufficient_funds(self):
        # Створюємо об'єкт BankAccount з початковим балансом 50
        account = BankAccount(50)
        # Перевіряємо, чи при спробі зняти 100 викликається помилка ValueError
        with self.assertRaises(ValueError) as context:
            account.withdraw(100)
        # Перевіряємо, чи повідомлення про помилку правильне
        self.assertEqual(str(context.exception), "Недостатньо коштів на рахунку для зняття")

    # Тест на обробку некоректної суми депозиту (негативна сума)
    def test_deposit_negative_amount(self):
        # Створюємо об'єкт BankAccount з початковим балансом 50
        account = BankAccount(50)
        # Перевіряємо, чи при спробі внести негативну суму викликається помилка ValueError
        with self.assertRaises(ValueError) as context:
            account.deposit(-10)
        # Перевіряємо, чи повідомлення про помилку правильне
        self.assertEqual(str(context.exception), "Сума депозиту має бути більшою за нуль")

    # Тест на обробку некоректної суми зняття (негативна сума)
    def test_withdraw_negative_amount(self):
        # Створюємо об'єкт BankAccount з початковим балансом 50
        account = BankAccount(50)
        # Перевіряємо, чи при спробі зняти негативну суму викликається помилка ValueError
        with self.assertRaises(ValueError) as context:
            account.withdraw(-5)
        # Перевіряємо, чи повідомлення про помилку правильне
        self.assertEqual(str(context.exception), "Сума зняття має бути більшою за нуль")

    # Тест на обробку некоректного початкового балансу (негативний баланс)
    def test_create_account_with_negative_initial_balance(self):
        # Перевіряємо, чи при створенні рахунку з від'ємним початковим балансом викликається помилка ValueError
        with self.assertRaises(ValueError) as context:
            BankAccount(-100)
        # Перевіряємо, чи повідомлення про помилку правильне
        self.assertEqual(str(context.exception), "Початковий баланс не може бути від'ємним")

# Запускаємо тести
if __name__ == "__main__":
    unittest.main()
