from statistics import mode
from django.db import models
from django.db.models.query import F, Q
from django.utils import timezone
# from app.companies.models import Company


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CompanyBaseModel(models.Model):
    company = models.ForeignKey("companies.Company", on_delete=models.SET_NULL, blank=True, null=True, default=None)

    class Meta:
        abstract = True

class RandomModel(BaseModel):
    """
    This is an example model, to be used as reference in the Styleguide,
    when discussing model validation via constraints.
    """
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="start_date_before_end_date",
                check=Q(start_date__lt=F("end_date"))
            )
        ]
