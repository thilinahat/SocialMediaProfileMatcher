from StringComparison import softtfidf

"""
fbList = [
    'Virtusa Colombo',
    'DirectFN Sri Lanka',
    'MoraSpirit',
    'IronOne Technologies'
]

linkedInList = [
    'Virtusa',
    'DirectFN',
    'Moraspirit Initiative',
    'IronOne Technologies LLC'
]

"""
fbList = [
    'WSO2 Kandy, Sri Lanka',
    'Directtion Setters',
    'Xtreme Youth',
    'Codegen PVT LTD'
]

linkedInList = [
    'Virtusa Colombo',
    'DirectFN',
    'Moraspirit',
    'IronOne Technologies LLC'
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