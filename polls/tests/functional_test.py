import datetime
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from django.utils import timezone
from polls.models import Question, Choice
from selenium import webdriver


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (days < 0 for questions published
    in the past, days > 0 for questions published in the future).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class FunctionalTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome(executable_path='C:/Users/user/Downloads/chromedriver.exe')
        super(SeleniumTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SeleniumTestCase, self).tearDown()

    def test_header(self):
        self.selenium.get(self.live_server_url + '/polls/')
        head = self.browser.find_element_by_tag_name('h1')
        self.assertEqual('Hot Topics', head.text)