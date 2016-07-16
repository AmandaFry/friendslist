from system.core.controller import *
from flask import Flask, flash, session, request, redirect

class Friend(Controller):
    def __init__(self, action):
        super(Friend, self).__init__(action)
        self.load_model('FriendModel')
        # self.db = self._app.db

    def dashboard(self):
        # friend = self.models['FriendModel'].my_friends()
        # print ('%' * 25)
        # print friend
        # print ('%' * 25)
        # not_friend = self.models['FriendModel'].not_friend()
        # print ('!' * 25)
        # print others_trip
        # print ('!' * 25)
        # return self.load_view('dashboard.html', mytrips=mytrips, trips_joined=trip_joined, others_trips=others_trip)
        return self.load_view('dashboard.html')


    # def add_travel(self):
    #     return self.load_view('addplan.html')

    # def add_plan(self):
    #     trip_info = {
    #         'destination' : request.form['destination'],
    #         'plan' : request.form['plan'],
    #         'start_date' : request.form['start_date'],
    #         'end_date' : request.form['end_date']
    #     }
    #     trips = self.models['FriendModel'].add_trip(trip_info)

    #     if  trips['status'] == False:
    #         #switch error message from array to Falsh and redirect to login page again
    #         for message in trips['errors']:
    #             flash(message)
    #         return self.load_view('addplan.html')
    #         # return redirect('/dashboard')
    #     else:
    #         # return self.load_view('addplan.html')
    #         return redirect('/dashboard')

    # def dashboard(self):
    #     mytrips = self.models['FriendModel'].my_trip()
    #     print ('%' * 25)
    #     print mytrips
    #     print ('%' * 25)
    #     trip_joined = self.models['FriendModel'].trip_joined()
    #     print ('$' * 25)
    #     print trip_joined
    #     print ('$' * 25)
    #     others_trip = self.models['FriendModel'].others_trip()
    #     print ('!' * 25)
    #     print others_trip
    #     print ('!' * 25)
    #     return self.load_view('dashboard.html', mytrips=mytrips, trips_joined=trip_joined, others_trips=others_trip)

    # def details(self, id):
    #     trip_details = self.models['FriendModel'].trip_details(id)
    #     print ('~' * 25)
    #     print trip_details
    #     print ('~' * 25)
    #     friends_joined = self.models['FriendModel'].friends_joined(id)
    #     return self.load_view('details.html', trip_details=trip_details, friends_joined=friends_joined)

    # def join_trip(self, id):
    #     join_trip = self.models['FriendModel'].join_trip(id)
    #     print ('/' * 25)
    #     print join_trip
    #     print ('/' * 25)
    #     return redirect('/dashboard')