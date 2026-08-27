from datetime import timedelta

from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Expense.objects.filter(user=self.request.user)

        period = self.request.query_params.get("period")
        today = timezone.localdate()

        if period == "week":
            start_date = today - timedelta(days=7)
            queryset = queryset.filter(date__gte=start_date)

        elif period == "month":
            start_date = today - timedelta(days=30)
            queryset = queryset.filter(date__gte=start_date)

        elif period == "3months":
            start_date = today - timedelta(days=90)
            queryset = queryset.filter(date__gte=start_date)

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")

        if start_date:
            queryset = queryset.filter(date__gte=start_date)

        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)