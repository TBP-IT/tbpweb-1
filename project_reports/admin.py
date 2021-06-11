from django.contrib import admin

from tbpweb.project_reports.models import ProjectReport
from tbpweb.project_reports.models import ProjectReportFromEmail


class ProjectReportFromEmailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_prefix')


admin.site.register(ProjectReport)
admin.site.register(ProjectReportFromEmail, ProjectReportFromEmailAdmin)
