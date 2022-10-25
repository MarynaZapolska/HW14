""" Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та жанр.
Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_. """

class Book:
    my_count = 0


    def __init__(self, autor, name_of_the_book, the_year_of_publishing, genre):
        self.autor = autor
        self.name_of_the_book = name_of_the_book
        self.the_year_of_publishing = the_year_of_publishing
        self.genre = genre

        Book.my_count += 1

    def __str__(self):
        return f"Автор: {self.autor}, Назва книги:  {self.name_of_the_book}, рік видання:  {self.the_year_of_publishing}, жанр:  {self.genre}"


    def __repr__(self):
        return f"Автор: {self.autor}, Назва книги:  {self.name_of_the_book}, рік видання:  {self.the_year_of_publishing}, жанр:  {self.genre}"


mb1 = Book("Д. Овенс", "Там, де співають раки", "2021", "детектив")
print(mb1.__str__())
mb2 = Book("С. Кінг", "Воно", 1986, "Фентезі")
print(mb2.__repr__())

book1 = Book("А. Сапковський", "Відьмак", 2017 , "фентезі")
print(book1)
print("Total books:", book1.my_count)