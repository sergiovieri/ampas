from rest_framework import serializers

from splitbill.models.usergroup import UserGroup


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ["id", "created", "last_activity", "name", "discord_server_id"]
