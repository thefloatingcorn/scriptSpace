# Function: matching rows from excel2.table2 to excel1.table1,
#   based on a reference column which has same elements.
# Output: two txt files to be transformed into xlsx, and one log file.

# module used to read xlsx
import xlrd

def main():

    ###############################
    # start of a part to be updated accroding to target excels
    ###############################

    print('Loading table1...')
    excel1 = xlrd.open_workbook('DictateIT-SpeechMagic-Soliton Users List.xlsx')
    table1 = excel1.sheet_by_name(u'Dictate IT Users')

    print('Loading table2...')
    excel2 = xlrd.open_workbook('20190219 Detailed file for analysis columns removed UUID added for EPIC-V1.4.xlsx')
    table2 = excel2.sheet_by_name(u'Analysis sheet')

    # used when writing column names
    #shortNameForTable2 = 'NHSRM' + ':'
    shortNameForTable2 = ''

    # offset of row/column to be set
    # e.g. set to 1 if one row/column to skip
    firstRowTable1 = 1
    firstRowTable2 = 1
    firstColTable2 = 2
    lastColTable2 = 48
    lastColTable2 += 1

    # row interval for indicating process in console
    processIndicatorRowInterval = 1000

    # reading the reference column
    refColumn_list1 = table1.col_values(3) # read Column  from table1
    refColumn_list2 = table2.col_values(51) # read Column from table2

    # print(refColumn_list1)
    # print('***********************************')
    # print(refColumn_list2)

    ###############################
    # end fo a part to be updated accroding to target excels
    ###############################

    print('Files opened for saving results.')
    file1 = open('match.txt', 'w+')
    file2 = open('nonMatch.txt','w+')
    file3 = open('log.txt', 'w+')

    # variable to keep results
    countMatched = 0
    countUnmatch = 0
    countIfUsedRow = [0 for j in range(table2.nrows)]

    # read the column names from table2 and write to results as the first row
    for k in range(firstColTable2,lastColTable2):
        file1.write(shortNameForTable2 + \
            table2.row_values(firstRowTable2-1)[k]+'$')
        file2.write(shortNameForTable2 + \
            table2.row_values(firstRowTable2-1)[k]+'$')
    file1.write('\n')
    file2.write('\n')

    # for each row in table1
    for i in range(firstRowTable1, table1.nrows):
        # set a flag to show if this row can be matched with table2
        isFound = False;
        # for each row in table2
        for j in range(firstRowTable2, table2.nrows):
            # row is matched if two elements from the sharing column are same
            #print(str(refColumn_list1[i])+','+str(refColumn_list2[j]))
            if refColumn_list1[i] == refColumn_list2[j]:
                # write the current row from table2 into file1
                #print('Matched.')
                for k in range(firstColTable2,lastColTable2):
                    file1.write(str(table2.row_values(j)[k])+'$')
                file1.write('\n')
                # update status variables
                countMatched += 1
                countIfUsedRow[j] += 1
                isFound = True
                break
        # when no matching row can be found from table2
        if isFound == False:
            # write an empty row into file1
            for k in range(firstColTable2,lastColTable2):
                file1.write(''+'$')
            file1.write('\n')
        # indicating the process of matching
        if i%processIndicatorRowInterval == 0:
            print(str(i) + ' rows done.')

    # for each row in table2
    for j in range(firstRowTable2, table2.nrows):
        # if this row cannot be matched to table1
        if countIfUsedRow[j] == 0:
            # write this row into file2
            for k in range(firstColTable2, lastColTable2):
                file2.write(str(table2.row_values(j)[k])+'$')
            file2.write('\n')
            countUnmatch += 1
        # if this row is matched to multiple rows in table1
        elif countIfUsedRow[j] > 1:
            # save into the log file
            file3.write(str(table2.row_values(j)[0])+' matched '\
            + str(countIfUsedRow[j])+' times.\n')

    # finish the log file
    file3.write(str(countMatched) + ' entries matched from table2 ('\
    + str(table2.nrows-firstRowTable2) + ' entries) to table1 ('\
    + str(table1.nrows-firstRowTable1) + ' entries).\n')
    file3.write(str(countUnmatch) +' entries unmatched.')

    file1.close()
    file2.close()
    file3.close()

    print('Files closed and results saved.')

if __name__ == '__main__':
    print('********** Scripts start. **********')
    main()
    print('********** Scripts end. **********')
