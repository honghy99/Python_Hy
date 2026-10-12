from document import Document
from article import Article
from email_doc import Email

# ===== Bài 2: Tính Kế thừa =====
doc = Document("Tài liệu chung")
article = Article("Python cơ bản", "Hồng Hy")
email = Email("Họp dự án", "admin@company.com")

for item in [doc, article, email]:
    item.show_info()
