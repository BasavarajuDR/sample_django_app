from django.http import HttpResponse, HttpResponseBadRequest

class Factorial(object):
    # """docstring for Factorial"""
    # def __init__(self, arg):
    #     super(Factorial, self).__init__()
    #     self.arg = arg

    @classmethod
    def run(cls, n):
        res = {'success' : False, 'message' : ''}
        try:
            fact=1
            while(n>0):
                fact = fact*n
                n = n-1
            res['data'] = fact
            res['success'] = True
        except Exception as e:
            res['message'] = str(e)

        return res
