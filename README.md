# Куда пойти — Москва глазами Артёма

Фронтенд для будущего сайта о самых интересных местах в Москве.
Авторский проект Артёма.

[Ссылка на сайт](https://ozhiv.pythonanywhere.com/)

[Ссылка на админку сайта](https://ozhiv.pythonanywhere.com/admin/)

### Как установить

Python3 должен быть уже установлен.

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

## Как запустить

* Скачайте код
* Перейдите в каталог проекта с файлом `index.html`
* Запустите веб-сервер
* Откройте в браузере

В качестве веб-сервера можно использовать что угодно. Например, подойдёт даже самый простой встроенный в Python веб-сервер:

```bash
$ python -m http.server 8000
```

## Настройки

Внизу справа на странице можно включить отладочный режим логгирования.

![debug mode](static/.gitbook/assets/debug-option.png)

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки, удалите ключи из Local Storage с помощью Chrome Dev Tools —&gt; Вкладка Application —&gt; Local Storage.

Если что-то работает не так, как ожидалось, то начните с включения отладочного режима логгирования.

<a href="#" id="data-sources"></a>

## Источники данных

Фронтенд получает данные из двух источников. Первый источник — это JSON, запечённый внутрь HTML. Он содержит полный список объектов на карте. И он прячется внутри тега `script`:

```javascript
<script id="places-geojson" type="application/json">
  {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [37.62, 55.793676]
        },
        "properties": {
          // Специфичные для этого сайта данные
          "title": "Легенды Москвы",
          "placeId": "moscow_legends",
          "detailsUrl": "./places/moscow_legends.json"
        }
      },
      // ...
    ]
  }
</script>
```

При загрузке страницы JS код ищет тег с id `places-geojson`, считывает содержимое и помещает все объекты на карту.

Данные записаны в [формате GeoJSON](https://ru.wikipedia.org/wiki/GeoJSON). Все поля здесь стандартные, кроме `properties`. Внутри `properties` лежат специфичные для проекта данные:

* `title` — название локации
* `placeId` — уникальный идентификатор локации, строка или число
* `detailsUrl` — адрес для скачивания доп. сведений о локации в JSON формате

Значение поля `placeId` может быть либо строкой, либо числом. Само значение не играет большой роли, важно лишь чтобы оно было уникальным. Фронтенд использует `placeId` чтобы избавиться от дубликатов — если у двух локаций одинаковый `placeId`, то значит это одно и то же место.

Второй источник данных — это те самые адреса в поле `detailsUrl` c подробными сведениями о локации. Каждый раз, когда пользователь выбирает локацию на карте, JS код отправляет запрос на сервер и получает картинки, текст и прочую информацию об объекте. Формат ответа сервера такой:

```javascript
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```

## Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

