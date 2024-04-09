from unicodedata import category
from django import forms
from .models import Category


class UserSearchForm(forms.Form):
    EXPORT_TYPE = (
        ("csv", "CSV"),
        ("json", "JSON"),
        ("xls", "XLS"),
    )
    SEARCH_TYPE = (
        ("by_keyword", "By Keyword"),
        ("daily_search", "Daily Search")
    )
    search_type = forms.ChoiceField(label="Search Type", choices=SEARCH_TYPE,)
    keyword = forms.CharField(label="Keyword", max_length=255)
    page_count = forms.IntegerField(
        label="Number of Pages to Search", max_value=100, min_value=1, initial=1
    )
    file_type = forms.ChoiceField(
        label="File Type",
        choices=EXPORT_TYPE,
        initial="JSON",
    )


class CategoryReportForm(forms.Form):
    REPORT_STATUS = (
        ("show", "SHOW"),
        ("dont_show", "Don't SHOW"),
    )
    report = forms.ChoiceField(
        label="Select Category",
        choices=REPORT_STATUS,
        initial=None,
    )
