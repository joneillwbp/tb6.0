#JACK O'Neill
#DENNIS KIM
#PEACE RUGGIA
#
#This script is used to take a TouchBistro OT Details report and convert it into
#an ADP import file.
#
#      LINE INDEX
#
# 44 - Library Imports
#
# 50 - Local Function: Convert TouchBistro ID into ADP # ID
#
# 55 - Local Function: Convert TouchBistro Job into ADP Job ID, also tracks if
#      the position is as a trainer.
#
# 134 - Local Function: Tracks Exception users to exclude from export.
#
# 148 - Local Function: Determines if the start date is a Holiday
#
# 167 - Local Function: Test is hours are negative returning BOOL
#
# 176 - Variable Declarations
#
# 201 - CVS Reader and transfer unique lines into list. If the shift is an
#       existing ID/Job/notHoliday combanation, then add the hours and skip the line.
#
# 246 - Loop Through list to seperate Training shifts
#
# 264 - Test for holiday date at start of shift
#
# 278 - Adjust the first two lines into ADP format and differentiate the company
#
# 293 - Set file output Variables
#
# 296 - consolidate TRN shifts with regular Shifts and put these on the same line.
#
# 330 - Subtract Holiday hours from lowest paying hours
#
# 341 - TEST lines to print outputname
#
# 347 - Converts code to .CSV output

################################################################################
import os
import glob
import csv
import array
import time

################################################################################
################################################################################
#returns Bool to test if number is negative
def isNegativeHRS(HRS):
    if HRS < 0:
        return True;
    else:
        return False;
#Try to run for every file in input ending in .csv
for file in glob.glob("./input/*.csv"):
###############################################################################
    #File specific Variables that reset for each file
    firstrow_company = ""
    secondrow_headers = ""
    listOfAllShifts = []
    index = 0
    consolidatedIndex = 0
    consolidatedList = []
    thirdList = []
    cocode = ""
    outfilename = ""
    batchID = "90"
    ratecode = ""
    temprate = ""
    ### What items in each line translates to numerically the position in the list
    name = 0
    job = 1
    hrs = 5
    overtime = 11
    startDate = 2
    TRNCode = 14
    hold = []
    TRNHours = 15
    HOLCode = 16
    HOLHours = 17
################################################################################
#First consolidation. This will combine all like Name/Job hours
    #Read in .CSV
    with open('{0}'.format(file)) as csvFile:
        csv_reader = csv.reader(csvFile)
        #Loop through the CSV file line by line
        for row in csv_reader:
             #put first line into a string and move to next row
            if firstrow_company == "":
                firstrow_company = row
            #put the 2nd line into a string and move to next row
            elif secondrow_headers == "":
                secondrow_headers = row
            elif NotAManagerOrIT(row) == True:
                #Add new blank fields to each line, for TRNCode, TRNHours, HOLCode, HOLHours
                row.append('')
                row.append('')
                row.append('')
                row.append('')
                #take the CSV reader row and put it as a new list item so we can work with it
                listOfAllShifts.append(row)
        #pop last line because that is the "REPORT SUMMARY"
        listOfAllShifts.pop()
        #Sort the list so all jobs are grouped per users
        listOfAllShifts.sort()
        #we need to move the first line over b.c. consolidatedList cannot be empty. Also b.c. the first line is 100% unique.
        consolidatedList.append(listOfAllShifts[0])
        #now we need to consolidate
        while index < len(listOfAllShifts):#this will step through and compare one line at a time
        	#this compares the worker and job position
            #is name the same as the last line?
            if listOfAllShifts[index][name] == consolidatedList[consolidatedIndex][name] and listOfAllShifts[index][job] == consolidatedList[consolidatedIndex][job] and isHoliday(listOfAllShifts[index][startDate]) == False:
            #if so make sure it is not the same exact line being compared to itself..
                if listOfAllShifts[index] != consolidatedList[consolidatedIndex]:
            #if still same name and job and not itslef. Then add Hours and overtime (consolidate)
                    consolidatedList[consolidatedIndex][hrs] = float(consolidatedList[consolidatedIndex][hrs]) + float(listOfAllShifts[index][hrs])
                    consolidatedList[consolidatedIndex][overtime] = float(consolidatedList[consolidatedIndex][overtime]) + float(listOfAllShifts[index][overtime])
            #this name/job combo is the first,
            #Add this as a new entry on the consolidated list and increase the index
            else:
                consolidatedIndex += 1
                consolidatedList.append(listOfAllShifts[index])
                #append 2nd list
            #once all list items are compared to the consolidated list. Move onto the next list item
            index += 1
