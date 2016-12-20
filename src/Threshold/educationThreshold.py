from StringComparison import softtfidf

"""
fbList = [
    'University of Moratuwa - Faculty of Engineering Moratuwa',
    'Royal College Colombo',
    'Richmond College Galle'
]

linkedInList = [
    'University of Moratuwa',
    'Royal College , Colombo-7',
    'Richmond College'
]

"""

fbList = [
    'University of Peradeniya',
    'Royal College Polonnaruwa',
    'Richmond College Galle'
]

linkedInList = [
    'University of Moratuwa',
    'Royal College , Colombo-7.',
    'Mahinda College'
]

def getMinimumScoreForMatchingData():
    minimumScore = 1.0
    for i in range(0, len(fbList)):
        currentScore = softtfidf.getSimilarityScore(fbList[i], linkedInList[i])
        """
        if currentScore < minimumScore:
            minimumScore = currentScore
    return minimumScore
        """
        print ("'" + fbList[i] + "' and '" + linkedInList[i] + "' similarity score is " + str(currentScore))

def getMaximumScoreForNonMatchingData():
    maximumScore = 0.0
    for i in range(0, len(fbList)):
        currentScore = softtfidf.getSimilarityScore(fbList[i], linkedInList[i])
        if maximumScore < currentScore:
            maximumScore = currentScore
    return maximumScore

print(getMinimumScoreForMatchingData())
#print(getMaximumScoreForNonMatchingData())