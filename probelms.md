# Arrays and Hashing

<details> <summary>Contains Duplicate</summary>

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
```

OR

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in nums:
            if i not in a:
                a.add(i)
                continue
            return True
        return False
```

</details>

<details><summary>Valid Anagram</summary><br/>

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

OR

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
```

</details>

<details><summary>2 Sum</summary><br/>

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            if (target - nums[i]) not in a:
                a[nums[i]] = i
            else:
                return [a[target - nums[i]], i]
```

</details>

<details><summary>Group Anagram</summary><br/>

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)
        for s in strs:
            grp[tuple(sorted(s))].append(s)
        return list(grp.values())
```

</details>

<details><summary>Top k frequent elements</summary><br/>

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
        return [x[i][0] for i in range(k)]
```

</details>

<details><summary>Product of Array Except Self</summary><br/>

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        prefix = 1
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
```

</details>

<details><summary>Valid Sudoku</summary><br/>

```python
class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                key = board[r][c]
                if key == '.':
                    continue
                if (key in rows[r] or key in cols[c]
                        or key in squares[r // 3, c // 3]):
                    return False

                rows[r].add(key)
                cols[c].add(key)
                squares[r // 3, c // 3].add(key)

        return True
```

</details>

<details><summary>Longest consecutive sequence</summary><br/>

```python
class Solution:

    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        numset = sorted(set(nums))
        longest = 0
        temp = 1
        never_ran = True
        for i, v in enumerate(numset[:-1]):
            never_ran = True
            if v == numset[i + 1] - 1:
                temp += 1
                continue
            longest = max(longest, temp)
            never_ran = False
            temp = 1
        if never_ran:
            longest = max(longest, temp)
        return longest
```

</details>

<details><summary>2Sum Sorted</summary><br/>

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            cursum = numbers[l] + numbers[r]

            if cursum > target:
                r -= 1
            elif cursum < target:
                l += 1
            else:
                return [l+1, r+1]
        return []

```

</details>

<details><summary>Group Anagram</summary><br/>

</details>

<details><summary>Group Anagram</summary><br/>

</details>

<details><summary>Group Anagram</summary><br/>

</details>

<details><summary>Group Anagram</summary><br/>

</details>

<details><summary>Group Anagram</summary><br/>

</details>

<details><summary>Group Anagram</summary><br/>

</details>

<details><summary>Group Anagram</summary><br/>

</details>

<details><summary>Group Anagram</summary><br/>

</details>

<details><summary>Group Anagram</summary><br/>

</details>

<details><summary>Group Anagram</summary><br/>

</details>

<details><summary>Group Anagram</summary><br/>

</details>

<details><summary>Group Anagram</summary><br/>

</details>
