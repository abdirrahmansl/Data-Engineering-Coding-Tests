# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


# [TODO]: fix the function
def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    list_of_nums = time_str.split(":")
    
    return sum(int(num) for num in list_of_nums)




def test_sum_of_current_time():
    time = '01:02:03'
    res = sum_current_time(time)
    assert res == 7

if __name__=="__main__":

    

    try:
        test_sum_of_current_time()
    except Exception:
        print("Incorrect summation.")