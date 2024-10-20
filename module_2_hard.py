def generate_password(n):
    if n < 1 or n > 20:
        return "Число должно быть в диапазоне от 1 до 20."
    pairs = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            pairs.append((i, j))
    password = ""
    for i, j in pairs:
        pair_sum = i + j
        if n % pair_sum == 0:
            password += f"{i}{j}"
    return password
def main():
    while True:
        user_input = input("Введите число от 1 до 20: ")
        try:
            n = int(user_input)
            print(f"Сгенерированный пароль: {generate_password(n)}")
        except ValueError:
            print("Пожалуйста, введите целое число.")
if __name__ == "__main__":
    main()
