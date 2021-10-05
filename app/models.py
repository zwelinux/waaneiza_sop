from django.db import models
from django.contrib.auth.models import User, Group
from ckeditor.fields import RichTextField 

class Tag(models.Model):
	tag_name = models.CharField(max_length=255)

	def __str__(self):
		return self.tag_name

class Policy(models.Model):
	policy_title = models.CharField(max_length=255, help_text="စည်းကမ်းချက်အမည်")
	content = RichTextField(help_text="စည်းကမ်းချက်များ")
	date = models.DateField(help_text="ထုတ်ပြန်သည့်ရက်စွဲ")

	class Meta:
		verbose_name = "Policy"
		verbose_name_plural = "Policies"

	def __str__(self):
		return self.policy_title

class KnowledgeBase(models.Model):
	title = models.CharField(max_length=255, help_text='အကြောင်းအရာ')
	content = RichTextField(help_text='အချက်အလက်များ')
	public_view = models.BooleanField(default=False, help_text='အများပြည်သူကိုပြမည်။')
	date = models.DateTimeField(help_text='ထုတ်ပြန်သည့်ရက်စွဲ')

	def __str__(self):
		return self.title

class Procedure(models.Model):
	procedure_title = models.CharField(max_length=255, help_text="လုပ်ဆောင်မည့်အကြောင်းအရာခေါင်းစဉ်")
	tag = models.ManyToManyField(Tag, blank=True, help_text="အမျိုးအစား")
	policy = models.ForeignKey(Policy, on_delete=models.CASCADE, blank=True, help_text="စည်းကမ်းချက်များရွေးရန် (သို့မဟုတ်) အသစ်လုပ်ရန်")
	date = models.DateField(help_text="ထုတ်ပြန်သည့်ရက်စွဲ")

	def __str__(self):
		return self.procedure_title

class Document(models.Model):
	procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, help_text="လုပ်ဆောင်မည့်အကြောင်းအရာခေါင်းစဉ်")
	document_title = models.CharField(max_length=255, help_text="လုပ်ငန်းအမည်")
	content = RichTextField(help_text='လုပ်ငန်းအကြောင်းအရာ')
	my_order = models.PositiveIntegerField(default=0, blank=False, null=False, help_text='ဦးစားပေးအဆင့်သတ်မှတ်ချက်')
	date = models.DateTimeField()

	class Meta(object):
		ordering = ['my_order']

	def __str__(self):
		return self.document_title

