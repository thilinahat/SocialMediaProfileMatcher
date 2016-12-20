import jellyfish

from StringComparison import softtfidf

fbList = [
    '0719565744',
    '0719563949',
    '0719565744',
    '0719563949',
    '0775673292'
]

linkedInList = [
    '+94-719565744',
    '+94719563949',
    '94719565744',
    '719563949',
    '0775673292'
]


"""
fbList = [
    '0719565744',
    '0719563949',
    '0719565744',
    '0719563949',
    '0775673292'
]

linkedInList = [
    '+94-719544765',
    '0779563949',
    '94706565744',
    '7295612847',
    '0773934139'
]
"""

def getMinimumScoreForMatchingData():
    minimumScore = 1.0
    for i in range(0, len(fbList)):
        #currentScore = softtfidf.getSimilarityScore(fbList[i], linkedInList[i])
        currentScore = float(jellyfish.jaro_distance(fbList[i].decode('unicode-escape'), linkedInList[i].decode('unicode-escape')))
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