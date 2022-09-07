# timetable.gbmc.ac.uk timetable parser
This function can parse timetable from timetable.gbmc.ac.uk and return list with dicts.  
Before using you need get your PHPSESSID after authing on timetable.gbmc.ac.uk via google oauth. You can found PHPSESSID in cookies.
After use code like this: 
```python
print(get_timetable("your_sessidd"))
```
And you will be get this:
```python
[
  {
     "day":"Tuesday 06 September",
     "subject":"EDEXCEL LEVEL 1/2 FIRST CERTIFICATE IN INFORMATION AND CREATIVE TECHNOLOGY",
     "lecturer":"staff detail is not available",
     "room":"Room detail is not available",
     "startTime":"10:15",
     "endTime":"11:30"
  }, 
  ...
]
```
