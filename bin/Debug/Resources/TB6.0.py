import os
import glob
import csv
import array
import time
################################################################################
#Global variables
jobExclusions = []
nameExclusions = []
Holidays = []
jobcodes = []
OTDetails1stline = ''
OTDetails2ndline = ''
OTDetailSummary = ''
shifts = []
listOfJobCodesrefined = []
CompiledList = []
################################################################################
# Reads UserException file and creates two lists: one for jobs that will be excluded form hour totals,
# Another for names that will not be included.
for file in glob.glob("./*UserExceptions.csv"):
    with open('{0}'.format(file)) as csvFile:
        csv_reader = csv.reader(csvFile)
        listOfUserExceptions = []
        for row in csv_reader:
            listOfUserExceptions.append(row)
    listOfUserExceptionsrefined = []
    for i in range(len(listOfUserExceptions)):
        if listOfUserExceptions[i][0] != '':
            listOfUserExceptionsrefined.append(listOfUserExceptions[i])
    listOfUserExceptionsrefined.pop(0)
    listOfUserExceptionsrefined.pop(0)

    for i in range(len(listOfUserExceptionsrefined)):
        if listOfUserExceptionsrefined[i][0] == 'job':
            jobExclusions.append(listOfUserExceptionsrefined[i][1])
        elif listOfUserExceptionsrefined[i][0] == 'name':
            nameExclusions.append(listOfUserExceptionsrefined[i][1])
# A function that will return a bool if this name/job should be excluded.
def NotAManagerOrIT(row):
    job = 1
    name = 0
    if row[job] in jobExclusions:
        return False;
    elif row[name] in nameExclusions:
        return False;
    return True;

################################################################################
#Reads Holiday file and puts all dates considered holidays into list.
for file in glob.glob("./*Holidays.csv"):
    with open('{0}'.format(file)) as csvFile:
        csv_reader = csv.reader(csvFile)
        listOfHolExceptions = []
        listOfHolExceptionsrefined = []
        for row in csv_reader:
            listOfHolExceptions.append(row)

        for i in range(len(listOfHolExceptions)):
            if listOfHolExceptions[i][0] != '':
                listOfHolExceptionsrefined.append(listOfHolExceptions[i])
        listOfHolExceptionsrefined.pop(0)
        listOfHolExceptionsrefined.pop(0)

        for i in range(len(listOfHolExceptionsrefined)):
            Holidays.append(listOfHolExceptionsrefined[i][0])
#Function returning bool if input matches a holiday
def isHoliday(row):
    row = (row.rsplit('/',1)[0])
    if row in Holidays:
        return True;
    return False;

################################################################################
#Reads Job Codes file and puts Jobs/Codes/isTRN into a 2d list.
for file in glob.glob("./*JobCodes.csv"):
    with open('{0}'.format(file)) as csvFile:
        csv_reader = csv.reader(csvFile)
        listOfJobCodes = []
        for row in csv_reader:
            listOfJobCodes.append(row)

        for i in range(len(listOfJobCodes)):
            if listOfJobCodes[i][0] != '':
                listOfJobCodesrefined.append(listOfJobCodes[i])
        listOfJobCodesrefined.pop(0)
        listOfJobCodesrefined.pop(0)

        for i in range(len(listOfJobCodesrefined)):
            jobcodes.append(listOfJobCodesrefined[i])

def ChangeJobToNumbers(job,TRNCode):

    TRNCode = ''
    for i in range(len(listOfJobCodesrefined)):
        if job == jobcodes[i][0]:
            job = jobcodes[i][1]
            TRNCode = jobcodes[i][2]
    return job,TRNCode;

################################################################################
#cuts name string down to only numbers at end
def ChangeNameToNumbers(name):
    name = name.rsplit(' ', 1)[-1]
    return name;
################################################################################


for file in glob.glob("./*OTDetails.csv"):
    with open('{0}'.format(file)) as csvFile:
        csv_reader = csv.reader(csvFile)
        for row in csv_reader:
            if OTDetails1stline == '':
                OTDetails1stline = row
            elif OTDetails2ndline == '':
                OTDetails2ndline = row
            elif "REPORT SUMMARY" in row[0]:
                OTDetailSummary = row
            else:
                if NotAManagerOrIT(row):

                    if isHoliday(row[1]):
                        #Set HOL Hours (9) equal to hours of the shift (4)
                        row[9] = row[4]
                        #Subtract those; now HOL hours, from Regular (3) hours
                        row[3] = row[3] - row[9]
                    #Update JobName to Number, Save TRN Code in column 8 to differenciate.
                    # row[1], row[8] = ChangeJobToNumbers(row[1], row[8])
                    row[8] = ''
                    row[10] = ''
                    if row[9] != '0.00':
                        row[10] = 'HOL'

                    row = (row[0], row[1], row[5], row[11], row[8], row[7], row[10], row[9])
                    # shifts.append(row[0], row[1], row[5], row[11], row[8], row[7], row[10], row[9])
                    shifts.append(row)

        shifts.sort()
        index = 1
        while index in range(len(shifts)):
            
            if shifts[index][0] == shifts[index-1][0] and shifts[index][1] == shifts[index-1][1]:
                print("hi")
                shifts[index-1][2] += shifts[index][2]
                shifts[index-1][3] += shifts[index][3]
                shifts[index-1][5] += shifts[index][5]
                shifts[index-1][7] += shifts[index][7]
                if shifts[index][4] == 'TRN' or shifts[index-1][4] == 'TRN':
                    shifts[index-1][4] == 'TRN'
                if shifts[index][6] == 'HOL' or shifts[index-1][6] == 'HOL':
                    shifts[index-1][6] == 'HOL'
            index =+ 1


        # otherindex = 0
        # CompiledList.append(shifts[0])
        #
        # for i in range(len(listOfJobCodesrefined)):
        #     if shifts[i][0] == CompiledList[otherindex][0] and shifts[i][1] == CompiledList[otherindex][1]:
        #         CompiledList[otherindex][2] += shifts[i][2]
        #         CompiledList[otherindex][3] += shifts[i][3]
        #         CompiledList[otherindex][5] += shifts[i][5]
        #         CompiledList[otherindex][7] += shifts[i][7]
        #         if CompiledList[otherindex][4] == 'TRN' or shifts[i][4] == 'TRN':
        #              CompiledList[otherindex][4] == 'TRN'
        #         if CompiledList[otherindex][6] == 'HOL' or shifts[i][6] == 'HOL':
        #              CompiledList[otherindex][6] == 'HOL'
        #
        #
        #for i in range(len(shifts)):
            #print(shifts[i])


    #consolidate

    #change TRN

    #CNG Name

    #output
