# Замер скорости скачивания
Скрипт последовательно делает 10 GET-запросов по одному адресу. Каждый раз полностью скачивает ответ, считает фактически прочитанные байты и время от начала запроса до окончания загрузки. Файл читается небольшими частями и не сохраняется на диск.

По умолчанию скачивается [большая фотография с Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Fronalpstock_big.jpg) — около 14,7 МБ. Десять скачиваний расходуют примерно 147 МБ трафика плюс служебные данные.

## Установка на Linux

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

Скачайте проект, откройте терминал в папке `internet-speed-meter` рядом с `main.py` и выполните:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

## Windows

Установите Python 3.10 или новее с [python.org](https://www.python.org/downloads/windows/). При использовании классического установщика включите `Add python.exe to PATH` и установку pip.

Скачайте проект, откройте PowerShell в папке `internet-speed-meter` рядом с `main.py`:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

Если команда `py` не найдена, используйте `python -m venv .venv`.

## Свой адрес

Передайте прямую HTTP- или HTTPS-ссылку на достаточно большой файл первым аргументом. Замените пример своим адресом; кавычки нужны в том числе для ссылок с `&`.

Linux (с активированным окружением):

```bash
python main.py "https://example.com/big-image.jpg"
```

Windows:
```powershell
.\.venv\Scripts\python.exe main.py "https://example.com/big-image.jpg"
```
