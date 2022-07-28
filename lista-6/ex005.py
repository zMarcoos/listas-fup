books = []

def add_book(book_name: str, author_name: str, year: int):
  books.append({'title': book_name, 'author': author_name, 'year': year})

  print(f"Livro {book_name} adicionado com sucesso")

def list_all_books():
  for book in books:
    print(f"{book['title']} - {book['author']} - {book['year']}")

def find_book_by_name(book_name: str):
  for book in books:
    if book['title'] == book_name:
      return book
        
def list_books_by_author(author_name: str):
  for book in books:
    if book['author'] == author_name:
      print(f"{book['title']} - {book['author']} - {book['year']}")

def remove_book(book_name: str):
  for index in range(len(books)):
    if books[index]['title'] == book_name:
      books.pop(index)
      print(f"Livro {book_name} removido com sucesso")

def delete_book_table():
  books.clear()

  print('Tabela de livros apagada com sucesso')

def save():
  try:
    file = open('books.txt', 'a')

    for book in books:
      file.write(str(book) + '\n')
    
    print('Livros salvos com sucesso')
  except:
    print('Não foi possível salvar os livros!')
  finally:
    file.close()

def load():
  try:
    file = open('books.txt', 'r')

    for line in file.readlines():
      books.append(eval(line))
  except:
    print('Erro ao carregar os livros!')
  finally:
    file.close()