################################################################################
#Now we need to sweep through again and differentiate Regular vs TRN.
    #reset index and now step through our first consolidation
    #We now need to go through again and handle TRN
    index = 0
    while index < len(consolidatedList):
        #Convert name
        consolidatedList[index][name] = ChangeNameToNumbers(consolidatedList[index][name])
        #convert Job and Recognize if it TRN. Function Returns Two variables so store into temp tuple
        hold = ChangeJobToNumbers(consolidatedList[index][job],consolidatedList[index][TRNCode])
        #Put Tuple into correct fields.
        consolidatedList[index][job] = hold[0]
        consolidatedList[index][TRNCode] = hold[1]
        #If the shift is "TRN" we need to move those hours into a different column
        if consolidatedList[index][TRNCode] == 'TRN':
            consolidatedList[index][TRNHours] = consolidatedList[index][hrs]
            consolidatedList[index][hrs] = str(float(consolidatedList[index][hrs]) - float(consolidatedList[index][TRNHours]))
        index += 1
################################################################################
#Test for holiday date at start of shift
    index = 0
    while index < len(consolidatedList):
        if isHoliday(consolidatedList[index][startDate]) == True:
            consolidatedList[index][HOLCode] = "HOL"
#Holiday hours get taken from lowest paying hours, First try to take these from REG HRS
            if consolidatedList[index][hrs] != '':
                consolidatedList[index][HOLHours] = consolidatedList[index][hrs]
                consolidatedList[index][hrs] = str(float(consolidatedList[index][hrs]) - float(consolidatedList[index][hrs]))
            if consolidatedList[index][TRNHours] != '':
                consolidatedList[index][HOLHours] = consolidatedList[index][TRNHours]
                consolidatedList[index][hrs] = str(float(consolidatedList[index][hrs]) - float(consolidatedList[index][TRNHours]))
        index += 1
################################################################################
#  Read and change first line accordingly.
    if 'SKY' in firstrow_company[0]:
        cocode = "MC8"
        outfilename = "Sky"
    elif 'sky' in firstrow_company[0]:
        cocode = "MC8"
        outfilename = "Sky"
    elif 'Sky' in firstrow_company[0]:
        cocode = "MC8"
        outfilename = "Sky"
    else:
        Cocode = "KS7"
        outfilename = "Tow"
    secondrow_headers = ['Co Code','Batch ID','File #','Rate Code','Temp Dept','Temp Rate','Reg Hours','O/T Hours','Hours 3 Code','Hours 3 Amount','Hours 4 Code','Hours 4 Amount','Reg Earnings','O/T Earnings']
################################################################################
    timestr = time.strftime("%Y%m%d")
    outputname = file + '_toADP_' + timestr + '.csv'
