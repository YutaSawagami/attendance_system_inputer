# attendance_system_inputer

自動で勤怠システムを入力してくれるプログラム

## 実行方法
chrome用のwebdriverを[公式サイト](https://chromedriver.chromium.org/downloads)からインストールして`/usr/local/bin`に配置  
`pipenv install`でpipfileをもとに必須モジュールをインストール  
`auto_enavi.sh`の環境変数を自身の値に設定、`URL`はenaviログイン画面のURL  
chmodコマンドで実行権限を付与して、`./auto_enavi.sh`で実行
