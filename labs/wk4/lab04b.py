from lab04 import getAllBooks

books = getAllBooks()
total = 0
count = 0

for book in books:
    total += book["Price"]
    count += 1
    avg_price = total / count

print(f'Average of {count} books is: {avg_price}')