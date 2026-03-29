class ThemeManager:
    def __init__(self, theme='light'):
        self.theme = theme
        self.colors = {
            'light': {
                'background': '#FFFFFF',
                'foreground': '#000000',
                'accent': '#FF5733',
            },
            'dark': {
                'background': '#000000',
                'foreground': '#FFFFFF',
                'accent': '#C70039',
            }
        }

    def set_theme(self, theme):
        if theme in self.colors:
            self.theme = theme
        else:
            raise ValueError(f'Theme {theme} is not supported.')

    def get_colors(self):
        return self.colors[self.theme]

    def update_colors(self, background=None, foreground=None, accent=None):
        if background:
            self.colors[self.theme]['background'] = background
        if foreground:
            self.colors[self.theme]['foreground'] = foreground
        if accent:
            self.colors[self.theme]['accent'] = accent

    def display(self):
        colors = self.get_colors()
        print(f'Theme: {self.theme.capitalize()}
Background: {colors['background']}
Foreground: {colors['foreground']}
Accent: {colors['accent']}')
