from flask import Flask, url_for,jsonify,request
from db import mongoConnector

app = Flask(__name__)

@app.route('/')
def api_root():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/demo', methods = ['GET'])
def api_demo():
    if 'name' in request.args:
        response = {}
        linkedInProfiles = mongoConnector.getLinkedInProfiles(request.args['name'])
        fbProfiles = mongoConnector.getFacebookProfiles(request.args['name'])
        html = ""
        html += "<div><h1 style='color:black'>FaceBook Profiles</h1></div>"
        html += "<div>"
        for count in range(0, len(fbProfiles)):
            if 'profile_picture' in fbProfiles[count]:
                html += "<img height='100' width='100' src='" + fbProfiles[count]['profile_picture'] +"' />"
        html += "</div>"
        html += "<div><h1 style='color:black'>LinkedIn Profiles</h1></div>"
        html += "<div>"
        for count in range(0, len(linkedInProfiles)):
            if 'profile_picture' in linkedInProfiles[count]:
                html += "<img height='100' width='100' src='" + linkedInProfiles[count]['profile_picture'] +"' />"
                #html += "<p>"+linkedInProfiles[count]['name']+"</p>"
        html += "</div>"
        html += "<div><h1 style='color:black'>Merged Profiles</h1></div>"
        html += "<div>"
        mergedProfiles = mongoConnector.demo(fbProfiles, linkedInProfiles)
        for count in range(0, len(mergedProfiles)):
            if 'facebook' in mergedProfiles[count] and 'profile_picture' in mergedProfiles[count]['facebook']:
                html += '</br>'
                html += "<img height='100' width='100' src='" + mergedProfiles[count]['facebook']['profile_picture'] +"' />"
            if 'linkedIn' in mergedProfiles[count] and 'profile_picture' in mergedProfiles[count]['linkedIn']:
                html += "<img height='100' width='100' src='" + mergedProfiles[count]['linkedIn']['profile_picture'] +"' />"
            html += '</br>'
        html += "</div>"
        return html
    else:
        error = {
            "status": 400,
            "message": "Please provide a valid name"
        }
        return jsonify(error)

@app.route('/match', methods = ['GET'])
def api_match():
    if 'name' in request.args:
        response = {}
        response['mergedSocialMediaAccounts'] = mongoConnector.main(request.args['name'])
        return jsonify(response)
    else:
        error = {
            "status": 400,
            "message": "Please provide a valid name"
        }
        return jsonify(error)

if __name__ == '__main__':
    app.run()