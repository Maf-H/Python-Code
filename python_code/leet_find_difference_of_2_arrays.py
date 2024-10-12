def find_difference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    """_summary_

    Args:
        nums1 (list[int]): _description_
        nums2 (list[int]): _description_

    Returns:
        list[list[int]]: _description_
    """
    return [list(set(nums1)-set(nums2)),list(set(nums2)-set(nums1))]
    # num_dict = {0:set(), 1:set()}
    # for i in set(nums1):
    #     if i not in set(nums2):
    #         num_dict[0].add(i)
    # for j in set(nums2):
    #     if j not in set(nums1):
    #         num_dict[1].add(j)

    # return [list(num_dict[0]),list(num_dict[1])]

nums1 = [1,2,3,4,5]
nums2 = [2,3,4,5,6]
print(find_difference(nums1, nums2))
nums1 = [1,2,2,3]
nums2 = [2,2,3,4]
print(find_difference(nums1, nums2))
# %%


# %%
