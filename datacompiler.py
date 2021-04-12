# Definitions:
# Master Test Item IDs - the unified test ids coming from the master specification
# Specific Test System Item IDs - the unique implementation test ids coming from each of the implementers

# Find files in a directory
#
# -- Python needed for this step:
#
# -- -- Importing OS commands
import os
# Important to use \\ such that file path is not interpreted as escape characters
files = os.listdir("C:\\Users\\PC\\Desktop\\Python Programs Written\\DataCompiler")

# Create an empty list
fileList = []

# Prune the list to only include files with extension *.txt
for each in files:
    if "txt" in each:
        fileList.append(each)

# Create / load in an index of universal test item ids and names
#
# -- Python needed for this step:
#
# -- -- List / Array
# -- -- Format: [item1, item2, item3]
#
# -- -- Input Box
# -- -- Format: input()
#
# -- -- File / Local Database
# -- -- Format: with open(filename, 'r') as f:
# -- -- Format: with open(filename, 'w') as f:


# Find the master test item id file
masterFile = []

for each in fileList:
    if "master" in each.lower():
        with open(each, 'r') as f:
            masterFile = f.read()

# Create a master item id list
masterItemId = []

# Find all the test item ids in the master file
while (len(masterFile) != 0):
    # Define the end position of a line by finding the newline character
    new = masterFile.find("\n")
    if (new != -1):
        # Check to see if an ID field is contained on that line
        pos = masterFile[:new].find("ID")
        if (pos != -1):
            # If an ID field exists, add it to the master item list
            masterItemId.append(masterFile[pos:new])
            # Update the search position in the file
            masterFile = masterFile[new + 1:]
        else:
            # If an ID field does not exist, skip that line and update the search position in the file
            masterFile = masterFile[new + 1:]
    else:
        # When no more newlines are found, the file is empty and no more logic needs to be performed
        masterFile = ""

# Write a master file of all test ids

with open("C:\\Users\\PC\\Desktop\\Python Programs Written\\DataCompiler\\MasterItemList.txt", "w") as f:
    for each in masterItemId:
        f.write(each)
        f.write("\n")

# Create a specific test item id list
specificTestItemList = []

for each in files:
    if "specific" in each.lower():
        # Add an empty array for each specific test id set
        specificTestItemList.append(each)

if "SpecificItemList.txt" in specificTestItemList:
    specificTestItemList.remove("SpecificItemList.txt")


# Create a specific item id dictionary
specificTestItemIds = {}

for each in specificTestItemList:

    testSystemName = each[:each.find(".txt")]
    
    # Add another special test id to the dictionary
    specificTestItemIds[testSystemName] = []
    
    with open(each, 'r') as f:
        specificFile = f.read()
    # Find all the test item ids in each file
    while (len(specificFile) != 0):
        # Define the end position of a line by finding the newline character
        new = specificFile.find("\n")
        if (new != -1):
            # Check to see if an ID field is contained on that line
            pos = specificFile[:new].find("ID")
            if (pos != -1):
                # If an ID field exists, add it to the specific item ID list
                specificTestItemIds[testSystemName].append(specificFile[pos:new])
                # Update the search position in the file
                specificFile = specificFile[new + 1:]
            else:
                # If an ID field does not exist, skip that line and update the search position in the file
                specificFile = specificFile[new + 1:]
        else:
            # When no more newlines are found, the file is empty and no more logic needs to be performed
            specificFile = ""


# Write a specific test system file of all test ids

with open("C:\\Users\\PC\\Desktop\\Python Programs Written\\DataCompiler\\SpecificItemList.txt", "w") as f:
    for testSystem, testIds in specificTestItemIds.items():
        f.write(testSystem)
        f.write("\n")
        for each in testIds:
            f.write(each)
            f.write("\n")






#print(masterItemId)
#print(specificTestItemIds)

for each in masterItemId:
    print("Master Item ID:")
    print(each[:each.find("ID")+3])
    print("Master Item Test Name:")
    print(each[each.find(":")+2:])

    for key , value in specificTestItemIds.items():
        for every in value:
            if (every[:every.find("ID")+3] == each[:each.find("ID")+3]):
                print(key + " Test Name:")
                print(every[every.find(":")+2:])

    print("\n")



for each in fileList:
    if "sampledata" in each.lower():
        with open(each, 'r') as f:
            masterFile = f.read()


        

        
# -- Material needed for this step:
# -- -- Documentation: Names of test item ids, categorized by test type
# -- -- Documentation: Names of test item names, corrseponding to ids

# Create an index of specific test system ids and names
# -- Python needed for this step:
# -- -- List / Array

# Determine file names

# Loop through each of the files

# Add cases to a set of items to look for

# Read in the text in the file

# Find the position of the 'key'

# Search a substring of the text, starting at the position of the key

# Find a 'value' from a list of possible choices

# Create a unified table of test results from all test systems


