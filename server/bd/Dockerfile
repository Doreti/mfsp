FROM mongo:4.0-xenial
WORKDIR /settings
COPY scripts/setting.sh /settings
RUN chmod +x setting.sh
EXPOSE 27017 
#CMD [ "./setting.sh" ]
#db.questions.insertOne(${questionsCollection})
#db.users.insertOne(${userCollection})
