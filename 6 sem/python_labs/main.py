import json
import datetime

from flask import Flask, abort

filename = "data.json"
app = Flask(__name__)

#   just error message


@app.errorhandler(405)
def error_message():
    return "Incorrect data format, should be DD.MM.YYYY"

#   check for correct Data


def correct_date(date):
    try:
        datetime.datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        return False

#   try to load .json file to object


def try_to_load(filename_f="data.json"):
    with open(filename_f) as json_file:
        try:
            data = json.load(json_file)
        except json_file:
            data = []
    json_file.close()
    return data

#   writing to file + showing new file


def write_to_json(element):
    json_file = open(filename, 'w')
    json.dump(element, json_file)
    json_file.close()

#   showing tasks for current day


@app.route('/tasks/<string:date>', methods=['GET'])
def show_task(date):
    data = try_to_load()
    data = find_date(data, date)
    a = ""
    if is_empty(data) is False:
        for i in range(0, data['Tasks'].__len__()):
            a += "<p> " + str(i+1) + ". " + data['Tasks'][i]['Task'] + "</p>"
        if is_empty(a) is False:
            # print(a)
            return a
    return "No tasks for this day"


#   finding date


def find_date(data, date):
    if correct_date(date) is True:
        for i in range(0, data.__len__()):
            if data[i]['Date'] == date:
                return data[i]
        if data[i]['Date'] != date:
            return []
    else:
        abort(405)


#   check for empty elements


def is_empty(data):
    if data.__len__() == 0:
        return True
    else:
        return False


#   finding task ( return dict )

def find_task(task, data):
    if is_empty(data['Tasks']) is False:
        for i in range(0, data['Tasks'].__len__()):
            if data['Tasks'][i]['Task'] == task:
                return data['Tasks'][i]
    return []

#   check for same task


def is_created(date, task):
    data = try_to_load()
    temp = find_date(data, date)
    if is_empty(temp) is False:

        if is_empty(find_task(task, temp)):
            return False
        else:
            return True
    else:
        return False

#  creating new date or return old


def create_date(date):
    data = try_to_load()
    data = find_date(data, date)
    if is_empty(data) is False:
        data = try_to_load()
        return data
    else:
        elem = {'Date': date, 'Tasks': []}
        data = try_to_load()
        data.append(elem.copy())
        return data

# creating new task


def create_task(data, task):
    elem = {"Task": task}
    data['Tasks'].append(elem.copy())

# adding element


@app.route('/add_task/<string:date>:<string:task>', methods=['GET'])
def add_elem(date, task):
    if is_created(date, task) is False:
        data = create_date(date)
        create_task(find_date(data, date), task)
        write_to_json(data)
        return "<a href=\"http://127.0.0.1:5000/tasks/" + date + "\"" + ">tasks</a>"
    else:
        return "Task: " + "\"" + task + "\"" + " already exist for " + date


#  del current task

def delete_task(date, task):
    data = try_to_load()
    temp = find_date(data, date)
    if is_empty(temp) is True:
        return data
    else:
        for i in range(0, temp['Tasks'].__len__()):
            if temp['Tasks'][i]['Task'] == task:
                del temp['Tasks'][i]
                break
        return data


def find_task_by_id(date, id):
    for i in range(0, date['Tasks'].__len__()):
        if i == id - 1:
            return date['Tasks'][i]['Task']
    return ""



@app.route('/delete_by_id/<string:date>:<int:id>', methods=['GET'])
def delete_elem_by_id(date, id):
    data = try_to_load()
    temp = find_date(data, date)
    task = find_task_by_id(temp, id)
    if is_empty(task) is True:
        return "Task with id \"" + str(id) + "\" doesn't exist"
    else:
        return delete_elem(date, task)


# del data if tasks.__len__ == 0

def delete_date(data, date):
    for i in range(0, data.__len__()):
        if data[i]['Date'] == date:
            if is_empty(data[i]['Tasks']) is True:
                del data[i]
                break
    return data


# del element


@app.route('/delete_by_name/<string:date>:<string:task>', methods=['GET'])
def delete_elem(date, task):
    if is_created(date, task) is True:
        data = delete_task(date, task)
        delete_date(data, date)
        write_to_json(data)
        return "<a href=\"http://127.0.0.1:5000/tasks/" + date + "\"" + ">tasks</a>"
    else:
        return "Task: " + "\"" + task + "\"" + " doesn't exist"


def main():
    id = 5
    date = "31.12.2018"
    delete_elem_by_id(date, id)

if __name__ == "__main__":
    app.run(debug=True)
    #  main()
