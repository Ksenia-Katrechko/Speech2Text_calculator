import os
import time
import pyautogui

CONFIDENCE = 0.9
PAUSE = 0.5


def click_button(image_name):
    """Функция для поиска и клика по кнопкам."""
    try:
        if not os.path.exists(image_name):
            raise FileNotFoundError(
                f"Файл {image_name} отсутствует. "
                "Проверьте, существует ли изображение в папке."
            )
        button = pyautogui.locateOnScreen(image_name, confidence=CONFIDENCE)
        if button:
            pyautogui.click(button)
            time.sleep(PAUSE)
            print(f"Нажата кнопка {image_name}")
        else:
            raise ValueError(
                f"Кнопка {image_name} не найдена."
            )
    except Exception as e:
        print(f"Ошибка при поиске {image_name}: {e}")
        raise


def main():
    """Основная логика программы."""
    try:
        os.system("start calc")
        time.sleep(2)
        print("Калькулятор открыт!")

        click_button("1.png")
        click_button("2.png")
        click_button("plus.png")
        click_button("7.png")
        click_button("equals.png")
        print("Программа завершила работу без ошибок!")
    except Exception:
        print("ВНИМАНИЕ! Программа завершена с ошибкой.")


if __name__ == "__main__":
    main()
