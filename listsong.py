import song
from flask import jsonify
from bson.objectid import ObjectId
def createPlayList(result,db):
    username= result['username']
    listname = result['playlistname']
    #song= result['song']
    play = db.playList
    
    res = []
    
    for x in play.find({'username':username},{'playlistName':1,'username':1,'song':1}):
        
        if (listname == x['playlistName']):
            return jsonify(
                message = "Already exist please try another name"
            ),400
        x['_id'] = str(x['_id'])
        res.append(x['playlistName'])
    play.insert({'username':username,'playlistName':listname,'songName':[]})
    return jsonify(
         res
    ),200
def myPlaylist(result,db):
    username = result ['username']
    # listname = result['playlistname']
    # song = result['song']
    play = db.playList
    res = []
    for x in play.find({"username":username},{'playlistName':1}):
        x['_id'] = str(x['_id'])
        res.append(x['playlistName'])
    return jsonify(
         res
    ),200