################################################################################
    #We now need to sweep through again to consolidate TRN shifts with regular Shifts
    #and put these on the same line.
    index = 0
    otherindex = 0
    thirdList.append(consolidatedList[index])
    while index < len(consolidatedList):
        if consolidatedList[index][name] ==  thirdList[otherindex][name] and consolidatedList[index][job] == thirdList[otherindex][job]:
            thirdList[otherindex][hrs] = str(float(thirdList[otherindex][hrs]) + float(consolidatedList[index][hrs]))
            thirdList[otherindex][overtime] = str(float(thirdList[otherindex][overtime]) + float(consolidatedList[index][overtime]))
        #convert TRN hours into Number so it can be added
            if thirdList[otherindex][TRNHours] == '':
                thirdList[otherindex][TRNHours] = '0'
            if consolidatedList[index][TRNHours] == '':
                consolidatedList[index][TRNHours] = '0'
            thirdList[otherindex][TRNHours] = str(float(thirdList[otherindex][TRNHours]) + float(consolidatedList[index][TRNHours]))
            if thirdList[otherindex][TRNHours] == '0.0':
                thirdList[otherindex][TRNHours] = ''
            if thirdList[otherindex][TRNHours] != '':
                thirdList[otherindex][TRNCode] = "TRN"
        #convert HOL hours into Number so it can be added
            if thirdList[otherindex][HOLHours] == '':
                thirdList[otherindex][HOLHours] = '0'
            if consolidatedList[index][HOLHours] == '':
                consolidatedList[index][HOLHours] = '0'
            thirdList[otherindex][HOLHours] = str(float(thirdList[otherindex][HOLHours]) + float(consolidatedList[index][HOLHours]))
            if thirdList[otherindex][HOLHours] == '0.0':
                thirdList[otherindex][HOLHours] = ''
            if thirdList[otherindex][HOLHours] != '':
                thirdList[otherindex][HOLCode] = "HOL"
        else:
            otherindex += 1
            thirdList.append(consolidatedList[index])
        index += 1
################################################################################
# since HOLHours are deducted from regular hours, if the holiday shift is TRN the hours will become negative
# in this situation HRS need to be taken from TRN and HRS needs to be added back
    index = 0
    while index < len(thirdList):
        if isNegativeHRS(float(thirdList[index][hrs])) == True:
            #adding negative, subtracts the hrs from TRN
            thirdList[index][TRNHours] = float(thirdList[index][TRNHours]) + float(thirdList[index][hrs])
            #Reset HRS by negative amount.
            thirdList[index][hrs] = float(thirdList[index][hrs]) - float(thirdList[index][hrs])
        index += 1
################################################################################
#TEST LINES TO PRINT OUTPUT
    # index = 0
    # while index < len(thirdList):
    #     print(cocode + ", " + batchID + ", " + thirdList[index][name] + ", " + thirdList[index][job] + ", " + str(thirdList[index][hrs]) + ", " + str(thirdList[index][overtime]) + ", " + thirdList[index][TRNCode] + ", " + str(thirdList[index][TRNHours]) + ", " + thirdList[index][HOLCode] + ", " + str(thirdList[index][HOLHours]))
    #     index += 1
################################################################################
#Changes output into .CSV
    with open(outputname,'w') as csvfile:
        index = 0
        #newline '' will remove blank rows
        writer = csv.writer(csvfile)
        #loop through for ever line in list
        writer.writerow(secondrow_headers)
        while index < len(thirdList):
            #each list needs to be put into a single variable, otherwise excel will
            #put each charachter in a new cell
            namestring = thirdList[index][name]
            jobstring = thirdList[index][job]
            hrsstring = str(float(thirdList[index][hrs]))
            othrsstring = str(float(thirdList[index][overtime]))
            if othrsstring == '0.0':
                othrsstring = ''
            trncodestring = thirdList[index][TRNCode]
            trnhrsstring = thirdList[index][TRNHours]
            if trnhrsstring == '0':
                trnhrsstring = ''
            holcodestring = thirdList[index][HOLCode]
            holhrsstring = thirdList[index][HOLHours]
            if holhrsstring == '0':
                holhrsstring = ''
            writer.writerow([cocode]+[batchID]+[namestring]+[ratecode]+[jobstring]+[temprate]+[hrsstring]+[othrsstring]+[trncodestring]+[trnhrsstring]+[holcodestring]+[holhrsstring])
            index += 1
