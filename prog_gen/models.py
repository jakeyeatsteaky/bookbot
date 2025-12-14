from dataclasses import dataclass, field
from exercises import Exercise, Scheme
    
@dataclass
class Day:
    order:int
    exercises: dict[Exercise,Scheme] = field(default_factory=dict)
    percentages: list[int] = field(default_factory=list) # todo refactor since thers not way to associate exercise and percent

    def add_exercise(self, exercise: Exercise, scheme: Scheme, percent: int):
        self.exercises[exercise] = scheme
        
    def get_num_exercises(self):
        return len(self.exercises)
    

@dataclass
class Week:
    order: int
    days: list[Day] = field(default_factory=list)

    def add_day(self, day_to_add: Day):
        self.days.append(day_to_add)

    def get_num_days(self):
        return len(self.days)

@dataclass
class Program:
    name: str = field(default="Unnamed Program")
    weeks: list[Week] = field(default_factory=list)
    
    def add_week(self, week: Week):
        self.weeks.append(week)

    def get_num_weeks(self):
        return len(self.weeks)
