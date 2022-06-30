from chef import Chef

class chineseChef(Chef):
    def make_salad(self):
        print("The chinese chef makes a mango salad.")

    def make_chicken(self):
        print("The chinese chef makes Hainanese Chicken Rice.")
        super().make_chicken()

    def make_special_dish(self):
        print("The chinese chef makes kung pao chicken.")
    
    def make_fried_rice(self):
        print("The chinese chef makes fried rice.")