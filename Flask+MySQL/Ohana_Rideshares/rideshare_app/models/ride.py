from rideshare_app.config.mysqlconnection import connectToMySQL
from rideshare_app import db


class Ride:
    def __init__(self, data):
        self.id = data['id']
        self.destination = data['destination']
        self.pick_up_localisation = data['pick_up_localisation']
        self.redeshares_date = data['redeshares_date']
        self.detail = data['detail']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = None

    @classmethod
    def save(cls, data):
        query ="INSERT INTO ohana_rideshares (destination, pick_up_localisation, redeshares_date, detail) VALUES (%(destination)s,%(pick_up_localisation)s,%(redeshares_date)s,%(detail)s);"
        result = connectToMySQL(db).query_db(query, data)
        return result
    
    @classmethod
