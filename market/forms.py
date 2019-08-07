from django import forms


class IssueForm(forms.Form):
    types = (
        ('出售', '出售'),
        ('求购', '求购'),
    )
    grades = (
        ('大一', '大一'),
        ('大二', '大二'),
        ('大三', '大三'),
        ('大四', '大四'),
    )
    majors = (
        ('生物信息学', '生物信息学'),
        ('药学', '药学'),
        ('软件工程', '软件工程'),
    )
    username = forms.CharField(label="用户名", max_length=128)
    bookname = forms.CharField(label="书名", max_length=128)
    price = forms.CharField(label="价格", max_length=128)
    major = forms.ChoiceField(label="专业", choices=majors)
    grade = forms.ChoiceField(label="年级", choices=grades)
    qq = forms.CharField(label="QQ", max_length=128)
    pic = forms.CharField(label="图片", max_length=128)
    type = forms.ChoiceField(label='类型', choices=types)

class SearchForm(forms.Form):
    types = (
        ('出售', '出售'),
        ('求购', '求购'),
    )
    grades = (
        ('大一', '大一'),
        ('大二', '大二'),
        ('大三', '大三'),
        ('大四', '大四'),
    )
    majors = (
        ('生物信息学', '生物信息学'),
        ('药学', '药学'),
        ('软件工程', '软件工程'),
    )
    major = forms.ChoiceField(label="专业", choices=majors)
    grade = forms.ChoiceField(label="年级", choices=grades)
    type = forms.ChoiceField(label='类型', choices=types)