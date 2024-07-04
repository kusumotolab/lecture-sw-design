---
marp: true
size: 4:3
theme: shin
paginate: true

---
<!-- _class: title -->
# ソフトウェア設計論 `#11`
## まつ本

---
# 何の授業をしようか･･･
## SW設計の内容であること
単なる前提，でもとんでもなく広い

## 被らないこと
SW設計論13回 (楠本) 要求･見積･RFP
SW開発論15回 (肥後) 要求･設計･実装･テスト

## 役立つ内容にしたい
情報科学研究科の最大公約数を
幸いSW設計周りは汎用的で役に立ちやすい

## 知らなさそうな話をしたい
B3授業 (演習D･実験B) の経験から考える

---
# 目次
## SW開発者が知るべきトピック集（実装編）
SWEBOK
良い名前をつける
動くの先にある良いプログラム
そもそも良いプログラムとは？
Don't call us, we'll call you
gotoはなぜだめなのか？
できないことを増やす
<!--span class="disabled">bb<span-->


---
# ソフトウェア工学基礎知識体系
## SWEBOK
Software Engineering Body of Knowledge
IEEEが作っているSEの知識体系

知識や概念の「体系化･構造化」が目的
例：生物分類 `脊索動物門 > 哺乳綱 > サル目 > サル科 > ...`

内容は薄くて広い
構造付きの辞書とみなすと良い


## 他にもいろいろなBOKがある
Project Management BOK
Data Management BOK
主にIT系分野

---
# SWEBOK 目次
## 全15章
```
1. SW要求
2. SW設計
3. SW構築
4. SWテスティング
5. SW保守
6. SW構成管理
7. SWエンジニアリング・マネージメント
8. SWエンジニアリングプロセス
9. SWエンジニアリングモデルおよび方法
10. SW品質
11. SWエンジニアリング専門技術者実践規律
12. SWエンジニアリング経済学
13. 計算基礎
14. 数学基礎
15. エンジニアリング基礎
```

---
# SWEBOK 目次
## SW設計の部分を抜粋
```
2. SW設計
  - SW設計の基礎
  - SW設計における主要な問題
    - 並行処理
    - イベントに対する制御と処理
    - データの永続化
    - コンポーネントの分散化
    - エラー・例外処理
    - 対話と表示
    - セキュリティ
  - SW構造とアーキテクチャ
  - UI設計
  - SW設計品質の分析と評価
  - SW設計のための表記
  - ...
```

---
# SWEBOK 目次
## 全15章
```
1. SW要求
2. SW設計
3. SW構築          // 今日はここ ★★★★
4. SWテスティング   // 次回
5. SW保守
6. SW構成管理
7. SWエンジニアリング・マネージメント
8. SWエンジニアリングプロセス
9. SWエンジニアリングモデルおよび方法
10. SW品質
11. SWエンジニアリング専門技術者実践規律
12. SWエンジニアリング経済学
13. 計算基礎
14. 数学基礎
15. エンジニアリング基礎
```

---
# 良い名前をつける
良いプログラミングの第一歩

```diff
- return result; // 抽象的すぎて何も伝わらない
+ return count;  // 具体的な名前を
```

```diff
- int delay = 1000;   // delay WHAT?
+ int delayMs = 1000; // 単位をつけるべき
```

```java
if (debug) {
  String s = ..; // スコープが小さいならサボってもOK
  print(s);
}
```

```diff
- getData();     // 抽象的すぎて何も伝わらない
+ getUserId();   // 具体的な名前を
```

```diff
- getMean();     // 開発者の期待を裏切る名前
+ computeMean(); // 計算コストを要するという旨を伝える
```

---
# 良い名前をつけるには?
## 色のある動詞を考える
`get` よりも `compute` `calculate` `retrieve` `extract`

## 分離する
名前をつけられない＝対象が曖昧かやりすぎか

## 他者のソースコードを読む [git/builtin/clone.c](https://github.com/git/git/blob/master/builtin/clone.c)
```c
int cmd_clone(int argc, const char **argv, const char *prefix)
  ...
  if (argc == 0)
    usage_msg_opt(_("You must specify a repository to clone."),
	  builtin_clone_usage, builtin_clone_options);
```

```
$ git clone
fatal: You must specify a repository to clone.
usage: git clone [<options>] [--] <repo> [<dir>]
```


---
# 動くプログラムは簡単
## プログラミング言語の基本命令
四則演算 `sum+5` `i++` `total*rate`
変数の宣言 `int i` `String s` `var v`
関数呼び出し `print("err")` `sort(arr)` `str.lower()`
繰り返し `for(..)` `while(..)`
条件分岐 `if(..)` `else`

## これだけであらゆる処理が可能
チューリング完全
意図通りに動くプログラムは作れる


<!--## 動くようになったら「良い」を考えるべき-->

---
# プログラミングの習得レベル
## Lv1. アルゴリズムとデータ構造

## Lv2. 構文･文法
この段階で動くプログラムは作れる

## Lv3. パラダイム
構造化･オブジェクト指向･関数型･宣言型

パラダイムの理解には各種概念の理解が必要
　- OO：カプセル化･継承･移譲･ポリモルフィズム
　- 関数型：参照透過性･冪等性･純粋性･副作用

Lv2は具体的だがLv3は抽象的で難しい

