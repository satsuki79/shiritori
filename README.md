# しりとりアプリ
LLMの勉強のため、LLMサービスの代表格、Chat-GPTのAPIを使ってしりとりをするアプリを作成します。

## 環境
- Google Colaboratory

## requirements
- OpenAIの公式サイトでユーザ登録をし、API Keyを取得する必要があります。
- 取得したAPI Keyは、Google Colaboratoryのユーザーデータに登録してください。
- Python環境
    - Python 3.12.12
    - pip install openai==1.66.3

## 結果
- しりとり中は特に問題なくルール通り回答を続けてくれる
- ユーザがルールに反する回答をした時に、誤った回答をする
    - ユーザが"ん"で終わらせたり、既出の単語を答えても、何事もなかったようにしりとりを続けてしまう
    - 違反点を指摘してくれることもあるが、負けた側をしりとりbotとして誤った判定をしてしまう。
- ルールを書いている`system_prompt`を追加・修正してみても効果はなかった

## 改善点
- "終了"と回答したときの動作は安定しているため、ルール違反の答えに対する動作のパターンを具体的に`system_prompt`に追加してみる
- プロンプトではなく、コンテキストとしてルールや挙動のパターンをAPIに渡す方法があるか

## 参考
- Udemy: うまたん "大規模言語モデル（LLM）・生成系AIをディープラーニングの成り立ちから学びPythonで動かしてみよう！"
- OpenAI APIドキュメント: https://platform.openai.com/docs/api-reference/chat/create