#1
# import json
#
#
# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
#
#
# json_data = json.dumps(data)
#
# with open('data.json', 'w') as file:
#     file.write(json_data)
#
# print("JSON файл успешно создан.")
#2
# import csv
# data = [    ["Country", "Region", "Sales Revenue", "Number of Orders", "Number of Customers"],
#     ["USA", "East", 50000, 200, 150],
#     ["USA", "West", 75000, 300, 200],
#     ["Canada", "East", 30000, 150, 100],
#     ["Canada", "West", 45000, 250, 150]
# ]
#
# with open("data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)