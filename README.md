# Data Engineering Interview Tests

This repository contains former tests used at interview by the Ministry of Justice Data Engineering team. This repo will be maintained over time with the addition of new coding tests once recruitment rounds end. Each test will have a README that explains the conditions each test would be taken under (time, coding languages, etc.).


## Usage 

In test_1 is_log_line function takes lines from the sample.log and returns true if the date is in the correct format, else none is returned. The get_dict function also takes a line and returns a dictionary formatted with appropriate keys.
```python
def is_log_line(line):
    try:
        date = datetime.datetime.strptime(str(line[0:17]), '%d/%m/%y %H:%M:%S')
        return True
    except ValueError as err:
        return None
```
```python
def get_dict(line):
    if is_log_line(line):
        red = line.split()
        return {"timestamp":red[0] +" "+ red[1], "log_level":red[2], "message":' '.join(red[3:])}
```

In test_2 the CSV file is read, iterated through. Postcode is used to fetch data from www.find-court-tribunal.service.gov.uk. Relevant data is extracted and then formated to being written into a csv file.

To run call: 
```python
python3 test_2.py 
```

In test_3 the sum_current_time function takes a string input of the time and returns the sum of the hours, minutes and seconds. 
```python
def sum_current_time(time_str: str) -> int:
    list_of_nums = time_str.split(":")
    
    return sum(int(num) for num in list_of_nums)
```