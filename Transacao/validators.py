from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_data_nao_futura(value):
    if value > timezone.now().date():
        raise ValidationError("A data da transação não pode ser no futuro.")
