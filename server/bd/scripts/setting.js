#!/bin/bash
echo $teest
mongo << EOF
use mfspbd
db.user.insertOne({$teest})
EOF






