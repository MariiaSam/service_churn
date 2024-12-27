import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Завантаження моделі та scaler
model = joblib.load('model/model.joblib')  # Шлях до файлу моделі
scaler = joblib.load('model/scaled.joblib')  # Шлях до файлу scaler

# Функція для обробки вхідних даних
def preprocess_input(data):
    # Перетворення даних у DataFrame
    input_data = pd.DataFrame([data])

    # Масштабування числових даних
    numeric_features = ['subscription_age', 'bill_avg', 'reamining_contract', 'service_failure_count', 'download_avg', 'upload_avg', 'download_over_limit']
    input_data[numeric_features] = scaler.transform(input_data[numeric_features])

    # Повернення підготовлених даних
    return input_data

# Головна функція додатку
def main():
    st.title("Прогнозування Відтоку Клієнтів")
    st.write("Цей додаток допомагає визначити ймовірність відтоку клієнта.")

    # Поля для вводу даних клієнта
    with st.form("client_data_form"):
        st.header("Введіть дані клієнта")
        # Поля с подсказками
        subscription_age = st.number_input(
        "Вік підписки (місяців)",
        min_value=0.0,
        max_value=120.0,  # <-- Укажите максимальное значение
        step=0.1,
        help="Вкажіть вік підписки від 0 до 120 місяців."  # <-- Подсказка
    )
        bill_avg = st.number_input(
        "Середній рахунок",
        min_value=0.0,
        max_value=500.0,  # <-- Укажите максимум
        step=0.1,
        help="Середній місячний рахунок, значення від 0 до 500."
    )
        reamining_contract = st.number_input(
        "Залишок контракту (місяців)",
        min_value=0.0,
        max_value=24.0,  # <-- Укажите максимум
        step=0.1,
        help="Кількість місяців до завершення контракту (від 0 до 24)."
    )
        service_failure_count = st.number_input(
        "Кількість збоїв сервісу",
        min_value=0,
        max_value=10,  # <-- Укажите максимум
        step=1,
        help="Кількість збоїв за період (від 0 до 10)."
    )
        download_avg = st.number_input(
        "Середнє завантаження (GB)",
        min_value=0.0,
        max_value=1000.0,  # <-- Укажите максимум
        step=0.1,
        help="Середній обсяг завантажень в GB (від 0 до 1000)."
    )
        upload_avg = st.number_input(
        "Середнє вивантаження (GB)",
        min_value=0.0,
        max_value=500.0,  # <-- Укажите максимум
        step=0.1,
        help="Середній обсяг вивантажень в GB (від 0 до 500)."
    )
        download_over_limit = st.number_input(
        "Перевищення ліміту завантаження (GB)",
        min_value=0.0,
        max_value=100.0,  # <-- Укажите максимум
        step=0.1,
        help="Перевищення ліміту в GB (від 0 до 100)."
    )
        is_tv_subscriber = st.selectbox(
        "Підписник ТВ",
        [0, 1],
        help="0 - Ні, 1 - Так."
    )
        is_movie_package_subscriber = st.selectbox(
        "Підписник кіно-пакету",
        [0, 1],
        help="0 - Ні, 1 - Так."
    )

        submitted = st.form_submit_button("Передбачити")

        if submitted:
            # Підготовка даних для моделі
            input_data = {
                "is_tv_subscriber": is_tv_subscriber,
                "is_movie_package_subscriber": is_movie_package_subscriber,
                "subscription_age": subscription_age,
                "bill_avg": bill_avg,
                "reamining_contract": reamining_contract,
                "service_failure_count": service_failure_count,
                "download_avg": download_avg,
                "upload_avg": upload_avg,
                "download_over_limit": download_over_limit
            }

            processed_data = preprocess_input(input_data)

            # Передбачення
            prediction = model.predict(processed_data)
            probability = model.predict_proba(processed_data)

            # Вивід результатів
            if prediction[0] == 1:
                st.error(f"Клієнт має високу ймовірність відтоку ({probability[0][1]*100:.2f}%).")
            else:
                st.success(f"Клієнт має низьку ймовірність відтоку ({probability[0][1]*100:.2f}%).")

if __name__ == "__main__":
    main()