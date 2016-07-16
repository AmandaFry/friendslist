from system.core.model import Model
from flask import Flask, flash, session
from datetime import datetime
import re

NOSPACE_REGEX = re.compile(r'^[a-zA-Z0-9]*$')

class FriendModel(Model):
    def __init__(self):
        super(FriendModel, self).__init__()
 
    def my_friends(self):
        query = "SELECT * FROM users JOIN friendslist ON users.id = friendslist.user_id WHERE user_id =:id"
        data = { 'id' : session['id']}
        my_friends = self.db.query_db(query, data)
        return (my_friends)

    def not_friends(self):
        query = "SELECT users.first_name, users.alias, users.id FROM users LEFT JOIN friendslist ON users.id = friendslist.user_id"
        not_friends = self.db.query_db(query)
        return (not_friends)

    def profile(self, id):
        query = "SELECT * FROM users WHERE id = :id"
        data = { 'id' : id }
        profile = self.db.query_db(query, data)
        return (profile)

    def add_friend(self,id):
        query = "INSERT INTO friendslist (user_id, friend_id, created_at, updated_at) VALUES (:id, :friend_id, NOW(), NOW())"
        data = {
            'id' : session['id'],
            'friend_id' : id,
        }
        add_friend = self.db.query_db(query, data)
        return (add_friend)


    def remove_friend(self, id):
        query = "DELETE FROM friendslist WHERE user_id = :id AND friend_id = :friend_id"
        data = {
            'id' : session['id'],
            'friend_id' : id,
        }
        remove_friend = self.db.query_db(query, data)
        return {'status':True}
