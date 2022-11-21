import os, csv, string, sys, math, re, nltk

capacity = 0

group = 0

items = [] #weight, value, class, index

def input():
	global capacity
	global group
	input_file = open("input/INPUT_x.txt", "r")
	capacity = int(input_file.readline())
	group = int(input_file.readline())
	w = (input_file.readline()).split(",")
	v = (input_file.readline()).split(",")
	c = (input_file.readline()).split(",")
	for i in range(len(w)):
		item = []
		item.append(int(w[i]))
		item.append(int(v[i]))
		item.append(int(c[i]))
		items.append(item)
	input_file.close()

def output(value, path):
	output_file.write(str(value)+'\n')
	result = [0]*len(items)
	result_str = ""
	for i in range(len(path)):
		result[path[i]] = 1

	for i in range(len(result)-1):
		result_str += str(result[i]) + ", "
	result_str += str(result[len(result)-1])

	output_file.writelines(result_str)

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
	for i in range(len(items)):
		node.append(i)

	while (node!=[]):
		current_path.append(node.pop())
		last = current_path[len(current_path)-1]
		for i in range(len(items)-last-1):
			node.append(i+last+1)
		if ((checkWeight(items, current_path) == False) ):
			while ((len(current_path)>0) and (len(node)>0) and (current_path[-1]<node[-1])):
				node.pop()
			while ((len(current_path)>0) and (len(node)>0) and (current_path[-1]>node[-1])):
				current_path.pop()
			continue
		s=calculate_value(items, current_path)
		if ((s>final_bound) and (isSatisfied(items, current_path, group))):
			final_path=[]
			for i in range(len(current_path)):
				final_path.append(current_path[i])
			final_bound = s
		if (last==len(items)-1):
			while ((len(current_path)>0) and (len(node)>0) and (current_path[-1]>node[-1])):
				current_path.pop()
	output(final_bound,final_path)

if __name__ == '__main__':
	input()
	output_file = open("output/OUTPUT.txt", "w")
	knapsack(items)
	output_file.close()