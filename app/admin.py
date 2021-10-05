from django.contrib import admin
from .models import Procedure, Document, Policy, Tag, KnowledgeBase
from adminsortable2.admin import SortableInlineAdminMixin

admin.site.index_title = 'Waaneiza Standard Operating Procedure'
admin.site.site_header = 'Waaneiza SOP'
admin.site.site_title = 'Waaneiza SOP Administration Panel'


class DocumentAdmin(admin.ModelAdmin):
	list_display = ['procedure', 'document_title', 'content', 'my_order', 'date']
	list_filter = ("procedure__procedure_title", 'my_order', 'date')
	search_fields = ['procedure__procedure_title', 'document_title', 'content', 'my_order', 'date']

class KnowledgeBaseAdmin(admin.ModelAdmin):
	list_display = ['title', 'content', 'public_view', 'date']
	list_filter = ['public_view', 'date']
	search_fields = ['title', 'content', 'public_view', 'date']

class PolicyAdmin(admin.ModelAdmin):
	list_display = ['policy_title', 'content', 'date']
	list_filter = ['date']
	search_fields = ['policy_title', 'content']

class DocumentInline(SortableInlineAdminMixin, admin.TabularInline):
	model = Document

class ProcedureAdmin(admin.ModelAdmin):
	inlines = [
		DocumentInline,
	]
	list_display = ['procedure_title', 'policy', 'date']
	list_filter = ['tag__tag_name', 'policy__policy_title', 'date']
	search_fields = ['procedure_title', 'tag__tag_name', 'policy__policy_title', 'date']



admin.site.register(Document, DocumentAdmin)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(Tag)
admin.site.register(KnowledgeBase, KnowledgeBaseAdmin)