import pandas as pd

# Example DataFrame
data = {
    'item': ['Apple', 'Banana', 'Cherry', 'Date', 'Eggplant', 'Fig', 'Grape', 
             'Honeydew', 'Iceberg', 'Jackfruit', 'Kiwi', 'Lime', 'Mango', 'Nectarine', 'Orange', 'Papaya'],
    'price': [1.2, 0.8, 2.5, 1.0, 1.5, 2.2, 0.9, 3.0, 0.5, 5.0, 1.1, 0.7, 1.8, 2.3, 1.4, 2.7],
    'quantity': [10, 20, 15, 25, 18, 12, 30, 8, 40, 5, 22, 35, 16, 9, 13, 11]
}

df = pd.DataFrame(data)

# Iterate over the first 15 rows and print the price
for index, row in df.head(15).iterrows():
    print(f"Row {index}: Price = {row['price']}")
