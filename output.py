#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import datetime
import os
import subprocess

#sysというライブラリを使って、コマンドで入力した引数を取得しています
#argsという配列に取得した引数を格納しています
args = sys.argv

#現在の時間を取得しています。
today = str(datetime.datetime.now())

#osというライブラリで現在のカレントディレクトリのパスを取得する
#現在のパスに作成された「test_py.html」のパスを作成する
path = os.getcwd() + "/test_py.html"

#ターミナルで入力するコマンドを作成する
cmd = 'open ' + path

#作成するファイルの存在確認をする
#ファイルが存在する場合は処理を中止
if os.path.exists(path):
    print("ファイルがすでに存在します。")
    sys.exit()

#新規で「test_py.html」というhtmlファイルを作成して、「w」書き込みを行います
f = open('test_py.html','w')
#新規で作成した空のファイルにhtmlコードを記述していきます
#f.write("""ここに記述する。変数1：%s 変数2：%s""" %(変数1,変数2))
#書き込んだ後は必ずcloseする
f.write("""
<!DOCTYPE html>
<html>
<head><title>Web App Creators</title></head>
<body>
<h1>
これはPythonの実行結果として生成されたHTMLです<br>
現在時刻は%sです
</h1>
<h2>
<ul>
<li>第1引数：%s</li>
<li>第2引数：%s</li>
<li>第3引数：%s</li>
</ul>
</h2>
</body></html>
"""%(today,args[1],args[2],args[3]))
f.close()

#subprocessというライブラリでターミナルでのコマンド入力を行う
subprocess.check_call(cmd.split())
