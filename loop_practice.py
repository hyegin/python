# python
fun fun python
def printAverages(grades):
    '''
    This function prints average excluding the lowest number.
    '''
    for i in range(0,len(grades)):
        min= 999
        sum = 0
        for j in range(0,len(grades[i])):
            if min > grades[i][j]:
                min = grades[i][j]
            sum += grades[i][j]
        sum-= min
        print("Average for row ", i, " is ", sum / (len(grades[i])-1))

def addTables(table1, table2):
    '''
    this function adds the avalue of each element in table 1 to the value of the corresponding element of table 2 and store the suma t the same location in table 3.
    '''
    results = []
    for i in range(0, len(table1)):
        temp = []
        for j in range(0, len(table1[i])):
           temp.append(table1[i][j] + table2[i][j])
        results.append(temp)
    return results
