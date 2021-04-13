#### *datacompiler project*

*The purpose of this project is to be able quickly compile a set of test results.
This is accomplished by creating a local database of master and specific test items,
and then iterating through a set of test results to compile the data.*

##### Goals
The primary goals of the program are the following:
 - [x] Provide an easy method for the user to add new test items
 - [x] Keep track of test item ids
 - [x] Allow for easy selection of test results
 - [x] Provide clean format of compared test result summary

##### Python Knowledge
The required python knowledge needed to implement the datacompiler includes the follows elements:
 - import statements
 - file io
 - lists
 - dictionaries
 - conditional loops (if, for, while)
 - find

##### Functional Syntax
- `import` statements to include necessary libraries including `os` for handling file name inputation
 
- `with open(filename, 'r') as f` to read in existing files
  - Note: this structure will close the file automatically after completion

- `with open(filename, 'w') as f` to write to new files
  - Note: this structure will close the file automatically after completiion

- `f.read()` to extract information from a file and place into as a string variable

- `[]` for defining and creating lists of test ids

- `list.append(item)` to add items incrementally to an array

- `for each in list` to iteration through a list

- `if item in list` to check to see if a substring is included in a string

- `list.find(item)` to find the position of the matched string
  - Note: the purpose of finding the item location is associate a result field with a test item id tag
  - Example: `Item1: Result1` -- if we can find the location of the `Item1` tag, we now can search proximally to identify `Result1`

- dictionaries `{}` to keep insert and keep track of mapping the master ids to the specific test system ids
  - Note: the dictionary is also used as a data structure to collate the test results


###### Additional information and inspiration provided by [W3Schools](https://www.w3schools.com/python/)

