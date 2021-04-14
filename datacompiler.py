# Definitions:
# Master Test Item IDs - the unified test ids coming from the master specification
# Master Test Item Names - the unified test names coming from the master specification
# Specific Test System Item IDs - the unique implementation test ids coming from each test system
# Specific Test System Item Names - the unique implementation test names coming from each test system

# Intended final datastructure for databaseResults
# databaseIDs => {ID#_of_master: [{Specific System#: ID#, Specific System#: ID#, ...}, 'Unified_Name'], ...}
# databaseResults => Specific System # - {ID#: Result, ID#: Result, ...}; Specific System # - {ID#: Result, ID#: Result, ...} ...

# Import necessary libraries for accessing local file system
import os

# Obtain the current working directory
cwd = os.getcwd()

# Obtain all files in test directory, use \\ such that file path is not interpreted as escape characters
files = os.listdir(cwd)

# Add the files in the subdirectories
subfilesTestItems = os.listdir(cwd+"\Test_Items")
for each in subfilesTestItems:
    files.append(cwd+"\Test_Items"+"\\"+each)

subfilesTestResults = os.listdir(cwd+"\Test_Results")
for each in subfilesTestResults:
    files.append(cwd+"\Test_Results"+"\\"+each)

print(files)

# Create possible test result choices
# This could be any categorical information
# Examples: T/F results, P/F results, Selection choices, etc.
testResultOptions = ["True", "False"]

# Create an empty list and add only .txt files to it
fileList = []
for each in files:
    if "txt" in each:
        fileList.append(each)

# Load the master input file into memory
for each in fileList:
    if "masterinputtestitems" in each.lower():
        with open(each, 'r') as f:
            masterFile = f.read()

# Create a master item id list
masterItemId = []
# Create a master item name list
masterItemName = []

# Find all the test item info in the master file
while (len(masterFile) != 0):
    # Define the end position of a line by finding the newline character
    new = masterFile.find("\n")
    if (new != -1):
        # Check to see if an ID field is contained on that line
        pos = masterFile[:new].find(":")
        if (pos != -1):
            # If an ID field exists, add the Id and Name to their respective lists
            masterItemId.append(masterFile[:pos])
            masterItemName.append(masterFile[pos+2:new])
            # Update the search position in the file
            masterFile = masterFile[new + 1:]
        else:
            # If an ID field does not exist, skip that line and update the search position in the file
            masterFile = masterFile[new + 1:]
    else:
        # When no more newlines are found, the file is empty and no more logic needs to be performed
        masterFile = ""

# Write a master file of all test ids with their names
with open(cwd + "\\MasterItemList.txt", "w") as f:
    for num in range(len(masterItemId)):
        f.write(masterItemId[num])
        f.write(": ")
        f.write(masterItemName[num])
        f.write("\n")

# Create a list of all of the specific test system item info files
specificTestItemList = []

for each in files:
    if ("system" in each.lower() and "items" in each.lower() and not "specificitemlist" in each.lower()):
        # Add an empty array for each specific test id set
        print(each)
        specificTestItemList.append(each)

# Create a specific item id dictionary
specificTestItemIds = {}

for each in specificTestItemList:

    testSystemName = each[len(cwd+"\Test_Items")+1:each.find(".txt")]
    
    # Add another special test id to the dictionary
	# the testSystemName is simply the name of the file that describes the test system ids
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

print(specificTestItemIds)

with open(cwd + "\\SpecificItemList.txt", "w") as f:
    for testSystem, testIds in specificTestItemIds.items():
        f.write(testSystem)
        f.write("\n")
        for each in testIds:
            f.write(each)
            f.write("\n")

#print(masterItemId)
#print(specificTestItemIds)

masterItemIdList = []
masterItemNameList = []


for each in masterItemId:
    #print("Master Item ID:")
    #print(each[:each.find("ID")+3])
    masterItemIdList.append(each[:each.find("ID")+3])
    #print("Master Item Test Name:")
    #print(each[each.find(":")+2:])
    masterItemNameList.append(each[each.find(":")+2:])

    for key , value in specificTestItemIds.items():
        for every in value:
            if (every[:every.find("ID")+3] == each[:each.find("ID")+3]):
                None
                #print(key + " Test Name:")
                #print(every[every.find(":")+2:])

    #print("\n")

# Create an array of all of the specific test items
specificTestSystems = []

print("specificTestItemList")
print(specificTestItemList)

for each in specificTestItemList:
    specificTestSystems.append(each[each.find("System")+len("System"):each.find("System")+len("System")+1])

print("specificTestSystems")
print(specificTestSystems)
#print(fileList)
#print(specificTestSystems)

databaseResults = {}

#print("masterItemId")
#print(masterItemId)
#print(masterItemIdList)

# Create a unified table of test results from all test systems
# Loop through each test system

#print("SpecificTestSystems:::::")
#print(specificTestSystems)

for each in fileList:
    # Loop through each of the test systems
    for every in specificTestSystems:
        #print(each.lower())
        #print(every)
        if ("system" + every.lower() in each.lower() and "result" in each.lower()):
            systemResultName = "System " + every + " Results"
            #print("here")
            #print(databaseResults)
            databaseResults[systemResultName] = {}
            with open(each, 'r') as f:
                testResult = f.read()
                #print("Test Result")
                #print(testResult)

            for id in masterItemIdList:
                #print(every)
                #print(id)
                #print(every)
                #print(id)
                result = testResult[testResult.find(id):][testResult[testResult.find(id):].find(id)+5:testResult[testResult.find(id):].find("\n")-1]
                if (result in testResultOptions):
                    databaseResults[systemResultName][id] = testResult[testResult.find(id):][testResult[testResult.find(id):].find(id)+5:testResult[testResult.find(id):].find("\n")-1]
            #print(testResult)

# Write unified set of results
with open(cwd + "\\Data_Compiled\\DatabaseResults.txt", "w") as f:
    #print(databaseResults)
    # Print out master table
    for keyA, valueA in databaseResults.items():
        print(keyA)
        f.write(keyA)
        f.write("\n")
        print(valueA)
        counter = len(valueA)
        for keyB, valueB in valueA.items():
            f.write(keyB)
            f.write(": ")
            f.write(valueB)
            counter -= 1
            if (counter != 0):
                f.write(", ")
            else:
                f.write("\n")
