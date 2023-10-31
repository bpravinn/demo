from .base import * #noqa
from .base import env


SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
     default="zU-ntPMiRM39w-lWB9-jpwi6Lckk2s5K2h2uq8lFsof5b7ITo2k",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["https://localhost:4200", "https://pravinbhati.com"]