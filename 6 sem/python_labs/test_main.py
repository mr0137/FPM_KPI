import unittest
from main import *


class MyTestCase(unittest.TestCase):
    data = [{"Date": "11.12.2018", "Tasks": [{"Task": "hello my dear friend"}]}]

    def test_correct_date(self):
        try:
            self.assertEqual(correct_date("31.12.2018"), True)
            self.assertEqual(correct_date("32.12.2018"), False)
            print("Test 'correct_date()' PASS")
        except UserWarning:
            print("Test 'correct_date()' FAIL")

    def test_try_to_load(self):
        try:
            self.assertLessEqual(is_empty(try_to_load("data.json")), True)
            print("Test 'try_to_load()' PASS")
        except UserWarning:
            print("Test 'try_to_load()' FAIL")

    def test_show_task(self):
        try:
            self.assertEqual(show_task("01.12.2018"), "No tasks for this day")
            self.assertMultiLineEqual(show_task("11.12.2018"), "<p> 1. hello my dear friend</p>")
            print("Test 'show_task()' PASS")
        except UserWarning:
            print ("Test 'show_task()' FAIL")

    def test_find_date(self):
        try:
            self.assertDictEqual(find_date(self.data, "11.12.2018"), {"Date": "11.12.2018", "Tasks": [{"Task": "hello my dear friend"}]})
            print("Test 'find_date()' PASS")
        except UserWarning:
            print("Test 'find_date()' FAIL")

    def test_is_empty(self):
        try:
            self.assertEqual(is_empty(self.data), False)
            print("Test 'is_empty()' PASS")
        except UserWarning:
            print("Test 'is_empty()' FAIL")

    def test_find_task(self):
        try:
            temp = {"Date": "11.12.2018", "Tasks": [{"Task": "hello my dear friend"}]}
            self.assertDictEqual(find_task("hello my dear friend", temp), {"Task": "hello my dear friend"})
            print("Test 'find_task()' PASS")
        except UserWarning:
            print("Test 'find_task()' FAIL")

    def test_is_created(self):
        try:
            self.assertEqual(is_created("31.12.2018", "hello my dear friend"), False)
            self.assertEqual(is_created("12.12.2018", "hello my dear friend"), False)
            self.assertEqual(is_created("11.12.2018", "hello my dear friend"), True)
            print("Test 'is_created()' PASS")
        except UserWarning:
            print("Test 'is_created()' FAIL")

    def test_add_elem(self):
        try:
            self.assertMultiLineEqual(add_elem("12.12.2018", "hi"), "Task: \"hi\" already exist for 12.12.2018")
            print("Test 'add_elem()' PASS")
        except UserWarning:
            print("Test 'add_elem()' FAIL")

    def test_delete_elem(self):
        try:
            self.assertMultiLineEqual(delete_elem("13.12.2018", "hi(1)"), "Task: \"hi(1)\" doesn't exist")
            print("Test 'delete_elem()' PASS")
        except UserWarning:
            print("Test 'delete_elem()' FAIL")