---
# 動くの先にある良いプログラム
## Lv3パラダイムの理解が重要
Lv2ので満足してはいけない
Lv3を習得すると劇的にプログラミングが上達する

LibやFWを使う際に開発者の気持ちがわかる


## Lv2の段階でも様々な良さがある
適切な名前･関数分割･浅いネスト等

---
# そもそも良いとは？
## 信頼性･効率性 (実行的側面の良さ)
目的を満たすか？バグがないか？
リソースの無駄がないか？

## 可読性･保守性
読みやすいか？意図を汲み取れるか？

## 拡張性
拡張はソースの書き換えか？追加か？

## テスタビリティ
`main()` vs `main()+sub1()+sub2()+sub3()`

---
# 
## 大昔の機械語
Dicstra

Goto
構造化しろ・モジュール化しろ


---
# Don't call us, we'll call you
## 制御の反転・ハリウッド原則
制御の主となるmain()を自分で書かない
フレームワークはこの考えに基づく

普通の制御
```java
[My source] // 我々のプログラムがLibを呼び出す
  ↓ call
[Library]
```

制御の反転
```java
[Framework] // main関数はここ
  ↓ call
[My source] // 我々のプログラムはFWから呼ばれる 
  ↓ call
[Library]
```

---
# FWの利用方法
FWのルールに則ってプログラムを作る
どんな時に･何をしたいかだけを記述する (!!)
あとはFWに任す
雑多な共通処理は全部FWがやってくれる

システム全体の制御を考えなくてよい

## 
---
# 制御の反転の一例
## Flask
```py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"
```

## Arduino言語
```c
void setup() {
  // 最初に一度だけ呼ばれる
}
void loop() {
  // 無限に何度も呼ばれる
}
```

---
# 制御の反転のpros/cons
## Pros
FWを利用する開発者はとても楽
共通の処理をFWに任せられる
関心の分離が可能

## Cons
できることに制限が生まれる
かゆいところに手が届かない

FWに対する深い理解が必要
　- いつcallback関数のか？


---
# goto有害論
##

![](fig/goto-harmful.png)

<sub>E.W. Dijkstra, Communications of the ACM, 1968</sub>

---
<div id="corner-triangle"><div class="corner-triangle-text">雑談</div></div>

# X Considered Harmful
## ![](fig/considered-harmful.png)

---
# gotoの例
## ARMアセンブリ言語によるQSort
```arm
qsort:
    PUSH    {R0-R10,LR}        
    MOV     R4,R0              
    MOV     R5,R1              
    CMP     R5,#1              
    BLE     qsort_done         # goto文
    CMP     R5,#2              
    BEQ     qsort_check        # goto文
    ..       
qsort_check:
    LDR     R0,[R4]    
    LDR     R1,[R4,#4] 
    CMP     R0,R1
    BLE     qsort_done         # goto文
    ..
qsort_done:
    POP     {R0-R10,PC}
```
<!--
https://vaelen.org/post/arm-assembly-sorting/
-->

---
# goto文の何が悪いのか？
## goto文は一見すごい命令
高い汎用性：分岐･繰返･関数の必須要素
使いやすい：`goto label` + `label` のみ

プログラムの制御を自在に変更できる

## 何でもできるのが良くない
使いやすいがゆえに乱用されがち

無秩序の種
いわゆるスパゲッティコードの根源🍝

天才なら制御できるかもしれないが常人には無理
天才は1年後自分コードを理解できるか？

---
# gotoを許すフローチャート
![width:700px](fig/runcible.png)
<sub>RUNCIBLE -algebraic translation on a limited computer</sub>

---
# goto否定論からの学び
## 汎用的･使いやすいは必ずしも正義ではない
目的に特化している方が意図が明確
`CMP` `JMP` ではなく `if()` や `while()`

3つの要素でプログラムは実現可能
　順序･分岐･反復
　→ 構造化プログラミング

## できることを制限したほうが良い場合がある
物事が単純になる
秩序が生まれる

---
# レポートより
<br><br><br><br><br>
> グローバル変数はとても使いやすかったので
> 今後積極的に使っていきたい

---
# できないことを増やす
## non-finalよりもfinal
変数の書き換えを禁止する
Rustはデフォルトで不変
```rust
let x = 5;     // 不変（デフォルト）
let mut y = 5; // 可変
```

## publicよりもprivate，globalよりもlocal
変数･フィールドの可視性を下げる
データと処理をくっつけるカプセル化の考え

## 自前main()よりも制御の反転
自分でやらずに誰かに任す


---
# 大きな問題を分解する
## 大きな問題を制御可能な程度に小さく分解する
大きな問題に体当たりしてはいけない

例）
　1. 指定ディレクトリ内のファイルを探索する
　2. 発見したファイルに処理XとYを行う
　3. その結果を外部ツールZに入力する
　4. その結果を指定ディレクトリに書き出す

./analyze.py in-dir out-dir

---
# Complex vs Complicated
## 
---
# できないことを増やす
## 何でもできるは危険である


どこで誰が書き換えるか予測できない
値を書き換えたらどこに波及するか予測できない
public private
final
encapsulate
static final


---
# DRYの原則
## Don't repeat yourself

---
# a

## プログラミングは機械との対話ではない
人との対話という側面もある

## ソースコードはコミュニケーション

