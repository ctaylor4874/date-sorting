import re

list_of_dates = [
    'Oct 7, 2009',
    'Nov 10, 2009',
    'Jan 10, 2009',
    'Oct 22, 2009',
    'Dec 10, 2008',
    'Mar 25, 2014',
    'Mar 24, 2014',
    'Mar 23, 2014',
    'Mar 23, 2013',
    'Mar 23, 2015'
]
month_strings = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def month_to_num(m):
    """
    Converts month abbreviation to integers, and month integers into month abbreviations.

    :param m: Month; either string or integer type
    :return: If month passed in was an int, return string.  If month passed in was a string, return int.
    """
    if type(m) == str:
        return dict(zip(month_strings, month_ints))[m]
    return dict(zip(month_ints, month_strings))[m]


# Remove comma from list item string
def strip_comma(l):
    return map(lambda x: re.sub(',', '', x), l)


# Create a list of dictionaries for each date, this is easier to work with
def make_list_of_dictionaries(l):
    tmp_list = []
    for s in l:
        string = s.split(' ')
        tmp_list.append(dict({
            'month': month_to_num(string[0]),
            'day': '{},'.format(string[1]),
            'year': int(string[2])
        }))
    return tmp_list


# Sort the list of dictionaries by year, month, then day
def sort_dates(l):
    sort = sorted(l, key=lambda x: (x['year'], int(x['month']), x['day']), reverse=True)
    return sort


# If the key for the item is 'month', convert the value back to it's abbreviation.
# Join the dictionaries back into a list of strings
def make_new_list(l):
    dates = list(
        ' '.join((str(month_to_num(v)) if k == 'month' else str(v)) for k, v in s.items()) for s in l)
    return dates


if __name__ == '__main__':
    stripped_list = strip_comma(list_of_dates)
    list_dicts = make_list_of_dictionaries(stripped_list)
    sorted_dates = sort_dates(list_dicts)
    list_of_dates = make_new_list(sorted_dates)

    print list_of_dates
