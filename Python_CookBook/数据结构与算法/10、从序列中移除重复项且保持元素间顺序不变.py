"""
去除重复元素，保持剩下的元素顺序不变
"""


# 如果序列中的值是可哈希的，可以通过集合和生成器来完成
def deque(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


# 如果想在不可哈希对象序列中去除重复项
def deque(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield val
            seen.add(item)
