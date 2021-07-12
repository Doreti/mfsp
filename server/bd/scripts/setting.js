use mfspbd
db.users.insertOne({_id: ObjectId("5099803df3f4948bd2f98391"),"admin": {"password": "admin","role": "admin", "user_id": "qwerty123", "achievements": ["arch1", "Arch2"]}})
db.getCollectionNames()



#!/bin/bash
teest="\"password__\": \"admin\""
echo $teest
mongo << EOF
use mfspbd
db.user.insertOne({$userCollection})
EOF






