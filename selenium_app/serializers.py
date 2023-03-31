from rest_framework import serializers
from selenium_app.models import SearchClass


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchClass
        fields = '__all__'