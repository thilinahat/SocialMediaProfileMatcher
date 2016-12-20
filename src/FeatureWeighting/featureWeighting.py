#!/usr/bin/env python

import json

from StringComparison import softtfidf

threshold = {
    'name': 0.73785,
    'work': 0.52455,
    'education': 0.62035,
    'mobile': 0.83425
}

featureWeights = {
    'name': 0,
    'work': 0,
    'education': 0,
    'mobile': 0,
    'email': 0,
    'birthday': 0,
    'languages': 0,
    'maritalStatus': 0
    #'friends': 0
}

"""
fbProfileList = [
    {
    'name': 'Thilina Hettiarachchi',
    'work': ['Mech Pump System PVT Engineer','Capital Solutions Lanka - PVT LTD', 'Nestle Production Exe'],
    'education': ["St.Anne's College", 'Institute of Engineering Technology, Katunayake','Engineering'],
    'currentCity': 'Malabe',
    'homeTown': 'Kurunegala',
    'mobile': None,
    'email': None,
    'birthday': '3 October',
    'gender': 'Male',
    'languages': [],
    'maritalStatus': None,
    'friends': ['Udeni Attanayake ','Manula Rajapaksha','Dinuka Dulani Fonseka'],
    'nearestHit': 0,
    'nearestMiss': 0
    },
    {
    'name': 'Thilina Hettiarachchi',
    'work': ['CAKE LABS Software Engineering Intern'],
    'education': ['Royal College', 'Science College','University Of Moratuwa'],
    'currentCity': 'Banadaragama',
    'homeTown': 'Mount Lavinia',
    'mobile': '0719565744',
    'email': 'asankafake92@gmail.com',
    'birthday': '25 July 1992',
    'gender': 'Male',
    'languages': ['Sinhala','English'],
    'maritalStatus': 'Single',
    'friends': ['Dinindu Nissanka','Isuru weerewardhana','Sachithra Pathiraja'],
    'nearestHit': 1,
    'nearestMiss': 0
    },
    {
    'name': 'Asanka Hettiarachchi',
    'work': ['Pearson Lanka','eCollege',''],
    'education': ['University of Colombo School of Computing', 'University of Kelaniya','Nalanda College - Colombo 10'],
    'currentCity': 'Padduka',
    'homeTown': 'Colombo, Sri Lanka',
    'mobile': None,
    'email': None,
    'birthday': None,
    'gender': 'Male',
    'languages': ['Sinhala'],
    'maritalStatus': 'Married',
    'friends': ['Chathura Wellage','Isanka Lakmal Dissanayake','Isuru Amarasinghe'],
    'nearestHit': 2,
    'nearestMiss': 0
    }
]
"""

"""
linkedInProfileList = [
    {
        'name': 'Thilina Hettiarachchi',
        'education': ["St.Anne's College"],
        'mobile': None,
        'email': None,
        'birthday': 'October 3',
        'maritalStatus': None,
        'connections': ['Janaka Gunathilaka','Siyad Zain','Chanaka Nissanka'],
        'experience': ['Engineer Mech Pumps Systems PVT LTD', 'Production Executive Nestle'],
        'languages': ['English']
    },
    {
        'name': 'Thilina Hettiarachchi',
        'education': ['Royal College','University Of Moratuwa'],
        'mobile': '0719565744',
        'email': '333thilina@gmail.com',
        'birthday': 'July 25',
        'maritalStatus': 'Single',
        'connections': ['Dinindu Nissanka','Gihan Hettiarachchi','Prasad Maduranga'],
        'experience': ['Intern Software Engineer CAKE LABS'],
        'languages': ['Sinhala','English']
    },
    {
        'name': 'Asanka Hettiarachchi',
        'education': ['University of Colombo', 'Kelaniya Vishwavidyalaya'],
        'mobile': None,
        'email': None,
        'birthday': None,
        'maritalStatus': None,
        'connections': ['Chinthani Dissanayake', 'Nilupa Samarasinghe', 'Lahiru Dharmasena'],
        'experience': ['Senior Software Engineer Pearson Lanka', 'Developer Fronter AS', 'Software Engineer eCollege', 'Software Engineer BenWorldWide'],
        'languages': ['English']
    }
]
"""

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

def getSimilarityScore(value1,value2):
    return softtfidf.getSimilarityScore(value1, value2)

