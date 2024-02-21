import logging
import os

# Настройка логирования
logging.basicConfig(filename='countries.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
# Словарь стран и столиц
COUNTRIES = {
    "Россия": "Москва",
    "Украина": "Киев",
    "Беларусь": "Минск",
    "Казахстан": "Нур-Султан",
    "Узбекистан": "Ташкент",
    "Таджикистан": "Душанбе",
    "Кыргызстан": "Бишкек",
    "Туркменистан": "Ашхабад",
    "Азербайджан": "Баку",
    "Армения": "Ереван",
}

# Функция поиска столицы
def get_capital(country):
    """
    Функция поиска столицы по названию страны.

    Args:
        country: Название страны.

    Returns:
        Столица страны или сообщение о том, что страна не найдена.
    """

    logging.info('Поиск столицы для страны "{}"'.format(country))
    if country in COUNTRIES:
        capital = COUNTRIES[country]
        logging.info('Столица страны "{}": {}'.format(country, capital))
        return capital
    else:
        logging.warning('Страна "{}" не найдена.'.format(country))
        return 'Страна "{}" не найдена.'.format(country)

# Функция поиска страны
def get_country(capital):
        """
        Функция поиска страны по названию столицы.

        Args:
            capital: Название столицы.

        Returns:
            Страна или сообщение о том, что столица не найдена.
        """

        logging.info('Поиск страны для столицы "{}"'.format(capital))
        for country, capital_name in COUNTRIES.items():
            if capital_name == capital:
                logging.info('Страна для столицы "{}": {}'.format(capital, country))
                return country
        logging.warning('Столица "{}" не найдена.'.format(capital))
        return 'Столица "{}" не найдена.'.format(capital)
# Основная функция
def main():
    """
    Основная функция программы.
    """

    while True:
        # Выбор режима работы
        print('1 - Поиск столицы')
        print('2 - Поиск страны')
        print('0 - Выход')
        choice = input('Введите номер пункта: ')

        if choice == '1':
            # Поиск столицы
            country = input('Введите название страны: ')
            capital = get_capital(country)
            print(capital)

        elif choice == '2':
            # Поиск страны
            capital = input('Введите название столицы: ')
            country = get_country(capital)
            print(country)

        elif choice == '0':
            # Выход
            break

        else:
            print('Неверный выбор.')

if __name__ == '__main__':
    main()