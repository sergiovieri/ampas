from rest_framework import serializers

from splitbill.models.userbalance import UserBalance


class UserBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBalance
        fields = [
            "id",
            "group_id",
            "user_id",
            "balance",
        ]

    def update(self, instance, validated_data):
        validated_data.pop("group_id")
        validated_data.pop("user_id")
        return super().update(instance, validated_data)
