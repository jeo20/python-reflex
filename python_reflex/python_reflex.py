# INCREMENTO Y DECREMENTO
import reflex as rx


# BACK
class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1
        
        
# FRONT        
def index():
    return rx.vstack(
        rx.hstack(
            rx.button(
                "Decrement",
                color_scheme="ruby",
                on_click=State.decrement,      
            ),
            rx.heading(State.count, font_size="2em"),
            rx.button(
                "Increment",
                color_scheme="grass",
                on_click=State.increment,           
            ),
            spacing="4", align_items="center", justify_content="center"
        )
    )
    
# PAGINA    
app = rx.App()
app.add_page(index)