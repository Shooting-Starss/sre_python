# 一个迭代器类，它可以迭代输出一个数字列表中的内容

class MyIterator(object):
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            result = self.numbers[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


iterator = MyIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for number in iterator:
    print(number)
