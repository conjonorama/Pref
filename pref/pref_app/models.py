from django.db import models

# Security identifier model
class SecurityIdentifier(models.Model):
    CUSIP = models.CharField(length=12, primary_key=True),
    full_symbol = models.CharField(max_length=8),
    short_symbol = models.CharField(max_length=10)

# Security type model
class SecurityType(models.Model):
    security_type = models.CharField(max_length=20),
    description = models.CharField(max_length=100)

class Ratings(models.Model):
    rating = models.CharField(max_length=10),
    description = models.CharField(max_length=100)

# Sector model
class Sector(models.Model):
    sector = models.CharField(max_length=10),
    description = models.CharField(max_length=100)

# Industry model
class Industry(models.Model):
    industry = models.CharField(max_length=10),
    description = models.CharField(max_length=100)

# Secuirty description model
class SecurityDescription(models.Model):
    CUSIP = models.ForeignKey(SecurityIdentifier, on_delete=models.CASCADE),
    description = models.CharField(max_length=100),
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE),
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE),
    securitytype = models.ForeignKey(SecurityType, on_delete=models.CASCADE)

# Security price model
class SecurityPrice(models.Model):
    CUSIP = models.ForeignKey(SecurityIdentifier, on_delete=models.CASCADE),
    date = models.DateField(),
    price = models.DecimalField(max_digits=10, decimal_places=2),
    volume = models.IntegerField(),
    rating = models.ForeignKey(Ratings, on_delete=models.CASCADE),
    yield_pct = models.DecimalField(max_digits=10, decimal_places=2),
    # f2_week_high = models.DecimalField(max_digits=10, decimal_places=2),
    # f2_week_low = models.DecimalField(max_digits=10, decimal_places=2),

# ToDo: 
# 1. Add a model for the reference securities price history (i.e. government bonds, treasury bills, etc.)
# 2. Add a model for the reference securities description (i.e. government bonds, treasury bills, etc.)


