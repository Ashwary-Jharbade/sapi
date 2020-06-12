from rest_framework import serializers

class SearchSerializers(serializers.Serializer):
    '''Features of serializers'''
    sname = serializers.CharField(max_length=100)
