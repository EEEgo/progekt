import openai
import flet as ft

openai.api_key = 'sk-proj-2YRanTbzwYBlNhjKZckET3BlbkFJTFoBjgWMKB6fkWMaJzN0'
messages = []


def main(page: ft.Page):
    chat = ft.Column()
    new_message = ft.TextField()

    def send_click(e):
        #chat.controls.append(ft.Text(new_message.value))
        new_message.value = ""
        message = new_message.value
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        new_message.value = {reply}
        messages.append({"role": "assistant", "content": reply})

        page.update()

    page.add(
        chat, ft.Row(controls=[new_message, ft.ElevatedButton("Send", on_click=send_click)])
    )

ft.app(target=main)