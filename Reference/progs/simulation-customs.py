""" 公路收费站模拟，队列和优先队列的应用
"""

from random import randint
from prioqueue import PrioQueue  # , PrioQueueError
from queue_list import SQueue    # , QueueUnderflow


class Simulation:
    def __init__(self, duration):
        self._eventq = PrioQueue()
        self._time = 0
        self._duration = duration

    def run(self):
        while not self._eventq.is_empty():
            event = self._eventq.dequeue()
            self._time = event.time()
            if self._time > self._duration:
                break
            event.run()  # may cause new event(s)

    def add_event(self, event):
        self._eventq.enqueue(event)

    def cur_time(self):
        return self._time

class Event:
    def __init__(self, event_time, host):
        self._ctime = event_time
        self._host = host

    def __lt__(self, other_event):
        return self._ctime < other_event._ctime

    def __le__(self, other_event):
        return self._ctime <= other_event._ctime

    def host(self):
        return self._host

    def time(self):
        return self._ctime

    def run(self):
        pass



class Customs:
    def __init__(self, gate_num, duration,
                 arrive_interval, check_interval):
        self.simulation = Simulation(duration)
        self.waitline = SQueue()
        self.duration = duration
        self.gates = [0]*gate_num
        self.total_wait_time = 0
        self.total_used_time = 0
        self.car_num = 0
        self.arrive_interval = arrive_interval
        self.check_interval = check_interval

    def wait_time_acc(self, n):
        self.total_wait_time += n

    def total_time_acc(self, n):
        self.total_used_time += n

    def car_count_1(self):
        self.car_num += 1

    def add_event(self, event):
        self.simulation.add_event(event)

    def cur_time(self):
        return self.simulation.cur_time()

    def enqueue(self, car):
        self.waitline.enqueue(car)

    def has_queued_car(self):
        return not self.waitline.is_empty()

    def next_car(self):
        return self.waitline.dequeue()

    def find_gate(self):
        for i in range(len(self.gates)):
            if self.gates[i] == 0:
                self.gates[i] = 1
                return i
        return None

    def free_gate(self, i):
        if self.gates[i] == 1:
            self.gates[i] = 0
        else:
            raise ValueError("Clear gate error.")

    def simulate(self):
        Arrive(0, self)  # initially generate one car
        self.simulation.run()
        self.statistics()
        
    def statistics(self):
        print("Simulate " + str(self.duration) + " minutes, for "
              + str(len(self.gates)) + " gates")
        print(self.car_num, "cars pass the customs")
        print("Average waiting time:",
              self.total_wait_time/self.car_num)
        print("Average passing time:",
              self.total_used_time/self.car_num)
        i = 0
        while not self.waitline.is_empty():
            self.waitline.dequeue()
            i += 1
        print(i, "cars are in waiting line.")


class Car:
    def __init__(self, arrive_time):
        self.time = arrive_time

    def arrive_time(self):
        return self.time


def event_log(time, name):
    print("Event: " + name + ", happens at " + str(time))
    pass



# a run of coming event will enter the next coming event and
# maybe a check and leave event

class Arrive(Event):
    def __init__(self, arrive_time, customs):
        Event.__init__(self, arrive_time, customs)
        customs.add_event(self)

    def run(self):
        time, customs = self.time(), self.host()
#        event_log(time, "car arrive")
        # genarate the next Arrive event
        Arrive(time + randint(*customs.arrive_interval), customs)
        # deal with current Arrive car
        car = Car(time)
        if customs.has_queued_car():
            customs.enqueue(car)
            return
        i = customs.find_gate()
        if i is not None:
#            event_log(time, "car check")
            Leave(time + randint(*customs.check_interval),
                  i, car, customs)
        else:
            customs.enqueue(car)


# a run of leaving event will cause some calculations

class Leave(Event):
    def __init__(self, leave_time, gate_num, car, customs):
        Event.__init__(self, leave_time, customs)
        self.car = car
        self.gate_num = gate_num
        customs.add_event(self)

    def run(self):
        time, customs = self.time(), self.host()
#        event_log(time, "car leave")
        customs.free_gate(self.gate_num)
        customs.car_count_1()
        customs.total_time_acc(time - self.car.arrive_time())
        if customs.has_queued_car():
            car = customs.next_car()
            i = customs.find_gate()
#            event_log(time, "car check")
            customs.wait_time_acc(time - car.arrive_time())
            Leave(time + randint(*customs.check_interval),
                  i, car, customs)

if __name__ == '__main__':

    car_arrive_interval = (1, 2)
    car_check_time = (3, 5)

    cus = Customs(3, 120, car_arrive_interval, car_check_time)
    cus.simulate()
    pass
