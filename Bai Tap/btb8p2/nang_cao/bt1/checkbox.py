from base_element import BaseElement


class Checkbox(BaseElement):
    def click(self):
        print(f"Toggling a checkbox with locator {self.get_locator()}")

    def is_selected(self):
        # Phương thức riêng chỉ Checkbox mới có
        print("Checking selection status....")


if __name__ == "__main__":
    Checkbox(("id", "test")).click()
