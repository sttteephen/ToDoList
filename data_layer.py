import csv


# the TaskDatabase class is used to read/write tasks to the csv file, the task strings read are held in its task_list
class TaskDatabase:
    def __init__(self):
        self.task_list = []

    # reads tasks from csv file if it exists and populates the task_list
    def read_tasks(self):
        read_task_list = []

        try:
            csv_file = open("tasks.csv")
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                read_task_list.append(row[0])
                line_count += 1
            csv_file.close()
        except OSError:
            pass

        self.task_list = read_task_list

    # take the task_list and save content to csv file
    def write_tasks(self):
        csv_file = open("tasks.csv", mode="w", newline='\n')
        data_writer = csv.writer(csv_file)
        for task in self.task_list:
            data_writer.writerow([task])
        csv_file.close()
