from base_element import BaseElement


class Button(BaseElement):
    def click(self):
        # __locator là private nên phải lấy qua get_locator()
        print(f"Clicking on a button with locator {self.get_locator()}")


if __name__ == "__main__":
    Button(("id", "test")).click()
