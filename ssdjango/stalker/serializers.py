__author__ = 'shawn'

from rest_framework import serializers

from .models import Accounts, History


"""
Account Serializers
"""

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accounts

class HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = History