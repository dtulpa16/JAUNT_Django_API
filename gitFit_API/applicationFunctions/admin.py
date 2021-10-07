from django.contrib import admin
from .models import ClientTrainer
from .models import ForumPost
from .models import ForumReply
from .models import TrainerReview
from .models import TrainerBlog
from .models import Workout

# Register your models here.

admin.site.register(ClientTrainer)
admin.site.register(ForumPost)
admin.site.register(ForumReply)
admin.site.register(TrainerReview)
admin.site.register(TrainerBlog)
admin.site.register(Workout)
