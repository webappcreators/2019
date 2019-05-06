# Web App Creators Vol.1

- 今回の wac 勉強会の資料

## 開発環境について
- バージョン管理システム：[Github](https://github.com/)
- サーバー：[さくらVPSサーバー](https://vps.sakura.ad.jp/)  
一番安価なプランを契約して使用する。

- 使用言語：Python3

## 開発ツールの紹介、準備
- macbook
- Github
- さくらVPSサーバー
- Python3
- atom

## ローカル環境でhtmlファイルをwebブラウザで開く
シンプルテキストでHTMLファイルを作成し、ローカル環境でwebブラウザを開く。  
ターミナルを開き、ホームディレクトリに作業用ディレクトリを作成する。  
````
$ mkdir test  
$ cd test  
````
テキストエディタを開き新規ファイルでtest.htmlファイルを作成する。  
以下のコードを記述し、保存する。
````
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Web App Creators</title>
</head>
<body>
<h1 class="title">ローカル環境でHTMLファイルを表示しよう</h1>
</body>
</html>
````
webブラウザで作成したhtmlファイルを開く  
````
$ open test.html
````

## ローカル環境でpythonをつかってhtmlファイルを作成する
Python3を使ってHTMLファイルを作成し、ローカル環境でwebブラウザを開く

## 公開用サーバーの準備
さくらVPSでのシステムの基本設定
- [os_sakuravps - sakura vps](https://github.com/ykHakata/summary/blob/master/os_sakuravps.md) でのシステムの基本設定
- [security_sakuravps](https://github.com/ykHakata/summary/blob/master/security_sakuravps.md) - 最低限のセキュリティの設定
- [ssh_sakuravps](https://github.com/ykHakata/summary/blob/master/ssh_sakuravps.md) - ssh 設定 sakura vps と github

## webサーバー nginx の準備
- [nginx_sakuravps](https://github.com/ykHakata/summary/blob/master/nginx_sakuravps.md) - sakura vps での nginx の基本設定


## githubを使ったローカル環境と公開サーバーとの連携


## テストファイルにアクセスする


##

##
