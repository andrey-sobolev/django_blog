from rest_framework import serializers


class AnaliticSerializer(serializers.Serializer):
    date_from = serializers.DateField()
    date_to = serializers.DateField()
    
    def validate(self, data):
        date_from = data['date_from']
        date_to = data['date_to']
        if date_from > date_to:
            raise serializers.ValidationError('date_from should be <= of date_to')
        return data
