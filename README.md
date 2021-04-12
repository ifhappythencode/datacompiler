#### datacompiler project

##### The purpose of the datacompiler project is to be able quickly map a set of test ids to their test results
##### This is accomplished by creating a local database of master and specific test items...
##### ...and then iterating through a set of test results to compile the data

##### The required python knowledge needed to implement the datacompiler includes the follows elements:
##### `import` statements to include necessary libraries including `os` for handling file name inputation
##### use of `with open(filename, 'r') as f` to read in existing files
###### (Note: this structure will close the file automatically after completion)
##### use of `with open(filename, 'w') as f` to write to new files
###### (Note: this structure will close the file automatically after completiion)
##### `f.read()` to extract information from a file and place into as a string variable

##### use of python lists `[]` for handling array operations

##### use of `list.append(item)` to add items incrementally to an array

##### use of `for each in list` to iteration through a list

##### use of `if item in list` to check to see if a substring is included in a string

##### use of `list.find(item)` to find the position of the matched string
###### (Note: the purpose of finding the item location is associate a result field with a test item id tag)
###### Example: `Item1: Result1` -- if we can find the location of the `Item1` tag, we now can search proximally to identify `Result1`

##### user of python dictionaries `{}` to keep insert and keep track of mapping the master ids to the specific test system ids
###### (Note: the dictionary is also used as a data structure to collate the test results
