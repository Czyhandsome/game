class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "标题: 《%s》, 作者: %s" % (self.title, self.author)


class ChildBook(Book):
    def __init__(self, title, author, child):
        Book.__init__(self, title, author)
        self.child = child

    def __str__(self):
        return Book.__str__(self) + ", 儿童: %s" % self.child


if __name__ == '__main__':
    book = Book("雾都孤儿", "狄更斯")
    print(book)

    child_book = ChildBook("安徒生童话", "安徒生", "罗思源")
    print(child_book)
