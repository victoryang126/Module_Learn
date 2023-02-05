import functools
# class DataSet:
#
#     def __init__(self, sequence_of_numbers):
#         self._data = tuple(sequence_of_numbers)
#
#     @functools.cached_property
#     def stdev(self):
#         return functools.statistics.stdev(self._data)


class DataSet(object):
    def __init__(self):
        self._images = 1
        # self._labels = 2 #定义属性的名称
    @property
    def images(self): #方法加入@property后，这个方法相当于一个属性，这个属性可以让用户进行使用，而且用户有没办法随意修改。
        return self._images
    @functools.cached_property
    def labels(self):
        return functools.statistics.labels(self._labels)
    # @property
    # def labels(self):
    #     return self._labels
    #
    # @labels.setter
    # def labels(self, value):
    #     self._labels = value
    #
    # @labels.deleter
    # def labels(self):
    #     del self._labels
l = DataSet()
#用户进行属性调用的时候，直接调用images即可，而不用知道属性名_images，因此用户无法更改属性，从而保护了类的属性。
print(l.images) # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）。
print(l.__dict__)
l.labels = 3
# print(l.images) # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）。
print(l.__dict__)
del l.labels
print(l.__dict__)
