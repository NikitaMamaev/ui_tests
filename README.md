# О проекте

Данный проект - результат выполнения тестового задания по написанию UI-автотестов к сервису подписок.

### Использованные паттерны

* Singleton
* Page object
* Page element

# Запуск тестов

Тесты запускаются из корня проекта.

### В Chrome:

```bash
sh ./test_chrome.sh
```

### В Firefox:

```bash
sh ./test_firefox.sh
```

### Необходимое ПО:

* `chromedriver`
* `geckodriver`
* `PyHamcrest`
* `pylint`
* `pytest`
* `requests`
* `selenium`

# Результаты тестирования

Во время тестирования сервис подписок был доступен по IP-адресу `192.168.0.3`, сам же адрес для удобства вынесен в настройки (файл `settings.py`, константа `LOCAL_IP`).

Представленные в проекте тесты можно разделить на позитивные и негативные.

### Позитивные тесты

Позитивные тесты находятся в файлах `tests/test/test_deleting.py`, `tests/test/test_redirecting.py` и `tests/test/test_positive_creating.py`. Список тестов:

* Удаление подписок (`test_subscriptions_deleting`):

Перед тестированием создаётся подписка, в самом же тесте происходит нажатие на кнопку удаления, после чего проверяется, таблица подписок опустела.

* Переход на страницу в GitHub (`test_redirecting`)

В тесте происходит нажатие на кнопку перехода на GitHub с последующей проверкой перехода.

* Создание подписки с корректными данными (`test_creating_with_correct_data`):

В тесте происходит ввод *корректных** данных в поля параметров подписки с последующим нажатием на кнопку "Подписаться", затем проверяется, что в таблице появилась соответствующая запись.

