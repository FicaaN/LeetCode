class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined_list = list(zip(heights, names))
        combined_list.sort(key=lambda x : x[0], reverse=True)
        sorted_names = [name for height, name in combined_list]
        return sorted_names