# Advent of Code 2020
My code for [Advent of Code 2020](https://adventofcode.com/).
   
## What did I learn so far?
### [Day 1: Report Repair](https://adventofcode.com/2020/day/1)
- [Convert list of string into list of int](https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int):
```python
def convert_list_str_to_int(list_str):
    return list(map(int, list_str))
```

### [Day 2: Password Philosophy](https://adventofcode.com/2020/day/2)
### [Day 3: Toboggan Trajectory](https://adventofcode.com/2020/day/3)

- [Read a text file in a 2d array](https://stackoverflow.com/questions/19056125/reading-a-file-into-a-multidimensional-array-with-python):
```python
>> def read_array(filename):
>>     with open(filename) as file:
>>         array2d = [[character for character in line.split()] for line in file]
>>     return array2d
```

### [Day 4: Passport Processing](https://adventofcode.com/2020/day/4)
- [Put a string separated by a ':' into a dictionary](https://stackoverflow.com/questions/186857/splitting-a-semicolon-separated-string-to-a-dictionary-in-python):
```python
>> def split_passport(passport):
>>     return dict(item.split(":") for item in passport.split(" "))

>> split_passport('iyr:2024 eyr:1974')
{'iyr': '2024', 'eyr': '1974'}
```

- [Filter a list with another list of boolean](https://stackoverflow.com/questions/18665873/filtering-a-list-based-on-a-list-of-booleans):
```python
>> from itertools import compress
>> list_a = [1, 2, 4, 6]
>> fil = [True, False, True, False]
>> list(compress(list_a, fil))
[1, 4]
```

### [Day 5: Binary Boarding](https://adventofcode.com/2020/day/5)
- [Convet a base-2 binary number string to int](https://stackoverflow.com/questions/8928240/convert-base-2-binary-number-string-to-int):
```python
>> int('11111111', base=2)
255
```
