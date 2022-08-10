import flet
from flet import (Column, Container, ElevatedButton, Page, Row, Text,
                  TextField, UserControl, alignment, colors, icons, padding)

values = ['O', 'X']


class Players(UserControl):
    def build(self) -> None:
        """Its create 2 players profile"""
        players = Row()
        for _ in range(2):
            players.controls.append(
                Container(
                    width=75,
                    height=75,
                    bgcolor=colors.BLUE_GREY_200,
                    alignment=alignment.center,
                    content=Text(value=values[_], size=25, weight="bold")
                )
            )
        players.controls[1].bgcolor = colors.GREEN
        return players


class Board(UserControl):
    def build(self) -> None:
        """
        It creates a 3*3 grid of blue-grey squares
        :return: A Column - our board with 3 Rows, each with 3 Containers.
        """
        board = Column()
        for _ in range(3):
            row = Row()
            for _ in range(3):
                row.controls.append(
                    Container(
                        width=75,
                        height=75,
                        bgcolor=colors.BLUE_GREY_200,
                        alignment=alignment.center,
                        on_click=self.change_field,
                        content=Text(value='', size=50, weight="bold")
                    )
                )
            board.controls.append(row)
        return board

    def check_for_set(self, e):
        """check the status of players"""
        cols = []
        for column in range(0, 3):
            rows = []
            for row in range(0, 3):
                rows.append(
                    e.page.controls[0].controls[0].controls[0].controls[0].controls[
                        column].controls[row].content.value)
            cols.append(rows)
        # horizontal
        result = None
        for row in cols:
            if row[0] and row[1] and row[2] and row[0] == row[2] and row[0] == row[1]:
                result = f' {row[0]} wins '
        # vertical
        for col in range(0, 3):
            if cols[0][col] and cols[1][col] and cols[2][col] and (
                    cols[0][col] == cols[1][col] and cols[0][col] == cols[2][col]):
                result = f' {cols[0][col]} wins '
        # diagonal
        if cols[0][0] and cols[1][1] and cols[2][2] and (
                cols[0][0] == cols[1][1] and cols[0][0] == cols[2][2]):
            result = f' {cols[0][col]} wins '
        if cols[0][2] and cols[1][1] and cols[2][0] and (
                cols[0][2] == cols[1][1] and cols[0][2] == cols[2][0]):
            result = f' {cols[0][col]} wins '
        return result

    def change_field(self, e):
        """change field value on click"""
        if e.control.content.value:
            return
        e.control.content.value = values.pop()
        if e.control.content.value == 'O':
            e.control.bgcolor = colors.RED_ACCENT
            e.page.controls[0].controls[0].controls[1].controls[0].controls[0].bgcolor = colors.BLUE_GREY_200
            e.page.controls[0].controls[0].controls[1].controls[0].controls[1].bgcolor = colors.GREEN
        else:
            e.control.bgcolor = 'blue'
            e.page.controls[0].controls[0].controls[1].controls[0].controls[1].bgcolor = colors.BLUE_GREY_200
            e.page.controls[0].controls[0].controls[1].controls[0].controls[0].bgcolor = colors.GREEN
        values.insert(0, e.control.content.value)
        e.page.controls[0].controls[0].controls[2].value = self.check_for_set(e)
        e.page.controls[0].controls[0].controls[1].controls[0].update()
        e.page.controls[0].controls[0].update()
        e.control.update()


class Sos:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.setup_page()
        self.game()

    def setup_page(self) -> None:
        """
        > The function sets the page title, theme mode, vertical and horizontal alignment, and padding
        """
        self.page.title = "Sos"
        self.page.theme_mode = "system"
        self.page.window_width = 300
        self.page.window_height = 500
        self.page.window_focused = True
        self.page.vertical_alignment = "center"
        self.page.horizontal_alignment = "center"
        self.page.padding = 15
        self.page.update()

    def game(self) -> None:
        self.board = Board()
        players = Players()
        message = Text(value='', size=25, weight="bold")
        column = Column(controls=[self.board,
                                  players,
                                  message],
                        horizontal_alignment='center',
                        spacing=30)
        self.page.add(
            Row(controls=[column]))


if __name__ == "__main__":
    flet.app(name="Sos", target=Sos)
