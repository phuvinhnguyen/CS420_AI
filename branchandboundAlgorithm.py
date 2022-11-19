import os, csv, string, sys, math, re, nltk

capacity = 0

group = 0

items = [] #weight, value, class, index

def calculate_upper_bound(value, weight, index, items):
	v = value
	w = weight
	for i in range(len(items)-index):
		if (w+items[i+index][0] <= capacity):
			w += items[i+index][0]
			v -= items[i+index][1]
		else:
			v -= ((float)(capacity-w)/items[i+index][0])*items[i+index][1]
			break
	return v

def calculate_lower_bound(value, weight, index, items):
	v = value
	w = weight
	for i in range(len(items)-index):
		if (w+items[i+index][0] <= capacity):
			w += items[i+index][0]
			v -= items[i+index][1]
		else:
			break
	return v

def checkWeight(items, path):
	s = 0
	for i in range(len(path)):
		s += items[path[i]][0]
	return s <= capacity

def calculate_value(items, path):
	s = 0
	for i in range(len(path)):
		s += items[path[i]][1]
	return s

def isSatisfied(items, path, group):
	isSelected = [0]*group
	for i in range(len(path)):
		isSelected[items[path[i]][2]-1] |= 1
	result = 1
	for i in range(len(isSelected)):
		result *= isSelected[i]
	return result


def knapsack(items):
	#items = sorted(items, key = lambda item: float(item[1])/item[0], reverse = False)
	min_lower_bound = 0
	final_bound = 0
	current_path = []
	final_path = []
	node = []
	print(items)
	#insert a dummy node
	for i in range(len(items)):
		node.append(i)

	while (node!=[]):
		current_path.append(node.pop())
		last = current_path[len(current_path)-1]
		for i in range(len(items)-last-1):
			node.append(i+last+1)
		print(node)
		print(current_path)
		if ((checkWeight(items, current_path) == False) ):
			print(1)
			while ((len(current_path)>0) and (len(node)>0) and (current_path[-1]<node[-1])):
				node.pop()
			while ((len(current_path)>0) and (len(node)>0) and (current_path[-1]>node[-1])):
				current_path.pop()
			continue
		s=calculate_value(items, current_path)
		print(s)
		if ((s>final_bound) and (isSatisfied(items, current_path, group))):
			final_path=[]
			for i in range(len(current_path)):
				final_path.append(current_path[i])
			final_bound = s
			print(final_path)
			print(final_bound)
		if (last==len(items)-1):
			while ((len(current_path)>0) and (len(node)>0) and (current_path[-1]>node[-1])):
				current_path.pop()
	print(final_bound)
	print(final_path)

if __name__ == '__main__':
	capacity = 15
	group = 2
	
	
	items.append([2, 10, 2])
	items.append([4, 10, 2])
	items.append([6, 12, 1])
	items.append([9, 18, 2])
	knapsack(items)