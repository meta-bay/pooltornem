#!/usr/bin/env python3
"""
Storage Module
"""
from pymongo import MongoClient
from backend.player import Player


class Storage:
    """
    Storage Class for MongoDB
    """

    mongo_uri = 'mongodb://localhost:27017/'
    database_name = 'pooltornem-test'
    collection_name = 'players'

    def __init__(self):
        """Initialize"""
        self.client = MongoClient(self.mongo_uri)
        self.database = self.client[self.database_name]
        self.collection = self.database[self.collection_name]

    def save(self, player):
        """Save instance"""
        player_dict = player.to_dict()
        self.collection.insert_one(player_dict)

    def get_player_by_email(self, email):
        """Fetch player instance by email"""
        player_dict = self.collection.find_one({'email': email})
        if player_dict:
            return self._create_player_instance(player_dict)
        return None

    def get_player_by_username(self, username):
        """Fetch player instance by username"""
        player_dict = self.collection.find_one({'username': username})
        if player_dict:
            return self._create_player_instance(player_dict)
        return None

    def _create_player_instance(self, player_dict):
        """Create player instance from the fetchec dict"""
        return Player(**player_dict)

    def check_save(self, player):
        """Check for existing instance before saving"""
        email = player.email
        username = player.username

        if self.get_player_by_email(email):
            raise ValueError(f"Email '{email}' is already registered.")

        if self.get_player_by_username(username):
            raise ValueError(f"Username '{username}' is already registered.")

        self.save(player)

    def get_all_players(self):
        """Fetch all player instances from the database"""
        player_dicts = self.collection.find()
        players = []
        for player_dict in player_dicts:
            player = self._create_player_instance(player_dict)
            players.append(player)
        return players

    def delete_player_by_email(self, email):
        """Delete a player instance from the database by email"""
        result = self.collection.delete_one({'email': email})
        return result.deleted_count > 0

    def close_connection(self):
        """Close mongoDB connection"""
        self.client.close()
