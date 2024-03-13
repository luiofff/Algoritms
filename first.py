class Book:
    def __init__(self, author, weight, cost):
        self.author = author
        self.weight = int(weight)  # Convert weight to integer
        self.cost = int(cost)      # Convert cost to integer

    def __str__(self):
        return f"Автор: {self.author}, Вес: {self.weight}, Стоимость: {self.cost}"


class Bookcase:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if self.get_total_weight() + book.weight <= 800:
            self.books.append(book)
            print(f"Добавлена книга авторства {book.author}")
        else:
            print("Невозможно добавить книгу, превышено максимальное значение веса")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Удалена книга авторства {book.author}")
        else:
            print("Книга не найдена в книжном шкафу")

    def search_by_author(self, author):
        found_books = [book for book in self.books if book.author == author]
        if found_books:
            print(f"Книги авторства {author}:")
            for book in found_books:
                print(book)
        else:
            print(f"Книги авторства {author} не найдены")

    def get_total_weight(self):
        return sum(book.weight for book in self.books)

    def get_total_cost(self):
        return sum(book.cost for book in self.books)

    def __str__(self):
        return f"Книжный шкаф: Максимальный вес = {self.max_weight}, Общий вес = {self.get_total_weight()}, Общая стоимость = {self.get_total_cost()}"


if __name__ == "__main__":

    bookcase = Bookcase()
    active = None
    while active != 0:
        print("Меню: 1 - Добавить книгу 2 - Найти по автору 3 - Удалить книгу 0 - выход")
        active = int(input("Введите действие: "))

        if active == 1:
            name = input("Введите имя автора: ")
            weight = input("Введите вес: ")
            price = input("Введите цену книги: ")
            bookcase.add_book(Book(name, weight, price))
        elif active == 2:
            author = input("Введите автора для поиска: ")
            bookcase.search_by_author(author)
        elif active == 3:
            author = input("Введите автора книги, которую хотите удалить: ")
            books_to_remove = [book for book in bookcase.books if book.author == author]
            if books_to_remove:
                for book in books_to_remove:
                    bookcase.remove_book(book)
            else:
                print("Нет книг этого автора в книжном шкафу")
        elif active == 0:
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

    print("Программа завершена.")
