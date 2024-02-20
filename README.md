### Тестовое задание UTF.Tech

Создать View, который при запросе вернет на  ```127.0.0.1/api/v1/foods/``` вернет выборку, где только Блюда у
которых `is_publish=True`. Если в категории нет блюд (или все блюда данной категории имеют `is_publish=False`) - не
включаем ее в выборку. Запрос в БД сделать любым удобным способом.

### Запуск:

- Клонировать репозиторий ```git clone git@github.com:Chinpakamon/utf_tech_test.git```
- Установить зависимости ```cd backend && pip install -r requirements.txt ```
- Локально запустить
  проект ```python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver```

### Пример работы:

- Запрос на ```http://127.0.0.1:8000/api/v1/foods/``` при ```queryset = FoodCategory.objects.all()```:

```commandline
[
    {
        "id": 1,
        "name_ru": "Морепродукты",
        "name_en": null,
        "name_ch": null,
        "order_id": 10,
        "foods": [
            {
                "internal_code": null,
                "code": 7707,
                "name_ru": "Краб камчатский",
                "description_ru": "Краб спелый. свежий и вкусный.",
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": true,
                "cost": "1000.00",
                "additional": []
            },
            {
                "internal_code": 1,
                "code": 990214,
                "name_ru": "Морской огурец",
                "description_ru": "Огурец морской для салата с помидором",
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "500.00",
                "additional": []
            }
        ]
    },
    {
        "id": 2,
        "name_ru": "Овощи",
        "name_en": null,
        "name_ch": null,
        "order_id": 11,
        "foods": []
    }
]
```

- Запрос на ```http://127.0.0.1:8000/api/v1/foods/``` при выполненном задании:

```commandline
[
    {
        "id": 1,
        "name_ru": "Морепродукты",
        "name_en": null,
        "name_ch": null,
        "order_id": 10,
        "foods": [
            {
                "internal_code": null,
                "code": 7707,
                "name_ru": "Краб камчатский",
                "description_ru": "Краб спелый. свежий и вкусный.",
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": true,
                "cost": "1000.00",
                "additional": []
            }
        ]
    }
]
```

В итоговую выборку попали блюда, у которых ```is_publish=True```. Если в категории нет блюд (или все блюда данной категории имеют `is_publish=False`) - не
включаем ее в выборку.
