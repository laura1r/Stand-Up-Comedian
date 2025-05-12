import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "black"

    for exitrow in page.controls:
        page.controls.remove(exitrow)

    jokeslist = [f"Did you hear about the guy who went to jail for stealing a calendar?",
                 "Why don't scientists trust atoms?",
                 "Why did the bicycle fall over?",
                 "What do you call fake spaghetti?",
                 "I'm reading a book on anti-gravity.",
                 "Why did the scarecrow win an award?",
                 "I tried to catch fog yesterday.",
                 "What do you call a bear with no teeth?",
                 "Did you know that 10+10 and 11+11 are the same thing?",
                 "My Bluetooth speaker wasn't working so I threw it into the lake."]

    jokelist2 = [f"He got 12 months.",
                 "Because they make up everything",
                 "Because it was two-tired.",
                 "An impasta",
                 "It's impossible to put down",
                 "Because he was outstanding in his field",
                 "Mist.",
                 "A gummy bear.",
                 "Because 10+10 is twenty and 11+11 is twenty too.",
                 "Now it's syncing."]

    page.update()

    def jokes(e):
        
        page.update()

    def jokes2(e):
        
        page.update()

    def start(e):
        for startrow in page.controls:
            page.controls.remove(startrow)
            page.controls.append(jokeButtom)
            page.controls.append(jokeButtom2)
        page.update()

    def exit(e):
        for exitrow in page.controls:
            page.controls.remove(exitrow)
        page.update

    title = ft.Text("Stand Up Comedian", size=22, weight="bold", color="white")
    text = ft.Text()

    jokeButtom = ft.Container(content=ft.ElevatedButton(
          on_click=jokes, content=ft.Text("Make a joke!", size=13, weight="bold", color="grey"),
          style=ft.ButtonStyle( shape={"": ft.RoundedRectangleBorder(radius=8)}, color={"": "white"}), height=45, width=255))
    
    jokeButtom2 = bs = ft.BottomSheet(ft.Container(ft.Column(
                [ft.Text("Here is a bottom sheet!"), ft.ElevatedButton("Dismiss", on_click=lambda _: page.close(bs)),],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,),padding=50,),open=False, on_dismiss=jokes2)

    startButton = ft.Container(content=ft.ElevatedButton(
          on_click=start, content=ft.Text("Start", size=13, weight="bold", color="grey"),
          style=ft.ButtonStyle( shape={"": ft.RoundedRectangleBorder(radius=8)}, color={"": "white"}), height=45, width=255))
     
    exitButton = ft.Container(content=ft.ElevatedButton(
          on_click=exit, content=ft.Text("Exit", size=13, weight="bold", color="grey"),
          style=ft.ButtonStyle( shape={"": ft.RoundedRectangleBorder(radius=8)}, color={"": "white"}), height=45, width=255))
    
    titlerow = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[title])
    startrow = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[startButton])
    exitrow = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[exitButton])

    page.add(titlerow, 
             ft.Divider(height=20, color="transparent"),
             startrow, exitrow, jokeButtom, text)
ft.app(target=main)