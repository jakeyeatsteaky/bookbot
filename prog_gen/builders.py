from __future__ import annotations
from dataclasses import dataclass
from models import Program, Week, Day, Exercise, Scheme


@dataclass
class ProgramBuilder():
    name: str

    def __post_init__(self):
        self.program = Program(self.name)

    def add_week(self) -> WeekBuilder:
        week = Week(order=len(self.program.weeks)+1)
        self.program.add_week(week)
        return WeekBuilder(self, week)

    def generate(self) -> Program:
        return self.program

@dataclass
class WeekBuilder:
    parent: ProgramBuilder
    week: Week

    def add_day(self) -> DayBuilder:
        day = Day(order=self.week.get_num_days()+1)
        self.week.add_day(day)
        return DayBuilder(self, day)
    
    def done(self) -> ProgramBuilder:
        return self.parent
    
@dataclass 
class DayBuilder:
    parent: WeekBuilder
    day: Day 

    def add_exercise(self, exercise: Exercise, scheme: Scheme, percent) -> DayBuilder:
        self.day.add_exercise(exercise, scheme, percent)
        return self

    def done(self) -> WeekBuilder:
        return self.parent

def test():
    program: Program = (ProgramBuilder("Test Program")
        .add_week()
            .add_day()
                .add_exercise(Exercise.BackSquat, Scheme.S3_R5)
                .add_exercise(Exercise.Snatch, Scheme.S3_R3)
            .done()
        .done()
    .generate())
    
if __name__ == "__main__":
    test()