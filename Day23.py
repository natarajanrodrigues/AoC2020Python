class Node: 
  def __init__(self, value):
    self.value = value
    self.next = None
    self.previous = None

class LinkedList:
  def __init__ (self):
    self.head = None
    self.crab_cursor = self.head

  def add(self, value):
    newNode = Node(value)
    if self.head is None:
      self.head = newNode
      self.head.next = newNode
      self.head.previous = newNode
      self.crab_cursor = self.head
    else:
      
      previous_head = self.head.previous
      previous_head.next = newNode
      
      newNode.previous = previous_head
      newNode.next = self.head
      self.head.previous = newNode

  def remove(self, value):
    cursor = self.head
    while cursor.value is not value:
      cursor = cursor.next
    if cursor is self.head:
      self.head = self.head.next
    
    c_prev = cursor.previous
    c_next = cursor.next
    cursor.next = None
    cursor.previous = None

    c_next.previous = c_prev
    c_prev.next = c_next
  
  def print(self):
    if self.head is None:    
      print("List is empty");    
      return
    else:  
      print("Printing...")
      cursor = self.head
      print(cursor.value, end="")
      while cursor.next is not self.head:
        cursor = cursor.next
        print(cursor.value, end="")
      print()
      return
  
  def print_cups(self):
    if self.head is None:    
      print("List is empty");    
      return
    else:  
      cursor = self.head
      
      while cursor.next is not self.head:
        if cursor.value != self.crab_cursor.value:
          print("{0} ".format(cursor.value), end="")
        else:
          print("({0}) ".format(cursor.value), end="")
        cursor = cursor.next
      if cursor.value != self.crab_cursor.value:
        print("{0} ".format(cursor.value), end="")
      else:
        print("({0}) ".format(cursor.value), end="")
        
      print()
      return

  def destination(self, pick_up):
    values = []
    cursor = self.head
    values.append(cursor.value)
    while cursor.next is not self.head:
      cursor = cursor.next
      values.append(cursor.value)
    values.sort()
    
    crab_cursor_index = values.index(self.crab_cursor.value)
    if crab_cursor_index  > 0:
      return values[crab_cursor_index - 1]
    else:
      return values[len(values) - 1]
  
  def move(self, num_move):
    print("\n-- move {0}--".format(num_move))
    print("cups: ", end="")
    self.print_cups()
    
    pick_up = []
    pick_cursor = self.crab_cursor
    
    for i in range(0,3):
      pick_up.append(pick_cursor.next.value)
      pick_cursor = pick_cursor.next

    for i in range(0,3):
      self.remove(pick_up[i])
    
    print("pick up: ", ' '.join([str(e) for e in pick_up]))
    destination = self.destination(pick_up)
    print("destination: ", destination)

    # making the moves:
    number_after = destination
    for i in range(0,3):
      self.add_after(number_after, pick_up[i])
      number_after = pick_up[i]
    self.crab_cursor = self.crab_cursor.next

  
  def destination2(self, pick_up):
    values = []
    cursor = self.head
    values.append(cursor.value)
    while cursor.next is not self.head:
      cursor = cursor.next
      values.append(cursor.value)
    values.sort()
    
    crab_cursor_index = values.index(self.crab_cursor.value)
    if crab_cursor_index  > 0:
      return values[crab_cursor_index - 1]
    else:
      return values[len(values) - 1]


  def move2(self, num_move):
    
    pick_up = []
    pick_cursor = self.crab_cursor
    
    for i in range(0,3):
      pick_up.append(pick_cursor.next.value)
      pick_cursor = pick_cursor.next

    for i in range(0,3):
      self.remove(pick_up[i])
    
    destination = self.destination2(pick_up)

    # making the moves:
    number_after = destination
    for i in range(0,3):
      self.add_after(number_after, pick_up[i])
      number_after = pick_up[i]
    self.crab_cursor = self.crab_cursor.next


  def add_after(self, num_after, num_to_add):
    cursor = self.head
    while cursor.value != num_after:
      cursor = cursor.next
    
    newNode = Node(num_to_add)
    
    next_c = cursor.next
    cursor.next = newNode
    newNode.previous = cursor
    newNode.next = next_c
    next_c.previous = newNode
    
  def play(self, n_moves):
    for i in range(0, n_moves):
      self.move(i + 1)
    print("\n-- final --")
    print("cups: ", end="")
    self.print_cups()

  def add_str_array(self, str_array):
    for i in str_array:
      self.add(i)
  
  def labels_after_1(self):
    cursor = self.head
    while cursor.value != str(1):
      cursor = cursor.next
    cursor = cursor.next
    res = []
    while cursor.value != str(1):
      res.append(cursor.value)
      cursor = cursor.next

    print(res)
    return ''.join([str(e) for e in res])

  play_2(self, n_moves):

    

    
def part_1(input):
  linked_list = LinkedList()
  linked_list.add_str_array(input)

  linked_list.play(100)

  return linked_list.labels_after_1()

def part_2(input):
  linked_list = LinkedList()
  linked_list.add_str_array(input)

  linked_list.play(100)

  return linked_list.labels_after_1()

def main():
  print("Part 1:", part_1("643719258") )



if __name__ == "__main__":
  main()




