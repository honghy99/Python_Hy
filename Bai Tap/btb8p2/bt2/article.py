# Bài 2: Lớp con Article kế thừa Document (nằm ở file khác)
from document import Document


class Article(Document):
    def __init__(self, title, author):
        super().__init__(title)   # gọi __init__ của lớp cha để lưu title
        self.author = author

    def show_info(self):          # override phương thức của lớp cha
        print(f"Bài báo: {self.title} - Tác giả: {self.author}")


if __name__ == "__main__":
    Article("Test", "Hy").show_info()
