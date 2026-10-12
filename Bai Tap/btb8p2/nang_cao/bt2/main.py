from driver_factory import DriverFactory

# ===== Bài nâng cao 2: Factory tạo WebDriver =====
for browser in ["chrome", "edge"]:
    try:
        driver = DriverFactory.get_driver(browser)
        print("Driver:", driver)
    except ValueError as e:
        print(f"Lỗi với '{browser}': {e}")
