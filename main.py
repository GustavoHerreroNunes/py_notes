from Notebook import Notebook, Page

if __name__ == "__main__":
    my_note = Notebook()
    first_page = Page("My first Note", "Common", "Test")

    my_note.add_page(first_page)
    print(my_note)

    first_page.content = "Some important text!"
    my_note.update_page(0, first_page)
    print(my_note.get_page(0))

    my_note.remove_page(0)
    print(my_note)
