outputArray = []
outputDict  = {}

for attendee in sqlQueries.output.getAttendees:
    if attendee.attendee:
        outputDict = attendee
        outputDict['attendeecount'] =     int(outputDict['attendeecount'])/ int(sqlQueries.output.getEventCount[0].count)
        outputArray.append(outputDict)
outputArray.sort(key=lambda x: (-x['invited'], -x['attendeecount']))
return outputArray
 