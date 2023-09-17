class tree:
  def __init__(self,data):
    self.node=data
    self.left=None
    self.right=None

  def show(self):
    if self.left:
      self.left.show()
    print(self.node)
    if self.right:
      self.right.show()
 
  def insert(self,new_data):
    if new_data<self.node:
      if self.left is None:
        self.left=tree(new_data)
      else:
        self.left.insert(new_data)
    elif new_data>self.node:
      if self.right is None:
        self.right=tree(new_data)
      else:
        self.right.insert(new_data)

sand=tree(55)
sand.insert(20)
sand.insert(10)
sand.insert(0)
sand.insert(45)
sand.insert(23)
sand.insert(-2)
sand.show()