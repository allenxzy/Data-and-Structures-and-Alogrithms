#-*-coding: utf-8-*-
#改进5.5代码的插入实现方法，达到插入元素是在操作过程中移动到其最终位置，从而避免了随后转移
def insert(self, k, value):
    if self._n == self._capacity:
        self._resize(2 * self._capacity)
    for j in range(self._n, k, -1):
        self._A[j] = self._A[j - 1]
    self._A[k] = value
    self._n += 1
