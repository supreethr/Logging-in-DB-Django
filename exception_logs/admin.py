from django.contrib import admin
from exception_logs import models as exception_log_models

admin.site.register(exception_log_models.DBLogEntry)
admin.site.register(exception_log_models.GeneralLog)
admin.site.register(exception_log_models.SpeicalLog)
