#--- ChatGPTのAPIを使って回答を取得する ---#
from openai import OpenAI
from google.colab import userdata

# Google Colabに登録しているユーザーデータからOpenAIのAPIKeyを取得
client = OpenAI( api_key=userdata.get('OPENAI_APIKEY') )

system_prompt = """
しりとりをします。すべての質問に対して以下のルールに厳格に従って答えてください。
- 'system'の一人称は'しりとりbot'とする
- 'user'の呼び名は'プレイヤー'とする
- 単語の選択は日本語辞書に基づく
- しりとりの単語は「」でくくる
- しりとりのルールは以下
  - 1つ前の単語の最後の文字から始まる単語を選ぶ
  - 一度出た単語は答えてはいけない
  - 最後の文字が"ん"で終わってはいけない
- ルールに反する行動があった場合は、最後に答えた方が負けとなる
- ルールに反する行動があった場合は、負けた理由と負けた方を説明する
- 回答は10文字以内の単語とする
"""
# メッセージリストを初期化
messages = [{"role": 'system', 'content': system_prompt}]

# ユーザ入力に対する応答を取得する関数
def get_response(user_input):
  # ユーザの回答をメッセージリストに追加
  user_message = {"role": 'user', 'content': user_input}
  messages.append(user_message)

  # ChatGPTのAPIを呼び出して応答を取得
  response = client.chat.completions.create(
      model="gpt-4o-mini",  # 無料版でも利用できるモデル(4oは有料版)
      store=True,
      messages=messages,
      temperature = 0.3     # 出力のランダム性を制御するパラメータ
  )
  bot_message = response.choices[0].message

  # しりとりbotの回答を整形してメッセージリストに追加
  bot_message_dict = {"role": bot_message.role, 'content': bot_message.content}
  messages.append(bot_message_dict)

  return bot_message.content

print("私はしりとりbotです。しりとりをしましょう！次のboxに単語を入力してください。")
while True:
  user_input = input("ユーザ：　※チャットを終了するには「終了」と入力してください。")
  if user_input=="終了":
    print("しりとりを終了します。")
    break

  bot_response = get_response(user_input)
  print(f"しりとりbot: {bot_response}")