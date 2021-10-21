class Athlete:
    def __init__(self, value='Jane'):
        self.inner_value = value
        print(self.inner_value)
        # 초기화 function (반드시 필요)
        # return값은 필요 없음

    def getInnerValue(self):
        return self.inner_value

class InheritanceClass(Athlete):
    def __init__(self):
        super().__init__() # 상속

    def setValue(self, first_value):
        self.inherit_value = first_value

    def getValue(self):
        return self.inner_value

# athlete = Athlete() # athlete = Athelte.__init__() 같은 의미
# athlete = Athlete(value='mio')
# athlete.getInnerValue()

inherit = InheritanceClass()
print(inherit.getInnerValue())
inherit.setValue(first_value='mio')
print(inherit.getInnerValue())
