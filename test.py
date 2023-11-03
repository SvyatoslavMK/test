class Student():
  happy = 20
  def __init__(self, name, height=160):
    self.name = name
    self.height= height
    self.happy +=10
  def show(self):
    print(self.name,self.height,self.happy)

st1 = Student("bob")
st2 = Student("kate",150)

st1.show()
st2.show()


