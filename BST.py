def insert_bst(x, n):
	if x == n[0]:
		return n

	elif x < n[0]:
		if not n[1]:
			return (n[0], (x, (), ()), n[2])
		else:
			return (n[0], insert_bst(x, n[1]), n[2])

	elif x > n[0]:
		if not n[2]:
			return (n[0], n[1], (x, (), ()))
		else:
			return (n[0], n[1], insert_bst(x, n[2]))


tree = (8, (7, (), ()), (9, (), ()))


print (insert_bst(3, tree))


for i in range(100):
	tree = insert_bst(i, tree)

print(tree)