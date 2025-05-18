# Request Interceptor with SeleniumWire & undetected-chromedriver
Этот проект показывает, как перехватывать HTTP-запросы в браузере Chrome с помощью seleniumwire и undetected_chromedriver, и подменять ответ от сервера на заранее заданный с сайта httpbin.org.
## Что сделано
- Настроена среда с Python 3.11 и виртуальным окружением venv.
- Используется undetected_chromedriver для обхода антибот-защиты.
- Подключён seleniumwire для перехвата HTTP-запросов.
- Написан перехватчик interceptor, который:
    - Проверяет URL запроса,
    - Если он совпадает с REPLACED_URL, создаёт фейковый ответ с кастомным HTML.
- Конфигурация вынесена в .env и загружается через pydantic_settings.
## Установка и запуск
### 1. Установить зависимости 
```
pip install -r requirements.txt
```
### 2. Создать файл .env в корне проекта:
```
URL=https://httpbin.org/html
REPLACED_URL=//httpbin.org/html
BODY=<html><head><title>Fake page</title></head><body><h1>Интерцепт сработал!</h1></body></html>
```
### 3. Запустить скрипт:
```
python main.py
```
Браузер откроется, перехват начнёт работать. Ты можешь вручную перейти по нужному адресу в браузере — если URL запроса совпадает, отобразится подменённая страница.

## Требования
 - Python 3.11
- Google Chrome (v126)
- Установленные зависимости:

