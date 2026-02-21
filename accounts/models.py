from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

username_validator = RegexValidator(
    regex=r"^[\w.@+\- ']+$",
    message=(
        "Enter a valid username. This value may contain letters, numbers, spaces, "
        "and @/./+/-/_/' characters."
    ),
)

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits, spaces and "
            "@/./+/-/_/' only."
        ),
        validators=[username_validator],
        error_messages={"unique": "A user with that username already exists."},
    )

    # here you can add any custom fields if necessary
    bio = models.TextField(null=True, blank=True)



