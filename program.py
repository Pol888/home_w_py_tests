class ListManipulation:

    def __init__(self, list_one, list_two):
        self.list_one = list_one
        self.list_two = list_two

    def comparison_of_averages(self):
        if sum(self.list_one) / len(self.list_one) > sum(self.list_two) / len(self.list_two):
            print('Первый список имеет большее среднее значение')
        elif sum(self.list_one) / len(self.list_one) < sum(self.list_two) / len(self.list_two):
            print('Второй список имеет большее среднее значение')
        else:
            print('Средние значения равны')
