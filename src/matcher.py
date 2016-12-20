#!/usr/bin/env python

import json
from StringComparison import softtfidf

# Following features should be allocated higher weight since they are kind of unique compared to other features
    # work, education, mobile, email, birthday, friends
# Following features have a threshold value
    # name, work, education, mobile, friends
# Following features' similarity score has to be binary
    # languages, maritalStatus
# Following features are identified as discriminating features, so the similarity score is {1,-1}
    # birthday, email

threshold = {
    'name': 0.73785,
    'work': 0.52455,
    'education': 0.62035,
    'mobile': 0.83425
}

featureWeights = {
    "languages": 1.5079,
	"education": 14.6238,
	"name": 8.6208,
	"mobile": 0,
	"maritalStatus": 0,
	"work": 21.2158,
	"email": 0,
	"birthday": 0,
    'friends': 0
}

FINAL_THRESHOLD = 15

"""
fbProfileList = []
linkedInProfileList = []

with open('facebook.json') as json_data:
    temp = json.load(json_data)
    fbProfileList = temp['fb_data']
    json_data.close()
    #print(json.dumps(fbProfileList[0]['name']))

with open('linkedin.json') as json_data:
    temp = json.load(json_data)
    linkedInProfileList = temp['linkedin_data']
    json_data.close()
    #print(linkedInProfileList[0]['name'])
"""

def getSimilarityScore(value1,value2):
    return softtfidf.getSimilarityScore(value1, value2)

def mergeSocialMediaAccounts(fbProfile,linkedInProfile,mergedProfileList):
    temp = {
        'facebook': fbProfile,
        'linkedIn': linkedInProfile
    }
    mergedProfileList.append(temp)

def mergeUnmatchedLinkedInAccounts(linkedInProfileList,mergedProfileList):
    for i in range(0,len(linkedInProfileList)):
        if linkedInProfileList[i]['matched'] == False:
            temp = {
                'linkedIn': linkedInProfileList[i]
            }
            mergedProfileList.append(temp)

def mergeUnmatchedFacebookAccounts(fbProfile,mergedProfileList):
    temp = {
        'facebook': fbProfile
    }
    mergedProfileList.append(temp)

