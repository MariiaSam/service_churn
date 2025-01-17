# Модель прогнозування відтоку клієнтів для телекомунікаційної компанії

Цей проєкт розроблено для передбачення ймовірності відтоку клієнтів у телекомунікаційній компанії. Інтерактивний інтерфейс створений на основі **Streamlit**, що дозволяє легко взаємодіяти з моделлю та аналізувати результати.

<!-- **https://servicechurn.streamlit.app/** -->

## Опис

**Детальний опис проєкту:**

- використання реальних даних для аналізу поведінки клієнтів;
- визначення ключових факторів, які впливають на ймовірність відтоку;
- побудова моделі машинного навчання для точного прогнозування;
- інтерактивний інтерфейс для завантаження нових даних та аналізу.

**Вимоги до проєкту:**

- опис аналізу та обробки даних;
- деталі моделі і обрані параметри;
- аналіз результатів, метрик;
- опис інтеграції та виведення результатів;
- процес контейнеризації та інструкції користування.

## Технології

**Проєкт реалізовано з використанням таких технологій:**

- **Python**: основна мова програмування;
- **Docker Compose**: для спрощення процесу розгортання та управління проєктом у середовищі Docker.

## Бібліотеки

- **Pandas**: для обробки даних;
- **Numpy**: для числових обчислень;
- **Scikit-learn**: для побудови та оцінки моделей машинного навчання;
- **Matplotlib** та **Seaborn**: для візуалізації даних;
- **Streamlit**: для створення інтерактивного інтерфейсу;
- **Joblib**: для ефективного серіалізування (збереження) та завантаження об'єктів Python.

## Dataset

**Для цього проєкту використовувався набір даних із такими характеристиками:**

- **https://www.kaggle.com/datasets/mehmetsabrikunt/internet-service-churn;**
- формат: `.csv`;
- містить такі ключові стовпці: `churn`, `subscription_age`, `bill_avg`, `download_avg`, тощо.

Датасет складається з 72275 рядків та 11 стовпців.

**id**: унікальний ідентифікатор абонента;

**is_tv_subscriber**: чи є у клієнта є підписка на телебачення?;

**is_movie_package_subscriber**: чи є підписка на кінопакети?;

**subscription_age**: скільки років клієнт користується нашими послугами?;

**bill_avg**: середній рахунок за останні 3 місяці;

**reamining_contract**: скільки років залишилося до закінчення контракту користувача.
Якщо **_null_** - клієнт не мав контракту. Клієнт, який має контрактний час, повинен користуватися послугою до кінця контракту. Якщо він відмовляється від послуги до закінчення контракту, він сплачує штрафний тариф. Є два способи, якими клієнт може користуватися послугами. Один - за допомогою контракту з обмеженим терміном дії, який коштує дешевше, а інший - за допомогою звичайної щомісячної підписки, яка, очевидно, коштує дорожче. Отже, навіть якщо людина не має контракту, вона все одно є користувачем, який сплачує щомісячні платежі;

**service_failure_coun**: кількість звернень клієнтів до колл-центру через збій обслуговування за останні 3 місяці;

**download_avg**: використання Інтернету за останні 3 місяці (ГБ);

**upload_avg**: середнє завантаження за останні 3 місяці (ГБ);

**download_over_limit**: більшість клієнтів мають обмеження на завантаження. Якщо вони досягають цього ліміту, вони повинні заплатити за це. Ця колонка містить «перевищення ліміту» за останні 9 місяців;

**_churn: відтік клієнта. Це цільова колонка, якщо 1 - клієнт скасував свою послугу_**.

## Модель

- В проекті було випробувано такі моделі як: LogisticRegression, RandomForestClassifier та SVM.
- Для підбору найкращих гіперпараметрів використовувався: GridSearchCV.
- Найкращою моделлю виявилась модель RandomForestClassifier з результатом:
  - precision для 0 - 0.92, для 1 - 0.96
  - recall для 0 - 0.95, для 1 - 0.94
  - f1-score для 0 - 0.93, для 1 - 0.95
  - accuracy 0.94
- Найкращі параметри які підібрав GridSearchCV для RandomForestClassifier:
  - 'class_weight': 'balanced'
  - 'max_depth': None
  - 'max_features': 'log2'
  - 'min_samples_leaf': 1
  - 'min_samples_split': 5
  - 'n_estimators': 80

## Запуск локально

1. **Клонування репозиторію:**

```
git clone https://github.com/MariiaSam/service_churn.git
cd service_chur
```

2. **Налаштування середовища за допомогою Poetry:**

Встановіть залежності проєкту:

```
poetry install
```

Для активації віртуального середовища необхідно виконати команду:

```
poetry shell
```

Щоб додати до проекту залежність, необхідно виконати команду

```
poetry add <назва_пакету>
```

Для підтягування існуючих залежностей:

```
poetry install
```

# Використання

Запустіть Streamlit-додаток командою:

```
streamlit run app.py
```

# Docker

Цей проєкт також підтримує Docker-контейнеризацію, що дозволяє легко запускати додаток без необхідності налаштовувати середовище вручну.

## Запуск за допомогою Docker:

1. **Запуск проекту за допомогою Docker Compose**

У кореневій директорії проекту виконайте команду:

```
docker compose up
```

2. **Доступ до додатку:**

Після успішного запуску додаток буде доступний за адресою:

```
http://localhost:8501
```

3. **Зупинка проекту:**

Щоб зупинити проект, виконайте:

```
docker compose down
```

Ця команда зупинить усі сервіси та видалить створені контейнери.
