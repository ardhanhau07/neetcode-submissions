class Solution:

  def hasDuplicate(self, nums: List[int]) -> bool:
    seen = set()
    for num in nums:
      if num in seen:
        return True
      seen.add(num)
    return False


def main():
  nums = [1, 2, 3, 3]
  print(Solution().hasDuplicate(nums))

if __name__ == "__main__":
  main()