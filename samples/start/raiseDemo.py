# author=shuyang
class my_error(Exception):
    def __init__(self, stri):
        self.leng = len(stri)

    def process(self):
        if self.leng < 5:
            return 'The input is of length %s,expecting at least 5' % self.leng
        else:
            return 'print success'
# e = new my_error('ssss')
# # try:
#     raise my_error('sss')
# except my_error as e:
#     print(e.process())
