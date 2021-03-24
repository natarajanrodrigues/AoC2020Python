class Node: 
  def __init__(self, value):
    self.value = value
    self.next = None
    self.previous = None

class LinkedList:

  def __init__ (self):
    self.head = None
    self.crab_cursor = self.head
    self.nodes_map = {}

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
    self.nodes_map[value] = newNode

  def remove(self, value):
    node_to_remove = self.nodes_map[value]
    node_prev = node_to_remove.previous
    node_next = node_to_remove.next
    node_prev.next = node_next
    node_next.previous = node_prev
    
    node_to_remove.next = None
    node_to_remove.previous = None

    self.nodes_map.pop(value)

  
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
    values = [ i for i in self.nodes_map.keys()]
    values.sort()
    for i in pick_up:
      values.remove(i)

    crab_cursor_index = values.index(self.crab_cursor.value)
    if crab_cursor_index  > 0:
      return values[crab_cursor_index - 1]
    else:
      return values[len(values) - 1]
  
  def move(self, num_move):
    # print("\n-- move {0}--".format(num_move))
    # print("cups: ", end="")
    # self.print_cups()
    
    print(num_move, end = "\r")

    pick_cursor_init = self.crab_cursor.next
    pick_cursor_end = self.crab_cursor
    pick_up = []
    
    for i in range(0,3):      
      pick_cursor_end = pick_cursor_end.next
      pick_up.append(pick_cursor_end.value)
      

    self.crab_cursor.next = pick_cursor_end.next
    self.crab_cursor.next.previous = self.crab_cursor

    pick_cursor_init.previous = None
    pick_cursor_end.next = None
    
    
    # print("pick up: ", ' '.join([str(e) for e in pick_up]))
    
    
    # destination = self.destination(pick_up)

    destination = self.crab_cursor.value
    while True:
      destination -= 1
      if destination < min:
        destination = max
      if destination not in pick_up:
        break 
    
    # print("destination: ", destination)

    # making the moves
    node_destination = self.nodes_map[destination]
    next_node_destination = node_destination.next

    node_destination.next = pick_cursor_init
    pick_cursor_init.previous = node_destination
    pick_cursor_end.next = next_node_destination
    next_node_destination.previous = pick_cursor_end

    self.crab_cursor = self.crab_cursor.next


  # def add_after(self, num_after, num_to_add):
  #   cursor = self.head
  #   while cursor.value != num_after:
  #     cursor = cursor.next
    
  #   newNode = Node(num_to_add)
    
  #   next_c = cursor.next
  #   cursor.next = newNode
  #   newNode.previous = cursor
  #   newNode.next = next_c
  #   next_c.previous = newNode

  def add_after(self, num_after, list_to_add):
    cursor = self.nodes_map[num_after]
    
    for i in list_to_add:
      newNode = Node(i)
      
      next_c = cursor.next
      cursor.next = newNode
      newNode.previous = cursor
      newNode.next = next_c
      next_c.previous = newNode
      self.nodes_map[i] = newNode
      cursor = cursor.next
    



  def play(self, n_moves):
    
    all_keys = self.nodes_map.keys()
    min_num = min(all_keys)
    max_num = max(all_keys)

    for i in range(0, n_moves):
      # self.move(i + 1)

      print("\n-- move {0}--".format(i))
      print("cups: ", end="")
      self.print_cups()
      
      pick_up = []
      pick_cursor = self.crab_cursor
      for i in range(0,3):      
        pick_up.append(pick_cursor.value)
        self.remove(pick_cursor.value)
        pick_cursor = pick_cursor.next

      destination = int(self.crab_cursor.value)

      while True:
        destination -= 1
        if destination < min_num:
          destination = max_num
        if destination not in pick_up:
          break 
      
      self.add_after(destination, pick_up)

      self.crab_cursor = self.crab_cursor.next



    # print("\n-- final --")
    # print("cups: ", end="")
    # self.print_cups()

  def add_str_array(self, str_array):
    for i in str_array:
      self.add(int(i))
  
  def labels_after_1(self):
    cursor = self.head
    # while cursor.value != str(1):
    while cursor.value != 1:
      cursor = cursor.next
    cursor = cursor.next
    res = []
    while cursor.value != 1:
      res.append(cursor.value)
      cursor = cursor.next

    # print(res)
    return ''.join([str(e) for e in res])


    

    
def part_1(input):
  linked_list = LinkedList()
  linked_list.add_str_array(input)

  linked_list.play(100)

  return linked_list.labels_after_1()

def part_2(input):
  linked_list = LinkedList()
  linked_list.add_str_array(input)
  for i in range(10, 1_000_001):
    linked_list.add(str(i))
  
  linked_list.play(10_000_000)

  v1 = int(linked_list.nodes_map[1].next.value)
  v2 = int(linked_list.nodes_map[1].next.next.value)


  return v1 * v2

def main():
  print("Part 1:", part_1("643719258") )
  # print("Part 2:", part_2("389125467") )



if __name__ == "__main__":
  main()