def matchSocialMediaAccounts(fbProfileList,linkedInProfileList):
    mergedProfileList = []
    for w in range(0, len(fbProfileList)):

        print("==================================================================================================")
        print("Facebook profile of " + fbProfileList[w]['name'])
        print("==================================================================================================")
        previousSimilarityScore = 0
        linkedInID = -1
        for x in range(0, len(linkedInProfileList)):
            currentSimilarityScore = 0
            temp = 0.0

            # name similarity
            temp = getSimilarityScore(fbProfileList[w]['name'],linkedInProfileList[x]['name'])
            if temp >= threshold['name']:
                currentSimilarityScore += featureWeights['name'] * temp

            # mobile similarity
            if ('mobile' in fbProfileList[w] and 'mobile' in linkedInProfileList[x]):
                temp = getSimilarityScore(fbProfileList[w]['mobile'],linkedInProfileList[x]['mobile'])
                if temp >= threshold['mobile']:
                    currentSimilarityScore += featureWeights['mobile'] * temp

            """
            # email similarity
            if ('email' in fbProfileList[w] and 'email' in linkedInProfileList[x]):
                temp = getSimilarityScore(fbProfileList[w]['email'],linkedInProfileList[x]['email'])
                if temp == 1:
                    currentSimilarityScore += featureWeights['email'] * (1)
                else:
                    currentSimilarityScore += featureWeights['email'] * (-1)

            # birthday similarity
            if ('birthday' in fbProfileList[w] and 'birthday' in linkedInProfileList[x]):
                temp = getSimilarityScore(fbProfileList[w]['birthday'],linkedInProfileList[x]['birthday'])
                if temp == 1:
                    currentSimilarityScore += featureWeights['birthday'] * (1)
                else:
                    currentSimilarityScore += featureWeights['birthday'] * (-1)

            # maritalStatus similarity
            if ('maritalStatus' in fbProfileList[w] and 'maritalStatus' in linkedInProfileList[x]):
                temp = getSimilarityScore(fbProfileList[w]['maritalStatus'], linkedInProfileList[x]['maritalStatus'])
                if temp == 1:
                    currentSimilarityScore += featureWeights['maritalStatus'] * temp
            """

            # education similarity
            if 'education' in linkedInProfileList[x] and 'education' in fbProfileList[w]:
                totalEducationSimilarity = 0
                for y in range(0, len(linkedInProfileList[x]['education'])):
                    maxCollegeSimilarity = 0
                    for z in range(0, len(fbProfileList[w]['education'])):
                        temp = getSimilarityScore(linkedInProfileList[x]['education'][y]['school'],
                                                  fbProfileList[w]['education'][z]['school'])
                        if (temp >= threshold['education'] and maxCollegeSimilarity < temp):
                            maxCollegeSimilarity = temp
                    totalEducationSimilarity += maxCollegeSimilarity
                if totalEducationSimilarity > 0:
                    currentSimilarityScore += featureWeights['education'] * (totalEducationSimilarity / len(linkedInProfileList[x]['education']))

            # languages similarity
            if 'languages' in fbProfileList[w] and 'languages' in linkedInProfileList[x]:
                totalLanguageSimilarity = 0
                for y in range(0, len(fbProfileList[w]['languages'])):
                    maxLanguageSimilarity = 0
                    for z in range(0, len(linkedInProfileList[x]['languages'])):
                        temp = getSimilarityScore(fbProfileList[w]['languages'][y], linkedInProfileList[x]['languages'][z])
                        if temp == 1:
                            maxLanguageSimilarity = temp
                    totalLanguageSimilarity += maxLanguageSimilarity
                if totalLanguageSimilarity > 0:
                    currentSimilarityScore += featureWeights['languages'] * (totalLanguageSimilarity / len(fbProfileList[w]['languages']))

            # work and experience similarity
            if 'work' in fbProfileList[w] and 'experience' in linkedInProfileList[x]:
                totalWorkSimilarity = 0
                for y in range(0, len(fbProfileList[w]['work'])):
                    maxExperienceSimilarity = 0
                    for z in range(0, len(linkedInProfileList[x]['experience'])):
                        temp = getSimilarityScore(fbProfileList[w]['work'][y]['work'], linkedInProfileList[x]['experience'][z]['organisation'])
                        if (temp >= threshold['work'] and maxExperienceSimilarity < temp):
                            maxExperienceSimilarity = temp
                    totalWorkSimilarity += maxExperienceSimilarity
                if totalWorkSimilarity > 0:
                    currentSimilarityScore += featureWeights['work'] * (totalWorkSimilarity / len(fbProfileList[w]['work']))

            # friends and connections similarity
            """
            totalFriendsSimilarity = 0
            for y in range(0, len(fbProfileList[w]['friends'])):
                maxFriendsSimilarity = 0
                for z in range(0, len(linkedInProfileList[x]['connections'])):
                    temp = getSimilarityScore(fbProfileList[w]['friends'][y], linkedInProfileList[x]['connections'][z])
                    if (temp >= threshold['name'] and maxFriendsSimilarity < temp):
                        maxFriendsSimilarity = temp
                totalFriendsSimilarity += maxFriendsSimilarity
            if totalFriendsSimilarity > 0:
                currentSimilarityScore += featureWeights['friends'] * (totalFriendsSimilarity/len(fbProfileList[w]['friends']))
            """

            print("Similarity score of " + linkedInProfileList[x]['name'] + " is " + str(currentSimilarityScore))
            if (currentSimilarityScore > FINAL_THRESHOLD and currentSimilarityScore > previousSimilarityScore):
                previousSimilarityScore = currentSimilarityScore
                linkedInID = x

        if linkedInID > -1:
            linkedInProfileList[linkedInID]['matched'] = True
            mergeSocialMediaAccounts(fbProfileList[w],linkedInProfileList[linkedInID],mergedProfileList)
            print("#####################################################################################################################")
            print("LinkedIn profile of Facebook profile " + fbProfileList[w]['name'] + " is " + linkedInProfileList[linkedInID]['name'])
            print("Similarity score of Facebook Profile " + fbProfileList[w]['name'] + " is " + str(previousSimilarityScore))
            print("#####################################################################################################################")
        else:
            mergeUnmatchedFacebookAccounts(fbProfileList[w],mergedProfileList)
            print("#####################################################################################################################")
            print("No LinkedIn Profile Found")
            print("#####################################################################################################################")
    mergeUnmatchedLinkedInAccounts(linkedInProfileList,mergedProfileList)
    return mergedProfileList

#print(json.dumps(linkedinProfileList[0]))
#print(json.dumps(linkedin_profile))

#print("Jaaro-Winkler similarity")
#print(jellyfish.jaro_winkler("afadfa","adfadf"))

#print("Jaccard Similarity")
#print(distance.jaccard(fb_profile['name'],linkedin_profile['name']))

#print("SoftTF-IDF Similarity")
#print(softtfidf.score(fb_profile['name'],linkedin_profile['name']))

#matchSocialMediaAccounts(fbProfileList,linkedInProfileList)
#mergeUnmatchedLinkedInAccounts()
#print(mergedProfileList)
