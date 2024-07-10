---
marp: true
size: 4:3
theme: shin
paginate: true
title: SW設計論 #15
---
<!-- _class: title -->
# ソフトウェア設計論 <div class="logo">#15</div>
## まつ本

---
<!-- _class: outline-->
# 開発者が知っておくべきトピック集<br><sub>－テスト編－</sub>
<div class="corner-triangle"><div class="corner-triangle-text"></div></div>

<span class="xisabled">・SWEBOK</span>

・テストはユーザ第1号である
・バグを直す前にテストを落とす
・リファクタリングする前にテストをする
・テストをしよう

---
# SWテスト
対象SWが意図通り動くかを検証するプロセス
下流工程の一つ, 実装とほぼ1:1

基本はSWを叩いてみて確認する
（コードレビューは叩かずに確かめる方法）

ソートプログラム `sort(arr)` に対するテスト
```java
@Test void testSort1() {
  expected = sort([1,2,3]);     // プログラムを叩いてみる
  assert(expected).is([1,2,3]); // その結果が正しいか検証
}
@Test void testSort2() {
  expected = sort([5,1,2]);
  assert(expected).is([1,2,5]);
}
@Test void testSortNull() {
  expected = sort(null);
  ...
```

---

# 様々なテスト
## 誰が叩くのか？
人が叩く：マニュアルテスト
機械が叩く：自動テスト

## どういう目線で叩くか？
中身を意識する：ホワイトボックス
中身を意識しない：ブラックボックス

## SWの何をテストするか？ (BBの場合)
機能 (単体テスト, 結合テスト, システムテスト)
非機能 (負荷テスト, パフォーマンステスト, ..)

---
<br><br><br><br>

> Program testing can be used to show the presence of bugs, but never to show their absence

> テストはバグが存在することを示せるが，バグがないことは示せない

<sub>Edsger W. Dijkstra</sub>