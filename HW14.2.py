"""  Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків.
Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї. """


class Review:

    def __init__(self, text):
        self.text = text


    def __str__(self):
        return f"Відгук: {self.text}"

    def __repr__(self):
        return f"Відгук: {self.text}"

class Book:


    def __init__(self, autor, title, the_year_of_publishing, genre, reviews):
        self.autor = autor
        self.title = title
        self.the_year_of_publishing = the_year_of_publishing
        self.genre = genre
        self.reviews = reviews


    def __str__(self):
        return f"Автор: {self.autor}, Назва книги:  {self.title}, рік видання:  {self.the_year_of_publishing}, жанр:  {self.genre}, \n , відгук: {self.reviews}"


    def __repr__(self):
        return f"Автор: {self.autor}, Назва книги:  {self.title}, рік видання:  {self.the_year_of_publishing}, жанр:  {self.genre}, \n відгук: {self.reviews}"


reviews ={ Review("Лучшие Фентези, это стоит своих денег, читается очень легко."),
           Review("Чудова сага. Раджу прочитати всім."),
           Review("Раджу всім! Неперевершений шедевр. Одна з моїх улюблених книг!")
           }

book1 = Book("А. Сапковський", "Відьмак", 2017 , "фентезі", reviews)
print(book1)