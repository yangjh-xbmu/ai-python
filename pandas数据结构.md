### Pandas教学内容：针对初学者的基础教程

#### 2. **Pandas的基本数据结构**

##### 2.1 **Series**：一维数组，类似于带标签的数组

###### 2.1.1 创建Series

首先，我们需要了解什么是Series。Series是Pandas中的一种基本数据结构，类似于一维数组，但它有一个额外的特性：每个元素都有一个标签（也称为索引）。

```python
import pandas as pd

# 创建一个简单的Series
s = pd.Series([1, 3, 5, 7, 9])
print(s)
```

输出结果：

```
0    1
1    3
2    5
3    7
4    9
dtype: int64
```

在这个例子中，`0, 1, 2, 3, 4` 是默认的索引，`1, 3, 5, 7, 9` 是Series中的数据。

###### 2.1.2 访问和修改Series中的数据

你可以通过索引访问Series中的数据：

```python
# 访问第一个元素
print(s[0])  # 输出: 1

# 访问第三个元素
print(s[2])  # 输出: 5
```

你也可以通过索引修改Series中的数据：

```python
# 修改第一个元素
s[0] = 10
print(s)
```

输出结果：

```
0    10
1     3
2     5
3     7
4     9
dtype: int64
```

###### 2.1.3 Series的基本操作（如索引、切片、过滤）

- **索引**：你可以使用标签（索引）来访问Series中的数据。

```python
# 创建一个带有自定义索引的Series
s = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])
print(s)

# 访问索引为'c'的元素
print(s['c'])  # 输出: 5
```

- **切片**：你可以使用切片来获取Series中的一部分数据。

```python
# 获取索引为'b'到'd'之间的元素
print(s['b':'d'])
```

输出结果：

```
b    3
c    5
d    7
dtype: int64
```

- **过滤**：你可以使用条件过滤来获取满足特定条件的元素。

```python
# 获取大于5的元素
print(s[s > 5])
```

输出结果：

```
d    7
e    9
dtype: int64
```

##### 2.2 **DataFrame**：二维表格，类似于Excel表格

###### 2.2.1 创建DataFrame

DataFrame是Pandas中另一种基本数据结构，类似于二维表格，可以看作是Series的集合。

```python
# 创建一个简单的DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
```

输出结果：

```
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
```

###### 2.2.2 访问和修改DataFrame中的数据

你可以通过列名访问DataFrame中的数据：

```python
# 访问'Name'列
print(df['Name'])
```

输出结果：

```
0      Alice
1        Bob
2    Charlie
Name: Name, dtype: object
```

你也可以通过行索引访问DataFrame中的数据：

```python
# 访问第一行
print(df.loc[0])
```

输出结果：

```
Name        Alice
Age            25
City     New York
Name: 0, dtype: object
```

你还可以修改DataFrame中的数据：

```python
# 修改'Age'列的第一个元素
df.loc[0, 'Age'] = 26
print(df)
```

输出结果：

```
      Name  Age         City
0    Alice   26     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
```

###### 2.2.3 DataFrame的基本操作（如索引、切片、过滤）

- **索引**：你可以使用列名或行索引来访问DataFrame中的数据。

```python
# 访问'Name'列
print(df['Name'])

# 访问第一行
print(df.loc[0])
```

- **切片**：你可以使用切片来获取DataFrame中的一部分数据。

```python
# 获取前两行
print(df.loc[0:1])
```

输出结果：

```
    Name  Age         City
0  Alice   26     New York
1    Bob   30  Los Angeles
```

- **过滤**：你可以使用条件过滤来获取满足特定条件的行。

```python
# 获取年龄大于30的行
print(df[df['Age'] > 30])
```

输出结果：

```
      Name  Age     City
2  Charlie   35  Chicago
```

### 总结

通过以上内容，你应该对Pandas的基本数据结构Series和DataFrame有了初步的了解。接下来，你可以尝试自己创建一些Series和DataFrame，并进行一些基本的操作，如访问、修改、切片和过滤。随着你逐渐熟悉这些操作，你可以进一步学习Pandas中的更多高级功能。
