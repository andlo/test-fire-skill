from mycroft import MycroftSkill, intent_file_handler


class TestFire(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fire.test.intent')
    def handle_fire_test(self, message):
        self.speak_dialog('fire.test')


def create_skill():
    return TestFire()

