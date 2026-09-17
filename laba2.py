# Консольна програма для перегляду оцінок

users = {
    "student1": {
        "password": "1234",
        "name": "Іван",
        "grades": [12, 10, 8, 7, 5, 4, 3]
    },
    "student2": {
        "password": "qwerty",
        "name": "Олег",
        "grades": [11, 9, 8, 6, 5, 4]
    },
    "student3": {
        "password": "pass123",
        "name": "Марія",
        "grades": [12, 12, 10, 9, 8, 7, 6]
    },
    "student4": {
        "password": "abcd",
        "name": "Анна",
        "grades": [10, 8, 7, 5, 4, 3, 2]
    }
}


print("===================================")
print("       СИСТЕМА ОЦІНОК УЧНІВ")
print("===================================")

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

# Перевірка користувача
if login in users and users[login]["password"] == password:

    user = users[login]
    grades = user["grades"]

    print("\nВхід виконано успішно!")
    print("Учень:", user["name"])

    print("\nВаші оцінки:")
    print(grades)

    # Підрахунок оцінок
    satisfactory = 0
    unsatisfactory = 0

    for grade in grades:
        if 5 <= grade <= 12:
            satisfactory += 1
        elif 1 <= grade <= 4:
            unsatisfactory += 1

    print("\nСтатистика оцінок:")
    print("Задовільних оцінок (5–12):", satisfactory)
    print("Незадовільних оцінок (1–4):", unsatisfactory)

else:
    print("\nПомилка! Неправильний логін або пароль.")