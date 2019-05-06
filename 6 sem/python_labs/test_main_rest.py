import unittest
import arrow
import requests

class PythonApi(unittest.TestCase):

    def test_get_item(self):
        utc = arrow.utcnow()
        res = requests.get('http://127.0.0.1:5000/tasks/31.12.2018')

        if res.status_code == 200:
            print("Test 'show_tasks()' PASS at " + str(utc))
        else:
            print("Test 'show_tasks()' FAIL at " + str(utc))


    def test_create_item(self):
        utc = arrow.utcnow()

        res = requests.get('http://127.0.0.1:5000/add_task/12.12.2018:hello')

        if res.status_code == 200:
            print("Test 'create_item()' PASS at " + str(utc))
        else:
            print("Test 'create_item()' FAIL at " + str(utc))


    def test_delete_item(self):
        utc = arrow.utcnow()

        res = requests.get('http://127.0.0.1:5000/delete_by_name/12.12.2018:hello')

        if res.status_code == 200:
            print("Test 'delete_measurements()' PASS at " + str(utc))
        else:
            print("Test 'delete_measurements()' FAIL at " + str(utc))


    def test_delete_item_by_id(self):
        utc = arrow.utcnow()

        res = requests.get('http://127.0.0.1:5000/delete_by_id/12.12.2018:1')

        if res.status_code == 200:
            print("Test 'delete_measurements()' PASS at " + str(utc))
        else:
            print("Test 'delete_measurements()' FAIL at " + str(utc))
