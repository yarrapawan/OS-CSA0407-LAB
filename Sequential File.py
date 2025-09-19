# Sequential File

class SequentialFile:
    def __init__(self, name):
        self.name = name
        self.records = []

    # Add record at the end
    def add_record(self, record):
        self.records.append(record)
        print(f"Record '{record}' added to {self.name}")

    def display_records(self):
        print(f"\nRecords in {self.name}:")
        for i, rec in enumerate(self.records):
            print(f"Record {i+1}: {rec}")

  
    def access_record(self, index):
        if index < 0 or index >= len(self.records):
            print("Invalid record number!")
            return
        print(f"\nReading records sequentially up to record {index+1}:")
        for i in range(index+1):   # must read previous records too
            print(f"Record {i+1}: {self.records[i]}")



file = SequentialFile("student_file")

# Adding records
file.add_record("Alice - ID 101")
file.add_record("Bob - ID 102")
file.add_record("Charlie - ID 103")
file.add_record("David - ID 104")

# Display all records
file.display_records()

# Accessing the 3rd record (Charlie)
file.access_record(2)