import random
import time

def dice():
    print("Добро пожаловать в игру в кости!")
    
    while True:
        # Бросок игрока
        player = random.randint(1, 6)
        print("\nВаш бросок:")
        print("У вас выпало", player)
        
        # Бросок компьютера
        print("\nКомпьютер делает бросок...")
        time.sleep(2)
        ai = random.randint(1, 6)
        print("У компьютера выпало", ai)
        
        # Определение победителя
        if player > ai:
            print("\nВы победили!")
        elif player == ai:
            print("\nНичья!")
        else:
            print("\nВы проиграли!")
        
        # Вопрос о продолжении игры
        while True:
            choice = input("\nХотите сыграть еще раз? (Y/N): ").strip().upper()
            if choice in ["Y", "N"]:
                break
            print("Неверный ввод. Пожалуйста, введите Y или N.")

            
        
        if choice == "N":
            print("Спасибо за игру! До свидания!")
            break
while True:
    print('Нажмите кнопку ввода, чтобы бросить кубик.')
    roll=input()
    dice()

if __name__ == "__main__":
    dice()

