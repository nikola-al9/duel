from config.env import env

EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
EMAIL_USE_SSL = env.bool('EMAIL_USE_SSL', default=False)  # Set to True if using SSL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Use the default backend for simplicity
EMAIL_HOST = env('EMAIL_HOST', default='smtp.example.com')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='your_password')
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='your_email@example.com')
EMAIL_PORT = env.int('EMAIL_PORT', default=587)  # Use 465 for SSL
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER