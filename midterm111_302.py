# Prompts the user for the number of Tests
# This function will include call(s) to the input function
# Keep prompting until the number is a positive integer.
# Returns the number of Tests
def getNumberOfTests():
    trees=0;
    while trees<=0 :
        trees=int(input("Enter the Positive Number of Tree"))
    return trees


# Prompts the user for the weight of Assignments
# This function will include call(s) to the input function
# Keep prompting until the number is a float >= 0 and <= 100
# Returns the weight of assignments
def getWeightOfAssignments():
    weights=-1
    while weights<0 or weights>100 :
        weights =float(input("Enter the Weights of Assignments (which is >=0 and <=100)"));
    return weights


# Prompts the user for the weight of Tests
# This function will include call(s) to the input function
# Keep prompting until the number is a float >= 0 and <= 100
# Returns the weight of Test
def getWeightOfTests():
    weights = -1
    while weights < 0 or weights > 100:
        weights = float(input("Enter the Weights of Tests (which is >=0 and <=100)"));
    return weights


# Prompts the user for the weight of the final
# This function will include call(s) to the input function
# Keep prompting until the number is a float >= 0 and <= 100
# Returns the weight of final
def getWeightOfFinal():
    weights = -1
    while weights < 0 or weights > 100:
        weights = float(input("Enter the Weights of Final (which is >=0 and <=100)"));
    return weights


# returns True if the sum of the 3 arguments is 100(%), False otherwise
# Assign the default values 40, 35, 25 to wAssign, wTest and wFinal respectively
def checkWeights(wAssign,wTest,wFinal):
    if wAssign+wTest+wFinal ==100 :
        return True
    else :
        return False


# calculate the numeric grade (https://www.wikihow.com/Calculate-Weighted-Average)
def calculateNumericGrade(AvgAssignments,AvgTests,final,wOfAssign,wOfTests,wFinal):
    return  AvgAssignments*(wOfAssign/100) + AvgTests*(wOfTests/100) + final*(wFinal/100)

# convert the numeric grade to a letter according to the conversion table
# in the course outline
def calculateAlphaGrade(numericGrade):
    if numericGrade >= 90 and numericGrade <= 100:
        return 'A+'
    elif numericGrade >= 85 and numericGrade <= 89:
        return 'A'
    elif numericGrade >= 80 and numericGrade <=84:
        return 'A-'
    elif numericGrade >= 77 and numericGrade <=79:
        return 'B+'
    elif numericGrade >= 73 and numericGrade <=76:
        return 'B'
    elif numericGrade >= 70 and numericGrade <=72:
        return 'B-'
    elif numericGrade >= 67 and numericGrade <=69:
        return 'C+'
    elif numericGrade >= 63 and numericGrade <=66:
        return 'C'
    elif numericGrade >= 60 and numericGrade <= 62:
        return 'C-'
    elif numericGrade >= 57 and numericGrade <= 59:
        return 'D+'
    elif numericGrade >= 53 and numericGrade <= 56:
        return 'D'
    elif numericGrade >= 50 and numericGrade <= 52:
        return 'D-'
    else:
        return 'F'


# Get the weight value of the assignments (call the appropriate function)
wAssignments= getWeightOfAssignments()

# Get the weight value of tests (call the appropriate function)
wTests=getWeightOfTests()

# Get the weight value of the final (call the appropriate function)
wFinal=getWeightOfFinal()

# Check the sum of weight values is 100 (call the appropriate function)
weights=checkWeights(wAssignments,wTests,wFinal)
if weights==100 :
    print("The Weights are 100%")



# Repeat the last four steps if weight is not equal to 100
if weights !=100 :
    # Get the weight value of the assignments (call the appropriate function)
    wAssignments = getWeightOfAssignments()

    # Get the weight value of tests (call the appropriate function)
    wTests = getWeightOfTests()

    # Get the weight value of the final (call the appropriate function)
    wFinal = getWeightOfFinal()

    # Check the sum of weight values is 100 (call the appropriate function)
    weights = checkWeights(wAssignments, wTests, wFinal)
    if weights == 100:
        print("The Weights are 100%")


# Get the average grade obtained on the assignments
AvgAssignments=

# Validate the input as a float between 0 and 100
if AvgAssignments>=0 and AvgAssignments<=100 :
    print("The Average Grade is Validated for Assignment")
else :
    print("The Average Grade is Not Validated for Assignment")


# Get the number of tests (call the appropriate function)
No_of_test=getNumberOfTests()

# Prompt the user for each test grades and accumulate the value
# Validate the input as a float between 0 and 100

# Calculate the average test grade.
AvgTests


# Prompt and get the final grade
final=
# Validate the input as a float between 0 and 100
if final>=0 and final<=100 :
    print("The Final is Validated")
else :
    print("The Final is Not Validated")

# Calculate and display the final numeric grade (call the appropriate function)
numericGrade=calculateNumericGrade(AvgAssignments,AvgTests,final,wAssignments,wTests,wFinal)
print("The Numeric Grade is :"+numericGrade)

# Calculate and display the final alphabetical grade (call the appropriate function)
alpha_grade=calculateAlphaGrade((numericGrade))
print("The Final alphabetical Grade is :"+alpha_grade)
