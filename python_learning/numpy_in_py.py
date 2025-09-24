import numpy as np

n1 = np.array([
    [10,20,30,40,50],
    [70,80,30,40,50]
]
)

# print(n1)

n2 = np.zeros((5,5))
n3 = np.full((4,8),6)
n4 = np.arange(10,20)
n5 = np.arange(10,20,6)
n6 = np.random.randint(1,100,20)


# print(n6)
# print(n1.shape)

n1.shape = (5,2)

# print(n1)



n7 = np.array([10,20,30])
n8 = np.array([40,50,60])

# print(np.vstack((n7,n8)))
# print(np.hstack((n7,n8)))
# print(np.column_stack((n7,n8)))


# print(np.intersect1d(n7,n8))
# print(np.setdiff1d(n7,n8))
# print(np.setdiff1d(n8,n7))


# print(np.sum([n7,n8]))
# print(np.sum([n7,n8], axis=0)) # col add
# print(np.sum([n7,n8], axis=1)) # row add


n7=n7+1
# n7=n7-1
# n7=n7*1
# n7=n7/1

# print(n7)


n9 = np.array([
    [10,20,30,40,50],
    [70,80,30,40,50],    
    [40,30,90,80,70]    

]
)
# print(n9[1])
# print(n9[:,2])

# print(n9.transpose())

# print(n7.dot(n8))


np.save("my_numpy", n9)

n10 = np.load("my_numpy.npy")
print(n10)