def findNearestMissForEachProfile():

    for w in range(0, len(fbProfileList)):

        previousSimilarityScore = -10
        temp =0.0
        for x in range(0, len(linkedInProfileList)):

            currentSimilarityScore = 0
            # name similarity
            temp = getSimilarityScore(fbProfileList[w]['name'], linkedInProfileList[x]['name'])
            if temp >= threshold['name']:
                currentSimilarityScore += temp

            # mobile similarity
            if ('mobile' in fbProfileList[w] and 'mobile' in linkedInProfileList[x]):
                temp = getSimilarityScore(fbProfileList[w]['mobile'], linkedInProfileList[x]['mobile'])
                if temp >= threshold['mobile']:
                    currentSimilarityScore += temp

            # email similarity
            if ('email' in fbProfileList[w] and 'email' in linkedInProfileList[x]):
                temp = getSimilarityScore(fbProfileList[w]['email'], linkedInProfileList[x]['email'])
                if temp == 1:
                    currentSimilarityScore += (1)
                else:
                    currentSimilarityScore += (-1)

            # birthday similarity
            if ('birthday' in fbProfileList[w] and 'birthday' in linkedInProfileList[x]):
                temp = getSimilarityScore(fbProfileList[w]['birthday'], linkedInProfileList[x]['birthday'])
                if temp == 1:
                    currentSimilarityScore += (1)
                else:
                    currentSimilarityScore += (-1)

            # maritalStatus similarity
            if ('maritalStatus' in fbProfileList[w] and 'maritalStatus' in linkedInProfileList[x]):
                temp = getSimilarityScore(fbProfileList[w]['maritalStatus'], linkedInProfileList[x]['maritalStatus'])
                if temp == 1:
                    currentSimilarityScore += temp

            # education similarity
            """
            for y in range(0, len(fbProfileList[w]['education'])):
                maxCollegeSimilarity = 0
                for z in range(0, len(linkedInProfileList[x]['education'])):
                    temp = getSimilarityScore(fbProfileList[w]['education'][y]['school'], linkedInProfileList[x]['education'][z]['school'])
                    if (temp >= threshold['education'] and maxCollegeSimilarity < temp):
                        maxCollegeSimilarity = temp
                totalEducationSimilarity += maxCollegeSimilarity
            """
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
                    currentSimilarityScore += (totalEducationSimilarity / len(linkedInProfileList[x]['education']))

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
                    currentSimilarityScore += (totalLanguageSimilarity / len(fbProfileList[w]['languages']))

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
                    currentSimilarityScore += (totalWorkSimilarity / len(fbProfileList[w]['work']))

            """
            # friends and connections similarity
            totalFriendsSimilarity = 0
            for y in range(0, len(fbProfileList[w]['friends'])):
                maxFriendsSimilarity = 0
                for z in range(0, len(linkedInProfileList[x]['connections'])):
                    temp = getSimilarityScore(fbProfileList[w]['friends'][y], linkedInProfileList[x]['connections'][z])
                    if (temp >= threshold['name'] and maxFriendsSimilarity < temp):
                        maxFriendsSimilarity = temp
                totalFriendsSimilarity += maxFriendsSimilarity
            if totalFriendsSimilarity > 0:
                currentSimilarityScore += (totalFriendsSimilarity / len(fbProfileList[w]['friends']))
            """

            if (currentSimilarityScore > previousSimilarityScore and x != fbProfileList[w]['nearestHit']):
                previousSimilarityScore = currentSimilarityScore
                fbProfileList[w]['nearestMiss'] = x

        #print("Nearest Similarity score of Facebook Profile  " + str(w) + " is " + str(previousSimilarityScore))
        print("Nearest Miss Of Facebook Profile " + str(w) + " is " + str(fbProfileList[w]['nearestMiss']))

