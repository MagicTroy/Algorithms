__description__ =  'This is in-place insert sort'
__arthor__ =  'Sixun Ouyang'
__git__ = 'https://github.com/MagicTroy'


# insert sort
def swap(the_list, left, right):
    the_list[left], the_list[right] = the_list[right], the_list[left]

def compare_and_insert(the_list, piviot):
    # from pivoit to 0
    while piviot > 0:
        # if the piviot smaller than the previous one
        # just swap and continue
        if the_list[piviot] < the_list[piviot - 1]:
            swap(the_list=the_list, left=piviot - 1, right=piviot)
        # if teh pivoit equal or greater than the previous one
        # break
        else:
            break
        piviot -= 1

def insert_sort(the_list):
    for piviot in range(1, len(the_list)):
        compare_and_insert(the_list=the_list, piviot=piviot)
        print(the_list)


l = [1, 20, 3, 50, 40, 70, 23, 100, 23, 88]
insert_sort(l)
print(l)
