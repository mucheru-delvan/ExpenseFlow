from rest_framework import serializers

from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        #I did not include the user field in the serializer because it will be automatically set to the authenticated user in the view.
        fields = [
            "id",
            "title",
            "amount",
            "date",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]