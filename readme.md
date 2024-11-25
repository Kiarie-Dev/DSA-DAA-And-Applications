# Data Structures and Algorithms

Data Structures and Algorithms with their design, analysis, and applications in real-life scenarios.

## Introduction

To start off, I would like to iterate on coding a subset of programming. It is not emphasized enough that the topic of 
data structures and algorithms is integral to it. We should write good code, not just any type of code. And the studying
the latter helps in so.

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

## considering a common leetcode problem (two sum)

### python 
'''python
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                return [i, j]
### c++
'''c++
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
