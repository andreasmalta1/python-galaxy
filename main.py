from kivy.app import App
from kivy.graphics import Color, Line
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 7
    V_LINES_SPACING = .1  # % in screen width
    vertical_lines = []

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print("INIT W: " + str(self.width))
        # print("INIT H: " + str(self.height))
        self.init_vertical_lines()

    def on_parent(self, widget, parent):
        # print("PARENT W: " + str(self.width))
        # print("PARENT H: " + str(self.height))
        pass

    def on_size(self, *args):
        print("SIZE W: " + str(self.width))
        print("SIZE H: " + str(self.height))
        # self.perspective_point_x = self.width/2
        # self.perspective_point_y = self.height * 0.75
        self.update_vertical_lines()

    def on_perspective_point_x(self, widget, value):
        # print("PX: " + str(value))
        pass

    def on_perspective_point_y(self, widget, value):
        # print("PY: " + str(value))
        pass

    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            # self.line = Line(points=[100, 0, 100, 100])
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def update_vertical_lines(self):
        central_line_x = int(self.width/2)
        offset = -int(self.V_NB_LINES/2)
        spacing = self.V_LINES_SPACING * self.width
        for i in range(0, self.V_NB_LINES):
            line_x = int(central_line_x + offset*spacing)
            self.vertical_lines[i].points = [line_x, 0, line_x, self.height]
            offset += 1


class GalaxyApp(App):
    pass


GalaxyApp().run()
