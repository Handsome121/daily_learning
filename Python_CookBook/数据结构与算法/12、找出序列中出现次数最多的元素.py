"""
找出出现次数最多的元素
"""
from collections import Counter

word_counts = Counter()
top_three = word_counts.most_common(3)
print(top_three)

