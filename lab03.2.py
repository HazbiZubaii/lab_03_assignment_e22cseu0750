#class initializing the parameters mentioned in the problem statement
class FlightPro:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority

    def __str__(self):
        return f"{self.p_id}\t{self.process}\t{self.start_time}\t{self.priority}"


class FlightTab:
    def __init__(self):
        self.processes = []
#function to add data
    def add_process(self, process):
        self.processes.append(process)
#function for sorting according to p_id
    def sort_by_p_id(self):
        self.processes.sort(key=lambda x: x.p_id)

#function to sort by start_time
    def sort_by_start_time(self):
        self.processes.sort(key=lambda x: x.start_time)

#function to sort by priority
    def sort_by_priority(self):
        priority_order = {"    High": 3, "    MID": 2, "    Low": 1}
        self.processes.sort(key=lambda x: priority_order[x.priority], reverse=True)

#function to print the given data in tabular form
    def print_table(self):
        print("P_ID\tProcess\tStart Time\tPriority")
        for process in self.processes:
            print(process)


#calling the class and making objects 
flight_tab = FlightTab()
flight_tab.add_process(FlightPro("P1", "   VSCode   ", 100, "    MID"))
flight_tab.add_process(FlightPro("P23", "   Eclipse   ", 234, "    MID"))
flight_tab.add_process(FlightPro("P93", "   Chrome   ", 189, "    High"))
flight_tab.add_process(FlightPro("P42", "   JDK      ", 9, "    High"))
flight_tab.add_process(FlightPro("P9", "   CMD      ", 7, "    High"))
flight_tab.add_process(FlightPro("P87", "   NotePad   ", 23, "    Low"))

print("Choose sorting parameter:")
print("1. Sort by P_ID")
print("2. Sort by Start Time")
print("3. Sort by Priority")

opt = int(input("Enter your choice: "))

if opt == 1:
    flight_tab.sort_by_p_id()
elif opt == 2:
    flight_tab.sort_by_start_time()
elif opt == 3:
    flight_tab.sort_by_priority()
else:
    print("Invalid choice")

flight_tab.print_table()