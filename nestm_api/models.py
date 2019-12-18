from django.db import models
from tenant_schemas.db import models
# Create your models here.
class Sample(models.TenantModel):
    name=models.CharField(max_length=12)