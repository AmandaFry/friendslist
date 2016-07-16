from system.core.model import Model
from flask import Flask, flash, session
from datetime import datetime
import re

NOSPACE_REGEX = re.compile(r'^[a-zA-Z0-9]*$')

class FriendModel(Model):
    def __init__(self):
        super(FriendModel, self).__init__()
 
    def my_friends(self):
        query = "SELECT * FROM friendslist WHERE user_id = :id"
        data = { 'id' : session['id']}
        my_friends = self.db.query_db(query, data)
        return (my_friends)

    def not_friends(self):
        query = "SELECT users.first_name, users.alias, users.id FROM users LEFT JOIN friendslist ON users.id = friendslist.user_id"
        not_friends = self.db.query_db(query)
        return (not_friends)

    def profile(self, id):
        pass

    def add_friend(self,id):
        pass
    
    #     query = "SELECT * from trips where organizer_id = :id"
    #     data = {'id': session['id']}
    #     return self.db.query_db(query, data)

    # def add_trip(self, trip_info):
    #     travel_erorrs = []
    #     print "I made it to travel model"
    #     trip_info = {
    #         'destination' : trip_info['destination'],
    #         'plan' : trip_info['plan'],
    #         'start_date' : trip_info['start_date'],
    #         'end_date' : trip_info['end_date']
    #     }
    #     print ('*' * 25)
    #     print trip_info
    #     print ('*' * 25)

    #     today = datetime.now().strftime("%Y-%m-%d")
    #     print ('^' * 25)
    #     print today
    #     print "User logged in: ", session['id']
    #     print ('^' * 25)
        
    #     if len(trip_info['destination']) < 2:
    #         travel_erorrs.append("Please enter a valid destination")
    #     elif len(trip_info['plan']) < 2:
    #         travel_erorrs.append("Please enter a valid plan")
    #     # elif not NOSPACE_REGEX.match(trip_info['plan']):
    #     #     travel_erorrs.append("Plan cannot be just spaces")
    #     elif today > trip_info['start_date']:
    #         travel_erorrs.append("Start date must be in the future")
    #     elif today > trip_info['end_date']:
    #         travel_erorrs.append("End date must be in the future")
    #     elif trip_info['start_date'] >= trip_info['end_date']:
    #         travel_erorrs.append("Start date must be before end date")
    #     if travel_erorrs:
    #         return {"status": False, "errors": travel_erorrs}
    #     else:
    #         sql = "INSERT into trips (organizer_id, destination, plan, start_date, end_date, created_at, updated_at) values(:organizer_id, :destination, :plan, :start_date, :end_date, NOW(), NOW())"
    #         data = {
    #             'organizer_id': session['id'], 
    #             'destination': trip_info['destination'],
    #             'plan' : trip_info['plan'],
    #             'start_date' : trip_info['start_date'],
    #             'end_date' : trip_info['end_date'] 
    #         }
    #         self.db.query_db(sql, data) #run the insert
    #         return {"status": True}

    # def my_trip(self):
    #     query = "SELECT * from trips where organizer_id = :id"
    #     data = {'id': session['id']}
    #     return self.db.query_db(query, data)

    # def trip_joined(self):
    #     # query = "SELECT * from travel_friends where friend_id = :id"
    #     query = "SELECT trips.id, trips.destination, trips.start_date, trips.end_date, trips.plan FROM trips JOIN travel_friends ON trips.id = travel_friends.trip_id WHERE travel_friends.friend_id = :id"
    #     data = {'id': session['id']}
    #     return self.db.query_db(query, data)

    # def friends_joined(self, id):
    #     # query = "SELECT users.first_name, users.last_name FROM users JOIN trips ON users.id = trips.organizer_id WHERE organizer_id != :id"
    #     query = "SELECT DISTINCT (users.first_name), users.last_name FROM users JOIN travel_friends ON users.id = travel_friends.friend_id  WHERE travel_friends.trip_id = :id"
    #     data = {'id': id}
    #     return self.db.query_db(query, data)

    # def others_trip(self):
    #     # query = "SELECT * from trips where organizer_id != :id"
    #     query = "SELECT users.first_name, users.last_name, trips.destination, trips.start_date, trips.end_date, trips.id FROM users JOIN trips ON users.id = trips.organizer_id WHERE organizer_id != :id"
    #     data = {'id': session['id']}
    #     # result_mytrip = self.db.get_one(query, data)
    #     # return {"status": True, 'mytrips': mytrips}
    #     return self.db.query_db(query, data)

    # def trip_details(self, id):
    #     query = "SELECT users.first_name, users.last_name, trips.destination, trips.plan, trips.start_date, trips.end_date FROM users JOIN trips ON users.id = trips.organizer_id WHERE trips.id = :id"
    #     # query = "SELECT * from trips where id = :id"
    #     data = {'id': id}
    #     return self.db.query_db(query, data)

    # def join_trip(self, id):
    #     query = "INSERT into travel_friends (trip_id, friend_id, created_at, updated_at) values(:trip_id, :friend_id, NOW(), NOW())"
    #     data = {
    #         'trip_id': id,
    #         'friend_id': session['id'] 
    #     }
    #     return self.db.query_db(query, data) #run the insert