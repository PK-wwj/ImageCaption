import h5py

for i in range(101,201):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            print(i)

'''以上代码中，我们首先使用h5py.File函数打开H5文件，'r'表示以只读方式打开文件。
然后，通过索引访问数据集，获取到一个dataset对象。
最后，我们可以通过切片操作dataset[:]来读取数据集中的所有数据，返回的结果是一个NumPy数组。
'''