class Goods:
    def __init__(self, name, weight, cost, category):
        self.name = name
        self.weight = weight
        self.cost = cost
        self.category = category

    def __str__(self):
        return f"Название: {self.name}, Вес: {self.weight}, Стоимость: {self.cost}, Категория: {self.category}"


class Scales:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.goods_on_scales = []

    def add_goods(self, goods):
        self.goods_on_scales.append(goods)
        print(f"Добавлен {goods.name} на весы")

    def remove_goods(self, goods):
        if goods in self.goods_on_scales:
            self.goods_on_scales.remove(goods)
            print(f"Удален {goods.name} с весов")
        else:
            print("Товар не найден на весах")

    def sort_by_cost(self):
        sorted_goods = sorted(self.goods_on_scales, key=lambda x: x.cost)
        print("Товары отсортированы по цене:")
        for goods in sorted_goods:
            print(goods)

    def sort_by_weight(self):
        sorted_goods = sorted(self.goods_on_scales, key=lambda x: x.weight)
        print("Товары отсортированы по весу:")
        for goods in sorted_goods:
            print(goods)

    def min_cost_goods(self):
        min_cost = min(self.goods_on_scales, key=lambda x: x.cost)
        print(f"Товар с минимальной стоимостью: {min_cost}")

    def max_weight_goods(self):
        max_weight = max(self.goods_on_scales, key=lambda x: x.weight)
        print(f"Товар с максимальным весом: {max_weight}")

    def current_weight(self):
        return sum(goods.weight for goods in self.goods_on_scales)

    def total_weight_of_category(self, category):
        total_weight = sum(goods.weight for goods in self.goods_on_scales if goods.category == category)
        print(f"Общий вес товаров в категории '{category}': {total_weight}")

    def get_total_weight(self):
        return sum(goods.weight for goods in self.goods_on_scales)

    def __str__(self):
        return f"Весы: Максимальный вес = {self.max_weight}, Текущий вес = {self.current_weight()}"

# Меню
def print_menu():
    print("Меню:")
    print("1 - Добавить товары")
    print("2 - Отсортировать товары по цене")
    print("3 - Отсортировать товары по весу")
    print("4 - Показать товары с минимальной ценой")
    print("5 - Показать товары с максимальной ценой")
    print("6 - Показать общий вес товаров в категории")
    print("7 - Удалить товары")
    print("0 - Выход")

if __name__ == "__main__":
    scales = Scales(300)
    
    while True:
        print_menu()
        choice = input("Введите ваш выбор: ")
        
        if choice == "1":
            name = input("Введите название товара: ")
            weight = int(input("Введите вес: "))
            cost = int(input("Введите стоимость: "))
            category = input("Введите категорию товара: ")
            goods = Goods(name, weight, cost, category)
            scales.add_goods(goods)
        elif choice == "2":
            scales.sort_by_cost()
        elif choice == "3":
            scales.sort_by_weight()
        elif choice == "4":
            scales.min_cost_goods()
        elif choice == "5":
            scales.max_weight_goods()
        elif choice == "6":
            category = input("Введите категорию: ")
            scales.total_weight_of_category(category)
        elif choice == "7":
            name = input("Введите название товара для удаления: ")
            goods_to_remove = [goods for goods in scales.goods_on_scales if goods.name == name]
            if goods_to_remove:
                for goods in goods_to_remove:
                    scales.remove_goods(goods)
            else:
                print("Товар с таким названием не найден на весах.")
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")
