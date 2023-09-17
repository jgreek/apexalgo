class ProductExceptSelf:

    def __init__(self, nums):
        self.nums = nums
        self.res = [1] * len(nums)

    def _left_products(self):
        prefix = 1
        for i in range(len(self.nums)):
            self.res[i] *= prefix
            prefix *= self.nums[i]

    def _right_products(self):
        postfix = 1
        for i in range(len(self.nums) - 1, -1, -1):
            self.res[i] *= postfix
            postfix *= self.nums[i]

    def get_result(self):
        self._left_products()
        self._right_products()
        return self.res


# Test Cases
def test_product_except_self():
    solution = ProductExceptSelf([1, 2, 3, 4])
    assert solution.get_result() == [24, 12, 8, 6]

    solution = ProductExceptSelf([5, 6, 7])
    assert solution.get_result() == [42, 35, 30]

    solution = ProductExceptSelf([0, 0, 0])
    assert solution.get_result() == [0, 0, 0]

    solution = ProductExceptSelf([0, 4, 5])
    assert solution.get_result() == [20, 0, 0]

    print("All tests passed!")


test_product_except_self()
