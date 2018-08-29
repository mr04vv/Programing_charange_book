# Programing_charange_book

## 使い方 [例]

使用するときはブランチを切ってから作業してください
```
git checkout -b mori/2-1_bubunwa // ブランチが存在するときは-bオプションはいりません
```
###  自分が解く場合
1. 自分のディレクトリを作成
```
mkdir mori
cd mori
```
2. 問題の章のディレクトリを作成
```
mkdir 2-1
cd 2-1
```
3. 解く問題のファイルを作成（何回目か書くとわかりやすい）
```
touch bubunwa-1.py  // 部分和問題1回目
```
4. 問題を解く
5. 解いたらとりあえずpush
```
git add ./
git commit -m "コミットメッセージ"
git push origin [ブランチ名]
```
6. githubに移動してmaster対象のプルリクエストを投げる
 - 上に黄色いのが出てきた場合
 ![2018-08-29 15 53 13](https://user-images.githubusercontent.com/24749358/44770780-162f8780-aba4-11e8-909c-7a4e9fd27aca.png)

 1. 緑のCompare & pull requestをクリック
![2018-08-29 15 51 25](https://user-images.githubusercontent.com/24749358/44770868-5abb2300-aba4-11e8-97cf-83ffcb76c220.png)
 
 2. Create pull requestを押す

 3. 完了

 - 上に黄色いのが出てこなかった場合（たまに緑のCompare & pull requestが出てこないことがあります）
 ![2018-08-29 15 50 15](https://user-images.githubusercontent.com/24749358/44770962-9c4bce00-aba4-11e8-8998-ec004fd4d1d0.png)
 
 1. 画像の左側のボタンで自分がpushしたブランチを選択

 2. 右のボタンでNew pull request 

 3. 緑のCreate pull requestを押す
 
 4. 完了
### 他の人のコードを見る場合

1. プルリクエストを確認

コメントを適宜追加


うまく活用していきましょう！！
