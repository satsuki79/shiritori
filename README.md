# しりとりアプリ
LLMの勉強のため、LLMサービスの代表格、Chat-GPTのAPIを使ってしりとりをするアプリを作成します。

## 環境
- 今回は`Google Colaboratory`上でコードを動かすことを前提とします。
- `OpenAI`の公式サイトでユーザ登録をし、API Keyを取得する必要があります。
    - https://platform.openai.com/docs/overview
- 取得したAPI Keyは、`Google Colaboratoryのシークレット`に登録してください。
- Python環境
    - Python 3.12.12
    - openai 1.66.3

## 使い方
- shiritori.py を実行してください。
    - しりとりが始まり、ユーザの入力待ち状態になります。

## 結果
- しりとり中は特に問題なくルール通り回答を続けてくれます。
- ユーザがルールに反する回答をした時に、次のような誤った回答をします。
    - ユーザが回答を"ん"で終わらせたり、既出の単語を答えても、何事もなかったようにしりとりを続けてしまう
    - 違反点を指摘してくれることもあるが、負けた側をプレーヤーでなくしりとりbotと説明するなど、誤った判定をしてしまう
- `system_prompt`に書いたルールの文章を追加・修正してみても効果はありませんでした。

## 改善点
- 今回はAPIを使ったLLMの勉強が目的なのでここまでとしますが、今後改良するとしたら次の点が考えられます。
    - "終了"と回答したときの動作は安定しているため、ルール違反の答えに対する動作のパターンを具体的に`system_prompt`に追加してみる
    - プロンプトではなく、コンテキストとしてルールや挙動のパターンをAPIに渡す方法があるか

## 参考
- Udemy [大規模言語モデル（LLM）・生成系AIをディープラーニングの成り立ちから学びPythonで動かしてみよう！](https://www.udemy.com/course/llm-ai-python/?srsltid=AfmBOoqZ6BbH2QjIE8VdlX15p-0JnG97lwI9flcMr9niT0GrzwXTxoxj&couponCode=V2JPLETSLEARN)
- [OpenAI APIドキュメント](https://platform.openai.com/docs/api-reference/chat/create)