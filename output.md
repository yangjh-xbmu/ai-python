## 如何访问Series中的数据？

你可以通过索引访问Series中的数据：

```python
# 访问第一个元素
print(s[0])  # 输出: 1

# 访问第三个元素
print(s[2])  # 输出: 5
```

## 如何修改Series中的数据？

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