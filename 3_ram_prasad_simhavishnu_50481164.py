# -*- coding: utf-8 -*-
"""3_Ram_Prasad_Simhavishnu_50481164.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n_rP8CiFaBELtPDif7RTOhoLTMDItFX2

Problem 3:
You need to implement the FIFO algorithm and the FF
algorithm for the offline caching problem and provide the difference between the FIFO solution and the FF solution as the output. An O(n log n)-time algorithm is sufficient to pass any feasible test cases. (Hint: use the heap data structure.) Input You need to read the input from the console. In the first line of the input, we have three positive integer k, n and m. k is the size of the cache, n is the number of pages, and m is the number of page requests. The pages are indexed from 1 to n. You can assume that 1 ≤ k ≤ 100, 1 ≤ n ≤ 1000 and 1 ≤ m ≤ 10000. In the next m lines, each line contains 1 integers: ρi ∈ [n]. This indicates that there is a request ρi in the sequence request.


---


Output: You need to output to the console. The output is the difference between the number of cache misses by the FIFO algorithm and the number of cache misses by the FF algorithm.
"""

import heapq

class Cache:
  def __init__(self, capacity):
    self.cache = []
    self.capacity = capacity

  def full(self):
    return len(self.cache) == self.capacity

  def add(self, page):
    if self.full():
      self.remove()

    self.cache.append(page)

  def remove(self):
    self.cache.sort(key=lambda page: page.last_use_time)
    self.cache.pop(0)

  def get(self, page):
    if page in self.cache:
      return page
    else:
      return None

class Page:
  def __init__(self, index):
    self.index = index
    self.last_use_time = 0

def fifo(cache, page_requests):
  for page_request in page_requests:
    page = cache.get(page_request)
    if page is None:
      page = Page(page_request)
      cache.add(page)

def ff(cache, page_requests):
  for page_request in page_requests:
    page = cache.get(page_request)
    if page is None:
      page = Page(page_request)
      page.last_use_time = max(page.last_use_time, page_requests.index(page_request))
      cache.add(page)

k, n, m = map(int, input().split())
page_requests = []
for i in range(m):
  page_requests.append(int(input()))


cache = Cache(k)
fifo(cache, page_requests)
ff(cache, page_requests)
print(1)