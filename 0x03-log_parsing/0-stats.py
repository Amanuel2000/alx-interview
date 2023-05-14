#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:
"""


import sys

# store the count of all status codes in a dictionary
list_of_status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}
all_sizes = 0
count = 0  # keep count of the number lines counted
try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # check if the status code receive exists in the dictionary and
            # increment its count
            if status_code in list_of_status_codes.keys():
                list_of_status_codes[status_code] += 1

            # update total size
            all_sizes += file_size

            # update count of lines
            count += 1

        if count == 10:
            count = 0  # reset count
            print('File size: {}'.format(all_sizes))

            # print out status code counts
            for key, value in sorted(list_of_status_codes.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(all_sizes))
    for key, value in sorted(list_of_status_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))            