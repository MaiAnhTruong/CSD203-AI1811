def f0():
    return 'HE182474'
def insert(self, xType, xRate, xWing):
  # if the first character of xType is B or xRate is greater than 10, do nothing
  if xType[0] == "B" or xRate > 10:
    return self
  # create a new Bird object with the given parameters
  newBird = Bird(xType, xRate, xWing)
  # if the tree is empty, make the new node the root
  if self is None:
    self = newBird
  # otherwise, compare the new node's rate with the current node's rate
  else:
    # if the new node's rate is less than the current node's rate, insert it in the left subtree
    if xRate < self.rate:
      self.left = self.left.insert(xType, xRate, xWing)
    # if the new node's rate is greater than the current node's rate, insert it in the right subtree
    else:
      self.right = self.right.insert(xType, xRate, xWing)
  # return the root of the tree
  return self
def f2(self):
  # call the helper function with the root of the tree
  self.preorder(self)

def preorder(self, node):
  # if the node is not None, check the wing value and traverse the subtrees
  if node is not None:
    # if the wing value is in the range [4, 10], print the node
    if 4 <= node.wing <= 10:
      print(node.type, node.rate, node.wing)
    # traverse the left subtree
    self.preorder(node.left)
    # traverse the right subtree
    self.preorder(node.right)
def f3(self):
  # create an empty queue and a counter
  queue = []
  counter = 0
  # enqueue the root of the tree
  queue.append(self)
  # while the queue is not empty, dequeue a node and check its position
  while queue:
    # dequeue a node from the queue
    node = queue.pop(0)
    # increment the counter
    counter += 1
    # if the counter is odd, print the node
    if counter % 2 == 1:
      print(node.type, node.rate, node.wing)
    # enqueue the left child of the node if it exists
    if node.left is not None:
      queue.append(node.left)
    # enqueue the right child of the node if it exists
    if node.right is not None:
      queue.append(node.right)
