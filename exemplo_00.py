from utils_log import log_decorator
from time_decorator import time_measure_decorator


# @log_decorator
@time_measure_decorator
def sum_elements(x, y):
    result = x + y
    return result
    

sum_elements(2, 3)
# sum_elements(2, '3')
sum_elements(2, 10)
