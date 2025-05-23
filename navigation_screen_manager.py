from kivy.uix.screenmanager import ScreenManager, FadeTransition, SlideTransition


class NavigationScreenManager(ScreenManager):
    screen_stack = []

    def push(self,screen_name):
        if screen_name not in self.screen_stack:
            self.screen_stack.append(self.current)
            self.transition = FadeTransition() if not self.screen_stack else SlideTransition(direction="left")
            self.current=screen_name

    def pop(self):
        if len(self.screen_stack):
            screen_name=self.screen_stack[-1]
            self.transition.direction="right"
            del self.screen_stack[-1]
            self.current=screen_name

