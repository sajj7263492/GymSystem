from django.contrib import admin
from gymfitness.models import Contact,Enrollment,MembershipPlan, Gallery
from gymfitness.models import Trainer
from gymfitness.models import Attendance

# Register your models here.
admin.site.register(Contact)
admin.site.register(Enrollment)
admin.site.register(MembershipPlan)
admin.site.register(Trainer)
admin.site.register(Gallery)
admin.site.register(Attendance)
