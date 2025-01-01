from django import forms
from .models import Order, Evaluation
from user_management.models import Address


class OrderForm(forms.ModelForm):
    address = forms.ModelChoiceField(queryset=Address.objects.none(), label="Select Address")

    class Meta:
        model = Order
        fields = ['address']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['address'].queryset = Address.objects.filter(user=user)


class DirectOrderForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label="Quantity")
    address = forms.ModelChoiceField(queryset=Address.objects.none(), label="Select Address")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['address'].queryset = Address.objects.filter(user=user)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['score', 'comments']
        widgets = {
            'score': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comments': forms.Textarea(attrs={'rows': 4, 'placeholder': '请输入您的评价...'}),
        }
        labels = {
            'score': '评分',
            'comments': '评论',
        }