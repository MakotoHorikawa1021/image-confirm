from django.shortcuts import render, redirect
from django.views import generic
from . import forms
from django.urls import reverse_lazy
from .models import MyModel
import os
from django.conf import settings

class MyCreateView(generic.CreateView):
    '''
    登録画面、登録確認画面用ビュー
    登録処理の前にプレビュー画面を割り込ませるイメージ
    '''

    model = MyModel # モデルは画像だけのやつ
    template_name = 'create.html' # 登録画面
    form_class = forms.MyModelForm # 画像だけのフォーム
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
            # 直前に入れたレコード情報を取得
            image = MyModel.objects.last()
            # ファイルを削除
            image.col1.delete()
            # DBからも削除
            image.delete()
            # 終わったのでリダイレクト
            return redirect('sampleapp:create')

        # 普通にバリデーションNG
        return super().form_invalid(form)

