class Page:
    def __init__(self, title, subject, content=None):
        self.title = title
        self.subject = subject
        self.content = content

    def __str__(self):
        if self.title is not None and self.subject is not None:
            page = f"{self.title} [{self.subject}]\n\n"
            page += self.content
            return page
        return "Empty Page"


class Notebook:
    def __init__(self):
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)

    def remove_page(self, index):
        self.pages.pop(index)

    def update_page(self, index, page):
        self.pages[index] = page

    def get_page(self, index):
        return self.pages[index]

    def __str__(self):
        if len(self.pages) > 0:
            notebook = ""
            i = 1
            for page in self.pages:
                notebook += f"{i}º - {page.title} [{page.subject}]\n"
                i += 1
            return notebook
        return "Empty Notebook"
