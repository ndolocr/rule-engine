from django.db import models

# Create your models here.

class Rule(models.Model):
    class Meta:
        db_table = "rules"

    action = models.TextFiled()
    condition = models.TextFiled()
    priority = models.IntegerField()
    description = models.TextFiled()
    rule_id = models.CharField(max_length = 512)
    ruleNamespace = models.CharField(max_length = 256)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)