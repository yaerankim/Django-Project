from django.contrib import admin
from todo_app.models import ToDoItem, ToDoList

# 커스터마이징 class. 상위 모델에서 하위 모델의 설정을 한번에 설정하고자 할 경우
class ToDoItemInline(admin.StackedInline):
    model = ToDoItem
    extra = 3

class ToDoListAdmin(admin.ModelAdmin):
    inlines = [ToDoItemInline]

# 커스터마이징 class 1) 소수의 field 보유
# class ToDoItemAdmin(admin.ModelAdmin):
#     fields = ["todo_list", "title", "due_date", "description"]

# 커스터마이징 class 2) 다수의 field 보유 - fieldset 사용
class ToDoItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Belongs to', {'fields' : ['todo_list']}),
        ('Detail', {'fields' : ['title', 'description']}),
        ('Date information', {'fields' : ['due_date']}),
    ]

admin.site.register(ToDoList, ToDoListAdmin)

# 1) 커스터마이징 없이 기본적으로 register할 경우
# admin.site.register(ToDoItem)

# 2) 커스터마이징 옵션 추가하여 register할 경우
# ex) ToDoItem 클래스의 field 순서를 바꾸는 커스터마이징 옵션을 추가
admin.site.register(ToDoItem, ToDoItemAdmin)