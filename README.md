# Куда пойти — Москва глазами Артёма

Сайт о самых интересных местах в Москве для любителей активного отдыха.
Авторский проект Артёма.

[Ссылка на сайт](https://ozhiv.pythonanywhere.com/)

[Ссылка на админку сайта](https://ozhiv.pythonanywhere.com/admin/)

### Как установить

Python3 должен быть уже установлен. Код написан на Python 3.11.

Скачайте или клонируйте репозиторий.

```commandline
git clone https://github.com/OlgaZhivaeva/where_to_go
```

Перейдите в папку проекта `where_to_go`.

```commandline
cd where_to_go
```

Установите и активируйте виртуальное окружение.

Для Windows:
```commandline
python -m venv venv
venv\Scripts\activate.bat
```
Для Linux:
```commandline
python3 -m venv venv
source venv/bin/activate
```
Используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей 

```commandline
pip install -r requirements.txt 
```

### Переменные окружения

Создайте файл `.env` в корне проекта и пропишите в нем переменные окружения

```commandline
SECRET_KEY=Секретный ключ проекта Джанго
DEBUG = True или False
```
### База данных

Выполните команду миграции базы данных

```commandline
python manage.py migrate
```
Создайте суперпользователя командой

```commandline
python manage.py createsuperuser
```

Загрузите данные в базу данных из JSON-файла

```python
python manage.py load_place Путь/до/вашего/JSON-файла
```
Образец JSON-файла с локациями

```json
{
    "title": "Экскурсионная компания «Легенды Москвы»",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/4f793576c79c1cbe68b73800ae06f06f.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7a7631bab8af3e340993a6fb1ded3e73.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/a55cbc706d764c1764dfccf832d50541.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/65153b5c595345713f812d1329457b54.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/0a79676b3d5e3b394717b4bf2e610a57.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1e27f507cb72e76b604adbe5e7b5f315.jpg"
    ],
    "description_short": "Неважно, живёте ли вы в Москве всю жизнь или впервые оказались в столице, составить ёмкий, познавательный и впечатляющий маршрут по городу — творческая и непростая задача. И её с удовольствием берёт на себя экскурсионная компания «Легенды Москвы»!",
    "description_long": "<p>Экскурсия от компании «Легенды Москвы» — простой, удобный и приятный способ познакомиться с городом или освежить свои чувства к нему. Что выберете вы — классическую или необычную экскурсию, пешую прогулку или путешествие по городу на автобусе? Любые варианты можно скомбинировать в уникальный маршрут и создать собственную индивидуальную экскурсионную программу.</p><p>Компания «Легенды Москвы» сотрудничает с аккредитованными экскурсоводами и тщательно следит за качеством экскурсий и сервиса. Автобусные экскурсии проводятся на комфортабельном современном транспорте. Для вашего удобства вы можете заранее забронировать конкретное место в автобусе — это делает посадку организованной и понятной.</p><p>По любым вопросам вы можете круглосуточно обратиться по телефонам горячей линии.</p><p>Подробности узнавайте <a class=\"external-link\" href=\"https://moscowlegends.ru \" target=\"_blank\">на сайте</a>. За обновлениями удобно следить <a class=\"external-link\" href=\"https://vk.com/legends_of_moscow \" target=\"_blank\">«ВКонтакте»</a>, <a class=\"external-link\" href=\"https://www.facebook.com/legendsofmoscow?ref=bookmarks \" target=\"_blank\">в Facebook</a>.</p>",
    "coordinates": {
        "lng": "37.64912239999976",
        "lat": "55.77754550000014"
    }
}

```
### Запуск сайта

Запустите сайт командой

```commandline
python manage.py runserver
```


![&#x41A;&#x443;&#x434;&#x430; &#x43F;&#x43E;&#x439;&#x442;&#x438;](static/.gitbook/assets/site.png)

[Демка сайта](https://devmanorg.github.io/where-to-go-frontend/).


### Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

