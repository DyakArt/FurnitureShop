# Система Управления Продукцией Компании "Восьмерка"

Этот проект представляет собой систему для управления продукцией компании "Восьмерка", которая занимается производством шин для легковых автомобилей. Система включает в себя функции просмотра, добавления, удаления и редактирования данных о продукции, а также управления списком материалов, необходимых для производства.

## Начало работы

Эти инструкции помогут вам запустить проект на вашем локальном компьютере для разработки и тестирования.

### Необходимые условия

Для установки и работы с проектом необходимо иметь установленное программное обеспечение:

Python 3.x
PostgreSQL
DBeaver
PyQt5
psycopg2
PyInstaller

### Установка

Пошаговая инструкция по установке и запуску проекта:

1. Склонируйте репозиторий проекта:

    ```bash
    git clone https://github.com/your_username/your_project.git
    cd your_project
    ```

2. Установите виртуальное окружение и активируйте его:

    ```bash
    python -m venv env
    source env/bin/activate  # Для Windows: .\env\Scripts\activate
    ```

3. Установите необходимые зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Настройка базы данных PostgreSQL:

	- Установите PostgreSQL и запустите его;
	- Создайте новую базу данных.

5. Использование DBeaver для импорта данных:

	- Откройте DBeaver и подключитесь к вашей базе данных PostgreSQL;
	- Щелкните правой кнопкой мыши на новой базе данных и выберите `Tools` > `Restore`.
    - Выберите файл дампа базы данных, который расположен в папке "db".
    - Нажмите `Start`, чтобы начать процесс восстановления.	

6. Измените параметры подключения в коде:

	- Откройте файл `model.py` и замените строки подключения на ваши данные:
	```python
    self.conn = psycopg2.connect(dbname="your_db", user="your_username", password="your_password", host="localhost")
    ```
	- Замените `your_db`, `your_username` и `your_password` на ваши данные для подключения к базе данных PostgreSQL.
	
7. Запустите приложение:

    ```bash
    python main.py
    ```
	
8. Для создания исполняемого файла (.exe), используйте PyInstaller:

    ```bash
    python pyinstaller --windowed --name Vosmerka --add-data "img/no_image.png;img" --add-data "img/Восьмерка.png;img" --add-data "img/products/*;img/products" main.py --icon=Восьмерка.ico
    ```

## Авторы

* **Artem Dyakovich** - *Initial work* - [DyakArt](https://github.com/DyakArt)
