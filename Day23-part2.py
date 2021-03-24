import time

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
    
    if node_to_remove is self.head:
      self.head = self.head.next

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
      # print(i + 1, end = "\r")

      # print("\n-- move {0}--".format(i + 1))
      # print("cups: ", end="")
      # self.print_cups()
      
      pick_up = []
      pick_cursor = self.crab_cursor.next
      for i in range(0,3):      
        pick_up.append(pick_cursor.value)
        pick_cursor = pick_cursor.next
      
      for i in range(0,3):      
        self.remove(pick_up[i])

      destination = int(self.crab_cursor.value)

      while True:
        destination -= 1
        if destination < min_num:
          destination = max_num
        if destination not in pick_up:
          break 
      
      # print("pick up: ", ' '.join([str(e) for e in pick_up]))
      # print("destination: ", destination)
      
      self.add_after(destination, pick_up)
      self.crab_cursor = self.crab_cursor.next    # end for

    # printing final results
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
    linked_list.add(i)
  linked_list.play(10_000_000)
  v1 = linked_list.nodes_map[1].next.value
  v2 = linked_list.nodes_map[1].next.next.value
  return v1 * v2

def main():
  print("Part 1:", part_1("643719258") )  
  print("Part 2:", part_2("643719258") )


if __name__ == "__main__":
  main()