def calculateFeatureWeights():
    for i in range(0, len(fbProfileList)):

        # name
        featureWeights['name'] += getSimilarityScore(fbProfileList[i]['name'], linkedInProfileList[fbProfileList[i]['nearestMiss']]['name'])
        featureWeights['name'] -= getSimilarityScore(fbProfileList[i]['name'], linkedInProfileList[fbProfileList[i]['nearestHit']]['name'])

        # mobile
        if ('mobile' in fbProfileList[i] and 'mobile' in linkedInProfileList[fbProfileList[i]['nearestMiss']]):
            featureWeights['mobile'] += getSimilarityScore(fbProfileList[i]['mobile'],
                                                         linkedInProfileList[fbProfileList[i]['nearestMiss']]['mobile'])
        if ('mobile' in fbProfileList[i] and 'mobile' in linkedInProfileList[fbProfileList[i]['nearestHit']]):
            featureWeights['mobile'] -= getSimilarityScore(fbProfileList[i]['mobile'],
                                                         linkedInProfileList[fbProfileList[i]['nearestHit']]['mobile'])

        # email
        if ('email' in fbProfileList[i] and 'email' in  linkedInProfileList[fbProfileList[i]['nearestMiss']]):
            featureWeights['email'] += getSimilarityScore(fbProfileList[i]['email'],
                                                         linkedInProfileList[fbProfileList[i]['nearestMiss']]['email'])
        if ('email' in  fbProfileList[i] and 'email' in  linkedInProfileList[fbProfileList[i]['nearestHit']]):
            featureWeights['email'] -= getSimilarityScore(fbProfileList[i]['email'],
                                                         linkedInProfileList[fbProfileList[i]['nearestHit']]['email'])

        # birthday
        if ('birthday' in fbProfileList[i] and 'birthday' in linkedInProfileList[fbProfileList[i]['nearestMiss']]):
            featureWeights['birthday'] += getSimilarityScore(fbProfileList[i]['birthday'],
                                                         linkedInProfileList[fbProfileList[i]['nearestMiss']]['birthday'])
        if ('birthday' in fbProfileList[i] and 'birthday' in linkedInProfileList[fbProfileList[i]['nearestHit']]):
            featureWeights['birthday'] -= getSimilarityScore(fbProfileList[i]['birthday'],
                                                         linkedInProfileList[fbProfileList[i]['nearestHit']]['birthday'])

        # maritalStatus
        if ('maritalStatus' in fbProfileList[i] and 'maritalStatus' in linkedInProfileList[fbProfileList[i]['nearestMiss']]):
            featureWeights['maritalStatus'] += getSimilarityScore(fbProfileList[i]['maritalStatus'],
                                                         linkedInProfileList[fbProfileList[i]['nearestMiss']]['maritalStatus'])
        if ('maritalStatus' in fbProfileList[i] and 'maritalStatus' in linkedInProfileList[fbProfileList[i]['nearestHit']]):
            featureWeights['maritalStatus'] -= getSimilarityScore(fbProfileList[i]['maritalStatus'],
                                                         linkedInProfileList[fbProfileList[i]['nearestHit']]['maritalStatus'])

        # education similarity
        totalEducationSimilarityHit = 0
        totalEducationSimilarityMiss = 0
        maxCollegeSimilarity = 0
        if 'education' in linkedInProfileList[fbProfileList[i]['nearestMiss']] and 'education' in fbProfileList[i]:
            for y in range(0, len(linkedInProfileList[fbProfileList[i]['nearestMiss']]['education'])):
                for z in range(0, len(fbProfileList[i]['education'])):
                    temp = getSimilarityScore(fbProfileList[i]['education'][z]['school'], linkedInProfileList[fbProfileList[i]['nearestMiss']]['education'][y]['school'])
                    if (maxCollegeSimilarity < temp):
                        maxCollegeSimilarity = temp
                totalEducationSimilarityMiss += maxCollegeSimilarity
                maxCollegeSimilarity = 0
        if 'education' in linkedInProfileList[fbProfileList[i]['nearestHit']] and 'education' in fbProfileList[i]:
            for y in range(0, len(linkedInProfileList[fbProfileList[i]['nearestHit']]['education'])):
                for z in range(0, len(fbProfileList[i]['education'])):
                    temp = getSimilarityScore(fbProfileList[i]['education'][z]['school'], linkedInProfileList[fbProfileList[i]['nearestHit']]['education'][y]['school'])
                    if (maxCollegeSimilarity < temp):
                        maxCollegeSimilarity = temp
                totalEducationSimilarityHit += maxCollegeSimilarity
                maxCollegeSimilarity = 0
        if totalEducationSimilarityMiss > 0:
            featureWeights['education'] += (totalEducationSimilarityMiss / len(linkedInProfileList[fbProfileList[i]['nearestMiss']]['education']))
        if totalEducationSimilarityHit > 0:
            featureWeights['education'] -= (totalEducationSimilarityHit / len(linkedInProfileList[fbProfileList[i]['nearestHit']]['education']))

        # languages similarity
        totalLanguageSimilarityHit = 0
        totalLanguageSimilarityMiss = 0
        if 'languages' in fbProfileList[i]:
            for y in range(0, len(fbProfileList[i]['languages'])):
                if 'languages' in linkedInProfileList[fbProfileList[i]['nearestMiss']]:
                    maxLanguageSimilarity = 0
                    for z in range(0, len(linkedInProfileList[fbProfileList[i]['nearestMiss']]['languages'])):
                        temp = getSimilarityScore(fbProfileList[i]['languages'][y],
                                                  linkedInProfileList[fbProfileList[i]['nearestMiss']]['languages'][z])
                        if (maxLanguageSimilarity < temp):
                            maxLanguageSimilarity = temp
                    totalLanguageSimilarityMiss += maxLanguageSimilarity
                if 'languages' in linkedInProfileList[fbProfileList[i]['nearestHit']]:
                    maxLanguageSimilarity = 0
                    for z in range(0, len(linkedInProfileList[fbProfileList[i]['nearestHit']]['languages'])):
                        temp = getSimilarityScore(fbProfileList[i]['languages'][y],
                                                  linkedInProfileList[fbProfileList[i]['nearestHit']]['languages'][z])
                        if (maxLanguageSimilarity < temp):
                            maxLanguageSimilarity = temp
                    totalLanguageSimilarityHit += maxLanguageSimilarity
        if totalLanguageSimilarityMiss > 0:
            featureWeights['languages'] += (totalLanguageSimilarityMiss / len(fbProfileList[i]['languages']))
        if totalLanguageSimilarityHit > 0:
            featureWeights['languages'] -= (totalLanguageSimilarityHit / len(fbProfileList[i]['languages']))

        # work and experience similarity
        totalWorkSimilarityHit = 0
        totalWorkSimilarityMiss = 0
        if 'work' in fbProfileList[i]:
            for y in range(0, len(fbProfileList[i]['work'])):
                if 'experience' in linkedInProfileList[fbProfileList[i]['nearestMiss']]:
                    maxWorkSimilarity = 0
                    for z in range(0, len(linkedInProfileList[fbProfileList[i]['nearestMiss']]['experience'])):
                        temp = getSimilarityScore(fbProfileList[i]['work'][y]['work'],
                                                  linkedInProfileList[fbProfileList[i]['nearestMiss']]['experience'][z]['organisation'])
                        if (maxWorkSimilarity < temp):
                            maxWorkSimilarity = temp
                    totalWorkSimilarityMiss += maxWorkSimilarity
                if 'experience' in linkedInProfileList[fbProfileList[i]['nearestHit']]:
                    maxWorkSimilarity = 0
                    for z in range(0, len(linkedInProfileList[fbProfileList[i]['nearestHit']]['experience'])):
                        temp = getSimilarityScore(fbProfileList[i]['work'][y]['work'],
                                                  linkedInProfileList[fbProfileList[i]['nearestHit']]['experience'][z]['organisation'])
                        if (maxWorkSimilarity < temp):
                            maxWorkSimilarity = temp
                    totalWorkSimilarityHit += maxWorkSimilarity
        if totalWorkSimilarityMiss > 0:
            featureWeights['work'] += (totalWorkSimilarityMiss / len(fbProfileList[i]['work']))
        if totalWorkSimilarityHit > 0:
            featureWeights['work'] -= (totalWorkSimilarityHit / len(fbProfileList[i]['work']))

        """
        # friends and connections similarity
        totalFriendsSimilarityHit = 0
        totalFriendsSimilarityMiss = 0
        for y in range(0, len(fbProfileList[i]['friends'])):
            maxFriendsSimilarity = 0
            for z in range(0, len(linkedInProfileList[fbProfileList[i]['nearestMiss']]['connections'])):
                temp = getSimilarityScore(fbProfileList[i]['friends'][y],
                                          linkedInProfileList[fbProfileList[i]['nearestMiss']]['connections'][z])
                if (maxFriendsSimilarity < temp):
                    maxFriendsSimilarity = temp
            totalFriendsSimilarityMiss += maxFriendsSimilarity
            maxFriendsSimilarity = 0
            for z in range(0, len(linkedInProfileList[fbProfileList[i]['nearestHit']]['connections'])):
                temp = getSimilarityScore(fbProfileList[i]['friends'][y],
                                          linkedInProfileList[fbProfileList[i]['nearestHit']]['connections'][z])
                if (maxFriendsSimilarity < temp):
                    maxFriendsSimilarity = temp
            totalFriendsSimilarityHit += maxFriendsSimilarity
        if totalFriendsSimilarityMiss > 0:
            featureWeights['friends'] += (totalFriendsSimilarityMiss / len(fbProfileList[i]['friends']))
        if totalFriendsSimilarityHit > 0:
            featureWeights['friends'] -= (totalFriendsSimilarityHit / len(fbProfileList[i]['friends']))
        """

findNearestMissForEachProfile()
calculateFeatureWeights()
print(json.dumps(featureWeights))