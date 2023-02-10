from django.shortcuts import render, redirect
from django.views import generic
from . import forms
from django.urls import reverse_lazy
from .models import MyModel
import os
from django.conf import settings

class MyCreateView(generic.CreateView):
    '''登録画面、登録確認画面用ビュー'''
    model = MyModel
    template_name = 'create.html'
    form_class = forms.MyModelForm
    success_url = reverse_lazy('sampleapp:create')

    def form_valid(self, form):
        '''バリデーションOKの処理'''
        response = super().form_valid(form)

        # どのボタンが押されたか判断
        if self.request.POST.get('action') == 'プレビュー':
            # プレビューボタンが押されたので、プレビュー画面に画像を渡す
            return render(self.request, 'confirm.html', {'image':self.object})
        else:
            # 登録ボタンが押された（プレビューでない、かつバリデーションOK）のでCreateViewのデフォルト処理
            return response

    def form_invalid(self, form):
        # キャンセルボタンが押された時
        if self.request.POST.get('action') == 'キャンセル':
            os.remove( # ファイル削除
                os.path.join( # 削除対象パスづくり（下２つをつなげる）
                    settings.MEDIA_ROOT, # MEDIA_ROOTで設定したフォルダ
                    str(MyModel.objects.last().col1 # 画像ファイル列の文字列
                    )
                )
            )
            # DBからも削除
            MyModel.objects.last().delete()
            # 終わったのでリダイレクト
            return redirect('sampleapp:create')

        # 普通にバリデーションNG
        return super().form_invalid(form)

