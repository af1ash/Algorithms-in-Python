# 递归
import os
# factorial function 阶乘


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# English ruler


def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length (followed by optional label)"""
    line = '-' * tick_length
    if tick_label:
        line += " " + tick_label
    print(line)


def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length"""
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))
# Binary search


def binary_search(data, target, low, high):
    """
    Return True if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)
# file system


def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents."""
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total), path)
    return total


if __name__ == "__main__":
    print(factorial(4))
    draw_ruler(2, 3)
    print(binary_search([2, 4, 5, 7, 8, 9, 12, 14,
                         17, 19, 22, 25, 27, 28, 33, 37], 22, 0, 15))
    disk_usage('f:\\学习\\Python\\')
