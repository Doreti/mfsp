#!/bin/bash
echo $teest
mongo << EOF
use mfspbd
db.user.insertOne({$userCollection})
db.question.insertOne({$questionsCollection})
EOF


