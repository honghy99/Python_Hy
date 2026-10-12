# Bài 2: Lớp cha Document
class Document:
    def __init__(self, title):
        self.title = title

    def show_info(self):
        print(f"Tiêu đề: {self.title}")


if __name__ == "__main__":
    Document("Test").show_info()
