def print_book_info(title, author=None, year=None):
    #  Write your code here
    book = f'"{title}"'

    if author is None and year is None:
        print(book)
        return

    addition = ["was written"]

    if author:
        addition.append(f'by {author}')

    if year:
        addition.append(f'in {year}')

    print("{} {}".format(book, " ".join(addition)))
    return
