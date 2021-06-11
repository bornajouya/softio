from rest_framework import serializers
from chatAPI.models import chat


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = chat

        fields = ('id', 'user', 'text', 'time', 'ads','isfirst')