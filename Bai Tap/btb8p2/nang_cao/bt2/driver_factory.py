# Bài nâng cao 2: Factory tạo WebDriver
class DriverFactory:
    @staticmethod
    def get_driver(browser_name):
        # staticmethod: không có self, gọi thẳng qua tên class DriverFactory.get_driver(...)
        if browser_name == "chrome":
            print("Initializing Chrome Driver...")
            return "ChromeDriver object"
        elif browser_name == "firefox":
            print("Initializing Firefox Driver...")
            return "FirefoxDriver object"
        else:
            raise ValueError("Browser không được hỗ trợ")
