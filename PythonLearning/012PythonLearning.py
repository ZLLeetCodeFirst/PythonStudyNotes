class Calculator(object):
    is_raise = False
    def calc(self, express):
        try:
            return eval(express)
        except ZeroDivisionError:
            # raise
            if self.is_raise:
                print ("zero can not be division.")
            else:
                raise

c = Calculator()
c.is_raise = True
print(c.calc('4/0'))
