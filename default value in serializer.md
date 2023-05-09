class ChatSerializerPost(serializers.ModelSerializer):
    name = serializers.CharField(default='My Chat Room')

    class Meta:
        model = Chat
        fields = ['name', 'members']