> \* Поскольку к данным не предъявляется явных требований (за исключением валидации email'а при добавлении подписки), было принято решение считать корректными данные, подходящие под следующие регулярные выражения:
>
> Для `email`: "`^\w+@[a-z]+.[a-z]{2,3}`"
>
> Для `name`: "`^[A-Z][a-z]+ [A-Z][a-z]+$`"
>
> Для `time`: "`^(\d+d)? *(\d+h)? *(\d+m)? *(\d+s)? *$`"
>
> Также предполагается, что вводимые значения должны валидироваться.

* Создание подписки и проверка её истечения (`test_creating_with_expiring_time`)

Предполагалось, что подписка считается истёкшей при истечении указанного при её создании промежутка времени, **НО** опытным путём было выявлено, что истёкшими считаются подпискиЮ до истечения которых осталось **8 или менее часов**. Соответственно, в тесте создаётся подписка на 8 часов и 5 секунд, проверяется её активность, а по истечению 10 секунд проверяется, что подписка истекла.

* Создание подписк на малый промежуток времени (`test_creating_with_small_time`)

Исходя из предположения о том, что подписка считается истёкшей, в данном тесте создаётся подписка на 2 часа с последующей проверкой её активности.

* Создание шестой подписки в списке (`test_sixth_subscription_creating`):

Перед тестированием заполняется таблица подписок (создаётся 5 записей), в самом же тесте создаётся ещё одна подписка, и проверяется, что эта подписка попала в таблицу, а та, что создавалась самой первой, из таблицы исчезла.

### Негативные тесты

Негативные тесты находятся в файле `tests/test/test_negative_creating.py`. Список тестов:

* Создание подписки с существующим email'ом (`test_creating_existing_subscription`)

Создание двух подписок с одинаковыми параметрами. Предполагается, что вторая запись не создастся.

* Создание подписки с пустым email'ом (`test_creating_with_empty_email`)

Предполагается, что нельзя создать подписку с пустым email'ом. Предположение основано на тексте в баннере:

> "Для подписки необходимо указать: Email, Имя пользователя и время на которое оформляем подписку"

Данный текст можно интерпретировать как условие, что поля не должны быть пустыми.

* Создание подписки с пустым именем (`test_creating_with_empty_name`)

Предполагается, что нельзя создать подписку с пустым именем.

* Создание подписки с пустым полем времени подписки (`test_creating_with_empty_time`)

Предполагается, что нельзя создать подписку с пустым полем времени подписки.

* Создание подписки с некорректным email'ом (`test_creating_with_incorrect_email`)

Предполагается, что нельзя создать подписку с некорректным email'ом.

* Создание подписки с некорректным именем (`test_creating_with_incorrect_name`)

Предполагается, что нельзя создать подписку с некорректным именем.

* Создание подписки с некорректным временем подписки (`test_creating_with_incorrect_time`)

Предполагается, что нельзя создать подписку с некорректным временем подписки.

* Создание подписки с нулевым временем подписки (`test_creating_with_zero_time`)

Предполагается, что нельзя создать подписку с нулевым временем подписки.

### Результаты запуска тестов:

В Chrome:

![tests-results-chrome](https://i.ibb.co/dgp43M9/2020-05-16-00-02-00.png)

В Firefox:

![tests-results-firefox](https://i.ibb.co/XjD259k/2020-05-16-00-04-47.png)

#### Тесты, которые завершились с **ошибками**:

* Создание подписки с существующим email'ом (`test_creating_existing_subscription`)

При создании двух подписок с одинаковыми данными создаётся две записи вопреки предположению о том, что в таблице не может быть записей с двумя одинаковыми email'ами.

* Создание подписки с пустым именем (`test_creating_with_empty_name`)

Подписка с пустым полем именем создаётся, несмотря на условие, указанное в баннере страницы.

* Создание подписки с пустым значением времени подписки (`test_creating_with_empty_time`)

Подписка с пустым полем значением времени подписки создаётся, несмотря на условие, указанное в баннере страницы.

* Создание подписки с некорректным именем (`test_creating_with_incorrect_name`)

Подписка с некорректным значением именем создаётся.

* Создание подписки с некорректным временем подписки (`test_creating_with_incorrect_time`)

Подписка с некорректным значением временем подписки создаётся.

* Создание подписки на малый промежуток времени (`test_creating_with_small_time`)

Подписка на 2 часа считается неактивной.

* Создание подписки с нулевым временем подписки (`test_creating_with_zero_time`)

Подписка с нулевым значением временем подписки создаётся

#### Описание полученных ошибок (вывод `pytest`):

```sh
================================================================== FAILURES ===================================================================
_____________________________________________________ test_creating_existing_subscription _____________________________________________________

enter = None, clean = None

    @pytest.mark.creating
    @pytest.mark.negative
    def test_creating_existing_subscription(enter, clean):
        """
        Try to create subscription with existing email
        """
    
        with SubscriptionsPage() as page:
            page.input_data(positive)
            page.submit_button.click()
            page.input_data(positive)
            page.submit_button.click()
            page.sync_button.click()
            hc.assert_that(
                actual=page.table.data,
                matcher=hc.has_length(1),
>               reason="Subscription with existing email should not be created!"
            )
E           AssertionError: Subscription with existing email should not be created!
E           Expected: an object with length of <1>
E                but: was <[{'email': 'positive@example.com', 'name': 'Positive Name', 'active': True}, {'email': 'positive@example.com', 'name': 'Positive Name', 'active': True}]> with length of <2>

tests/test/test_negative_creating.py:30: AssertionError
________________________________________________________ test_creating_with_empty_name ________________________________________________________

enter = None, clean = None

    @pytest.mark.creating
    @pytest.mark.negative
    def test_creating_with_empty_name(enter, clean):
        """
        Try to create subscription with empty name
        """
    
        with SubscriptionsPage() as page:
            page.input_data(empty_name)
            page.submit_button.click()
            page.sync_button.click()
            hc.assert_that(
                actual=page.table.data,
                matcher=hc.empty(),
>               reason="Subscription with empty name should not be created!"
            )
E           AssertionError: Subscription with empty name should not be created!
E           Expected: an empty collection
E                but: was <[{'email': 'empty_name@example.com', 'name': '', 'active': True}]>

tests/test/test_negative_creating.py:66: AssertionError
________________________________________________________ test_creating_with_empty_time ________________________________________________________

enter = None, clean = None

    @pytest.mark.creating
    @pytest.mark.negative
    def test_creating_with_empty_time(enter, clean):
        """
        Try to create subscription with empty time
        """
    
        with SubscriptionsPage() as page:
            page.input_data(empty_time)
            page.submit_button.click()
            page.sync_button.click()
            hc.assert_that(
                actual=page.table.data,
                matcher=hc.empty(),
>               reason="Subscription with empty time should not be created!"
            )
E           AssertionError: Subscription with empty time should not be created!
E           Expected: an empty collection
E                but: was <[{'email': 'empty_time@example.com', 'name': 'Empty Time', 'active': False}]>

tests/test/test_negative_creating.py:84: AssertionError
______________________________________________________ test_creating_with_incorrect_name ______________________________________________________

enter = None, clean = None

    @pytest.mark.creating
    @pytest.mark.negative
    def test_creating_with_incorrect_name(enter, clean):
        """
        Try to create subscription with incorrect name
        """
    
        with SubscriptionsPage() as page:
            page.input_data(incorrect_name)
            page.submit_button.click()
            page.sync_button.click()
            hc.assert_that(
                actual=page.table.data,
                matcher=hc.empty(),
>               reason="Subscription with incorrect name should not be created!"
            )
E           AssertionError: Subscription with incorrect name should not be created!
E           Expected: an empty collection
E                but: was <[{'email': 'incorrect_name@example.com', 'name': './*#@!%|^&*(),\'`~;:+-}_=[]?"<>{', 'active': False}]>

tests/test/test_negative_creating.py:120: AssertionError
______________________________________________________ test_creating_with_incorrect_time ______________________________________________________

enter = None, clean = None

    @pytest.mark.creating
    @pytest.mark.negative
    def test_creating_with_incorrect_time(enter, clean):
        """
        Try to create subscription with incorrect time
        """
    
        with SubscriptionsPage() as page:
            page.input_data(incorrect_time)
            page.submit_button.click()
            page.sync_button.click()
            hc.assert_that(
                actual=page.table.data,
                matcher=hc.empty(),
>               reason="Subscription with incorrect time should not be created!"
            )
E           AssertionError: Subscription with incorrect time should not be created!
E           Expected: an empty collection
E                but: was <[{'email': 'incorrect_time@example.com', 'name': 'Incorrect Time', 'active': False}]>

tests/test/test_negative_creating.py:138: AssertionError
________________________________________________________ test_creating_with_zero_time _________________________________________________________

enter = None, clean = None

    @pytest.mark.creating
    @pytest.mark.negative
    def test_creating_with_zero_time(enter, clean):
        """
        Try to create subscription with zero time
        """
    
        with SubscriptionsPage() as page:
            page.input_data(zero_time)
            page.submit_button.click()
            page.sync_button.click()
            hc.assert_that(
                actual=page.table.data,
                matcher=hc.empty(),
>               reason="Subscription with zero time should not be created!"
            )
E           AssertionError: Subscription with zero time should not be created!
E           Expected: an empty collection
E                but: was <[{'email': 'zero_time@example.com', 'name': 'Zero Time', 'active': False}]>

tests/test/test_negative_creating.py:156: AssertionError
________________________________________________________ test_creating_with_small_time ________________________________________________________

enter = None, clean = None

    @pytest.mark.creating
    @pytest.mark.positive
    def test_creating_with_small_time(enter, clean):
        """
        Test of creating subscription with correct data
        """
    
        with SubscriptionsPage() as page:
            page.input_data(small_time)
            page.submit_button.click()
            page.sync_button.click()
            hc.assert_that(
                actual=page.table.data,
                matcher=hc.has_item(hc.has_entries({
                    'active': True,
                })),
>               reason="Supscription should be active!"
            )
E           AssertionError: Supscription should be active!
E           Expected: a sequence containing a dictionary containing {'active': <True>}
E                but: was <[{'email': 'small_time@example.com', 'name': 'Small Time', 'active': False}]>

tests/test/test_positive_creating.py:79: AssertionError
=========================================================== short test summary info ===========================================================
FAILED tests/test/test_negative_creating.py::test_creating_existing_subscription - AssertionError: Subscription with existing email should n...
FAILED tests/test/test_negative_creating.py::test_creating_with_empty_name - AssertionError: Subscription with empty name should not be crea...
FAILED tests/test/test_negative_creating.py::test_creating_with_empty_time - AssertionError: Subscription with empty time should not be crea...
FAILED tests/test/test_negative_creating.py::test_creating_with_incorrect_name - AssertionError: Subscription with incorrect name should not...
FAILED tests/test/test_negative_creating.py::test_creating_with_incorrect_time - AssertionError: Subscription with incorrect time should not...
FAILED tests/test/test_negative_creating.py::test_creating_with_zero_time - AssertionError: Subscription with zero time should not be created!
FAILED tests/test/test_positive_creating.py::test_creating_with_small_time - AssertionError: Supscription should be active!
=================================================== 7 failed, 7 passed in 72.42s (0:01:12) ====================================================
```
