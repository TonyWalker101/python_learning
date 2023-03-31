#program to practice functional programming

import csv
from functools import reduce

def count(predicate, itr):
  count_filter = filter(predicate, itr)
  count_reduce = reduce(lambda x,y: x+1, count_filter, 0)

  return count_reduce

def average(itr):
  # If itr is not iterable, this will generate an iterator.  
  iterable = iter(itr) 
  def avg_helper(curr_count, itr, curr_sum):
    #base case
    next_sum = next(itr, "null")
    if next_sum == "null":
      return curr_sum/curr_count

    #computation
    curr_sum += next_sum
    curr_count += 1

    #recursive call
    return avg_helper(curr_count, itr, curr_sum)
  
  return avg_helper(0, iterable, 0)

with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  fields = next(reader)
  count_belgiums = count(lambda x: x[1] == "Belgium", reader)
  print("# of Belgiums: ", count_belgiums)
  csvfile.seek(0)
  avg_portugal = average(map(lambda x: float(x[13]),filter(lambda x: x[1] == "Portugal", reader)))
  print("Average total profit for Portugal: ", avg_portugal)