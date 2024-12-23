# 5. Запишите в файл формата CSV следующую информацию из JSON-файла `Saint-Petersburg24.09.06.json`: 
# Какие погодные условия и атмосферное давление _(pressure_mm)_ по часам в Санкт-Петербурге 08.09.2024


import json
import csv
import os

def process_weather_file(input_file, output_dir, target_date):
    
    # Проверяем наличие каталога для сохранения результата
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Читаем данные из JSON-файла
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Подготовка данных для записи
    output_data = [["Hour", "Condition", "Pressure (mm)"]]
    for forecast in data.get("forecasts", []):
        if forecast.get("date") == target_date:
            for hour_data in forecast.get("hours", []):
                output_data.append([
                    hour_data.get("hour"),
                    hour_data.get("condition"),
                    hour_data.get("pressure_mm")
                ])
            break

    # Создаем путь для сохранения CSV-файла
    output_file = os.path.join(output_dir, f"Weather_{target_date.replace('-', '_')}.csv")
    
    # Записываем данные в CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(output_data)
    
    return output_file

# вызов функции
input_path = 'data/Saint-Petersburg24.09.06.json'  
output_path = 'data/'                              
date = '2024-09-08'                               

result_file = process_weather_file(input_path, output_path, date)
print(f"Результат сохранен в файл: {result_file}")