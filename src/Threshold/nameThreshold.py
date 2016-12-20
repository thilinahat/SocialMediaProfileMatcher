from StringComparison import softtfidf

fbList = [
    'Thilina Hettiarachchi',
    'Asanka Thilina',
    'Sachithra Pathiraja',
    'Sachithra Madushan',
    'Sachithra Madhushan',
    'Dinindu Nissanka',
    'Dinindu Nissanka',
    'Isuru Lakmal',
    'Isuru Weerawardhana'
]

linkedInList = [
    'Thilan Jayamaha',
    'Yasanka Madushanka',
    'Achala Pathirajasenavi',
    'Dhanushka Madushanka',
    'Dhanushka Maduwantha',
    'Amindu Nissan',
    'Dishan Nisansa',
    'Ishan Lakshan',
    'Ishan Weerawansha'
]

def getMinimumScoreForMatchingData():
    minimumScore = 1.0
    for i in range(0, len(fbList)):
        currentScore = softtfidf.getSimilarityScore(fbList[i], linkedInList[i])
        """"
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