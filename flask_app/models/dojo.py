from types import ClassMethodDescriptorType
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'dojo_survey_schema'

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"

        return connectToMySQL(db).query_db(query, data)

    
    @classmethod
    def get_ninja(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"

        result = connectToMySQL(db).query_db(query, data)

        ninja = []

        for row in result:
            ninja.append(cls(row))


        return ninja




    # =============================================
    # Validate Method
    # =============================================

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True

        print(f'77777777777777777777777777777name:{len(dojo["name"])}')
        if len(dojo['name']) < 3:
            flash('Name must be at least 3 characters')
            is_valid = False

        print(f'77777777777777777777777777777name:{len(dojo["location"])}')
        # GETTING A KEYERROR HERE ON 'location' WHEN LEFT BLANK.....DONT KNOW WHY?
        if len(dojo['location']) < 1:
            flash('Please select a location')
            is_valid = False

        print(f'77777777777777777777777777777name:{len(dojo["language"])}')
        # GETTING A KEYERROR HERE ON 'language' WHEN LEFT BLANK.....DONT KNOW WHY?
        if len(dojo['language']) < 1:
            flash('Please select a favorite langauge')
            is_valid = False
        return is_valid
        
        
