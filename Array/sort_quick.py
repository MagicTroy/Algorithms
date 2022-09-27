__description__ =  'This is in-place quick sort'
__arthor__ =  'Sixun Ouyang'
__git__ = 'https://github.com/MagicTroy'


def swap(the_list, left, right):
    the_list[left], the_list[right] = the_list[right], the_list[left]

def partition(the_list, left, right):
    key = the_list[left]
    while left < right:
        while left < right and key <= the_list[right]:
            right -= 1
        # if we find right value is smaller than the key value
        # or left == right, we swap
        swap(the_list=the_list, left=left, right=right)
        
        while left < right and key >= the_list[left]:
            left += 1
        # if we find left value if greater than the key value
        # or left == right, we swap
        swap(the_list=the_list, left=left, right=right)
        
    # return left as piviot
    return left

def quick_sort(the_list, left, right):
    if left >= right:
        return
    else:
        piviot = partition(the_list=the_list, left=left, right=right)
        quick_sort(the_list=the_list, left=left, right=piviot - 1)
        quick_sort(the_list=the_list, left=piviot + 1, right=right)
        
l = [1, 20, 3, 50, 40, 70, 23, 100, 23, 88]
quick_sort(l)
print(l)
