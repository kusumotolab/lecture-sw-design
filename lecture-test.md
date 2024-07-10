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
・テストは証明ではない
・テストをしよう

---
# SWテスト
対象SWが意図通り動くかを検証するプロセス
下流工程の一つ, 実装とほぼ1:1

基本はSWを叩いてみて確認する
<sub>（コードレビューは叩かずに確かめる方法）</sub>

ソートプログラム `sort(arr)` に対するテスト
```java
@Test void testSort1() {
  actual = sort([1,2,3]);     // プログラムを叩いてみる
  assert(actual).is([1,2,3]); // その結果が正しいか検証
}
@Test void testSort2() {
  actual = sort([3,1,2]);
  assert(actual).is([1,2,3]);
}
@Test void testSortNull() {
  actual = sort(null);
...
```

---

# 様々なテスト
## 誰が叩くのか？
人が叩く：マニュアルテスト
機械が叩く：自動テスト (ユニットテスト)

## どういう目線で叩くか？
中身を意識する：ホワイトボックス
中身を意識しない：ブラックボックス

## SWの何をテストするか？
機能：単体テスト, 結合テスト, システムテスト
非機能：パフォーマンステスト, 負荷テスト, ..

---
# テストを書こう
## 実装したら即テストを書く
インタフェースを決める
```java
List sort(List);
```

実装する
```java
List sort(List l) {
  for ..
    ..
```

テストする (実装より先でもOK)
```java
@Test void testSort1() {
  assert(sort([1,2,3])).is([1,2,3]);
}
```

`要求` + `I/F` 

---

インタフェースを決める
```java
python analyze.py in out
```

実装する
```python
def analyze(in_file, out_file):
  f = open(in_file);
  ..
```

テストする (実装より先でもOK)
```python
def test_analyze(self):
  analyze("test/in.txt", "test/out.txt");
  assert("test/out.txt") ..
```

---
<br><br><br><br>

> Program testing can be used to show the presence of bugs, but never to show their absence

> テストはバグが存在することを示せるが，バグがないことは示せない

<sub>Edsger W. Dijkstra</sub>