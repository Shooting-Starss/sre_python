import os

class FileFinder:
    def __init__(self, addresses):
        self.addresses = addresses

    def find_files(self, target_name):
        """查找指定文件/文件夹是否存在"""
        for address in self.addresses:
            for root, dirs, files in os.walk(address):
                for name in files:
                    if name == target_name:
                        return True
                for name in dirs:
                    if name == target_name:
                        return True
        return False

    def iterate_files(self):
        """使用迭代器输出搜索的指定文件信息"""

        class FileIterator:
            def __init__(self, addresses):
                self.addresses = addresses
                self.index = 0

            def __iter__(self):
                return self

            def __next__(self):
                if self.index >= len(self.addresses):
                    raise StopIteration
                address = self.addresses[self.index]
                self.index += 1
                # 返回文件信息
                return address, os.stat(address).st_size

        return FileIterator(self.addresses)

    def generate_files(self):
        """使用生成器输出搜索的指定文件信息"""
        for address in self.addresses:
            yield address, os.stat(address).st_size

self_name = 'D:\\'
target_name = 'D:\\1073518250\AppWebCache\\1\pub.idqqimg.com\qqfind\css'
finder = FileFinder([self_name, target_name])


# 查找文件/文件夹是否存在
if finder.find_files('target'):
    print("Found!")
else:
    print("Not found.")

# 使用迭代器输出文件信息
for address, size in finder.iterate_files():
    print(f"{address}: {size} bytes")

# 使用生成器输出文件信息
# for address, size in finder.generate_files():
#     print(f"{address}: {size} bytes")
