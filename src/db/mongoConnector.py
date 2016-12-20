from pymongo import MongoClient
from bson.json_util import dumps
import json
import matcher

client = MongoClient('mongodb://admin:admin@ds153765.mlab.com:53765/asidsocialmedia') # connect to remote db
db = client['asidsocialmedia'] # select db

def getFacebookProfiles(name):
    facebookRecords = []
    queryBuiler = {
        "$or" : []
    }
    for nameToken in name.split():
        queryBuiler["$or"].append({"name": { "$regex": nameToken, "$options": 'i'}})
    for profile in db.facebook.find(queryBuiler):
        temp = dumps(profile) #parsing bson to json string
        facebookRecords.append(json.loads(temp)) # jsonifying the string
    return facebookRecords

def getLinkedInProfiles(name):
    linkedinRecords = []
    queryBuiler = {
        "$or": []
    }
    for nameToken in name.split():
        queryBuiler["$or"].append({"name": {"$regex": nameToken, "$options": 'i'}})
    for profile in db.linkedin.find(queryBuiler):
        temp = dumps(profile)  # parsing bson to json string
        linkedinRecords.append(json.loads(temp))  # jsonifying the string
    return linkedinRecords

def main(name):
    return matcher.matchSocialMediaAccounts(getFacebookProfiles(name), getLinkedInProfiles(name))

def demo(fbProfiles, linkedInProfiles):
    return matcher.matchSocialMediaAccounts(fbProfiles, linkedInProfiles)

if __name__ == '__main__':
    main()