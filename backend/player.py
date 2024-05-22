#!/usr/bin/env python3
"""
Player Modul
"""
import re


class Player:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.email = kwargs.get('email', '')
        self.username = kwargs.get('username', '')
        self.password = kwargs.get('password', '')
        self.valid_to_participate = kwargs.get('valid_to_participate', False)
        self.is_winner = False

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'username': self.username,
            'password': self.password,
            'valid_to_participate': self.valid_to_participate
        }

    def validate_email(self):
        email_regex = r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$'
        return bool(re.match(email_regex, self.email))

    def validate_password(self):
        password_regex = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]).{8,}$'
        return bool(re.match(password_regex, self.password))

    def __str__(self) -> str:
        return f'''name: {self.name}
username: {self.username}
email: {self.email}
valid to participate: {self.valid_to_participate}'''
