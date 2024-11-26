# Data Structures and Algorithms

Data Structures and Algorithms with their design, analysis, and applications in real-life scenarios.

## Introduction

To start off, I would like to iterate on coding as a subset of programming. The topic of data structures and algorithms is integral to programming, yet often underemphasized. We should write good code, not just any type of code. Studying them helps improve our coding practices.

!!majorly these repository is greatly influenced and a product of reading CLRS!!

![alt text](images/image.png)

## So what are they:
### Data structures
    These are ways to store data for easy access and modifications. 

### Algorithms
    an algorithm is any well defined computational procedure that takes
    some value, or set of values, as input and produces some value, or set of values, as
    output in a finite amount of time.

WOW! so some input, then the input goes through a well computational procedure and then 
some output but this must take place in a finite amount of time.

So key points is memory (for the data in the algorithm) and time.

## Considering a common LeetCode problem (Two Sum)

### Python
```python
    class Solution:
        def two_sum(nums, target):
            for i in range(len(nums)):
                for j in range(i):
                    if nums[i] + nums[j] == target:
                        return [i, j]
```
### C++
```c++
    class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            for (int i = 0; i < nums.size(); ++i) {
                for (int j = 0; j < i; ++j) {
                    if (nums[i] + nums[j] == target) {
                        return {i, j}; 
                    }
                }
            }
            return {}; 
        }
    };
```

The above code achieves the same thing, solving a classic problem in LeetCode, no. 1 known as Two Sum. But I am not here to explain LeetCode or the solution. I do research on algorithms and data structures and their analysis. While the above codes run well, they apply nested loops. The loops overall, using a common analysis way of Big O notation, are O(n^2). That's expensive on runtime:

- Runtime affects user experience; applications that take longer to run are not preferred.
- It also affects scalability; imagine running the above code on large (humongous) datasets.
- Unnecessary resource usage (processors in computers), hence also high cost. Even in cloud setups, runtime is accounted for, so one can pay unnecessary money for such.

A resource on BIG OH notation:
https://en.wikipedia.org/wiki/Big_O_notation

But there is a clever way to solve the above problem, but before that, we notice that
the solutions use a complex quadratic runtime but utilise no data structure, so that solution 
is very good in memory but bad in runtime. It is what problem solvers call a *Brute force solution*
meaning that we focus on solving the problem and getting the results not giving a consideration on 
factors like memory and runtime.

### Soln 2: Using a data structure and a well laid out plan(algorithm)
### Python
```python
    class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_set:
                return [hash_set[complement], i]
            else:
                hash_set[num] = i

```
### C++
```c++
#include <unordered_map>
#include <vector>

std::vector<int> twoSum(const std::vector<int>& nums, int target) {
    std::unordered_map<int, int> hashmap; 
    for (int i = 0; i < nums.size(); ++i) {
        int complement = target - nums[i]; 
        if (hashmap.find(complement) != hashmap.end()) {
            return {hashmap[complement], i}; 
        }
        hashmap[nums[i]] = i; 
    }
    return {}; 
}

```
The above solutions are the same except the language. But in overall they are efficient 
for the problem as their runtime is O(n) for the single loop being superior in runtime and the 
memory now accounted for by the hashmap is constant O(1) since we only need the memory of the 
hashmap only which is contant for the problem. RUNTIME is saved and memory is 
used well. Our program indeed saves a lot and is very efficient.

Later in detail, I will demonstrate the uses of the hashmap and we will see its relevance in our 
algorithm. 

With that I have demonstrated the importance of the concepts foundational to computer science which are data structures and algorithms with their design and analysis.

A resource just demonstrating big o notation simply.
![alt text](images/image2.png)
