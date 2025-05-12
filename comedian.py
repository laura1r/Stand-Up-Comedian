import flet as ft
import random

def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "black"

    jokeslist = ["Did you hear about the guy who went to jail for stealing a calendar?\nHe got 12 months.",
                 "Why don't scientists trust atoms?\nBecause they make up everything",
                 "Why did the bicycle fall over?\nBecause it was two-tired.",
                 "What do you call fake spaghetti?\nAn impasta",
                 "I'm reading a book on anti-gravity.\nIt's impossible to put down.",
                 "Why did the scarecrow win an award?\nBecause he was outstanding in his field.",
                 "I tried to catch fog yesterday.\nMist.",
                 "What do you call a bear with no teeth?\nA gummy bear.",
                 "Did you know that 10+10 and 11+11 are the same thing?\nBecause 10+10 is twenty and 11+11 is twenty too.",
                 "My Bluetooth speaker wasn't working so I threw it into the lake.\nNow it's syncing."]

    def displayJoke(e):
        jokeText.value = random.choice(jokeslist)
        page.update()
        page.open(Jokebs)

    title = ft.Text("Stand Up Comedian", size=22, weight="bold", color="white")
    jokeText = ft.Text("")

    jokeButtom = ft.Container(content=ft.ElevatedButton(
          on_click=displayJoke, content=ft.Text("Make a joke!", size=13, weight="bold", color="grey"),
          style=ft.ButtonStyle( shape={"": ft.RoundedRectangleBorder(radius=8)}, color={"": "white"}), height=45, width=255))
    
    Jokebs = ft.BottomSheet(ft.Container(ft.Column(
                [jokeText, ft.ElevatedButton("Dismiss", on_click=lambda _: page.close(Jokebs)),],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,),padding=50,),open=False)
     
    page.overlay.append(Jokebs)
    titlerow = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[title])

    page.add(titlerow, 
             ft.Divider(height=20, color="transparent"), jokeButtom)
ft.app(target=main)