Проект по языку Python 3 Мирошникова Александра 029.

Запуск Shell: source <путь до проекта>/start_shell.sh

Запуск бота: source <путь до проекта>/start_bot.sh
При запуске бота будет создано виртуальное окруение.
Для работы бота необходим токен и пароль.

Реализованн класс Shell с функциями:
    Режим бота:
    ● /start или /help. Для получения этой справки.
    ● /authorize <пароль>. Для аутентификации в систему.
    ● /unauthorize. Для выхода из системы.
    Режим Shell:
    ● ls. Выводит список файлов и директорий для текущей директории.
    ● pwd. Выводит полный путь для текущей директории.
    ● cd <путь>. Переходит по относительному или абсолютному пути.
    ● cp <имя файла> <имя файла>. Копирует файл.
    ● mv <имя файла> <имя файла>. Перемещает файл.
    ● rm <имя файла>. Удаляет файл.
    ● rmdir <имя директории>. Удаляет директорию в случае, если она пуста.
    ● mkdir <имя директории>. Создает директорию, если ее не было.
    Дополнительно:
    ● hello. Приветствует пользователя
    ● touch <имя файла>. Создает файл с указанным именем в текущей директории.
    ● echo <Любой ввод>. Печатает ввод.
    ● python <имя файла>. Выполняет код на python. Не дружит с input() в режиме бота.
    ● cat <имя файла>. Выводит содержимое файла.
    ● exit. Завершает работу программы в режиме bash.
    
