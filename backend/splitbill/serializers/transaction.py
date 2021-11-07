from rest_framework import serializers

from splitbill.models.transaction import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "created",
            "last_activity",
            "group_id",
            "owner_id",
            "name",
            "description",
            "amount",
            "type",
        ]
        read_only_fields = ["owner_id"]

    def update(self, instance, validated_data):
        validated_data.pop("group_id")
        return super().update(instance, validated_data)
