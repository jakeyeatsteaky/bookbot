from builders import ProgramBuilder, Program, WeekBuilder, DayBuilder, Exercise, Scheme
from enum import Enum

def get_template_lines(filepath: str) -> list[str]:
    try:
        with open(filepath) as template:
            return template.readlines()
    except FileNotFoundError:
        print("Error, file: {filepath} not found")
    return ""
        
def parse_program(template_lines: list[str]) -> Program:
    programName: str = template_lines[0]
    template_lines.pop(0)
    builder: ProgramBuilder = ProgramBuilder(programName)
    
    while len(template_lines) > 0:
        if "<W>" in template_lines[0]:
            template_lines.pop(0)
            enter_week(builder.add_week(), template_lines)
        if "<Program/>" in template_lines[0]:
            return builder.generate()
        
            
def enter_week(weekBuilder: WeekBuilder, lines: list[str]):
    while len(lines) > 0:
        if "<W/>" in lines[0]:
            weekBuilder.done()
            lines.pop(0)
            return
        if "<D>" in lines[0]:
            lines.pop(0)
            enter_day(weekBuilder.add_day(), lines) 
        

def enter_day(dayBuilder: DayBuilder, lines: list[str]):
    while len(lines) > 0:
        if "<D/>" in lines[0]:
            lines.pop(0)
            dayBuilder.done()
            return
        else:
            enter_exercise(dayBuilder, lines[0])
            lines.pop(0)

def enter_exercise(dayBuilder: DayBuilder, exerciseStr: str):
    [exercise, scheme, percent] = extract_exercise(exerciseStr)
    dayBuilder.add_exercise(exercise, scheme, percent)

def extract_exercise(line: str):
    exercise: Exercise
    scheme: Scheme
    percent: int

    line = line.split(':')
    exercise = get_exercise(line[0])
    scheme = get_scheme(line[1], line[2])
    percent = line[3]

    return [exercise, scheme, percent]

def get_exercise(ex: str) -> Exercise:
    match ex:
        case "bsquat":
            return Exercise.BackSquat
        case "snatch":
            return Exercise.Snatch
        case "jerk":
            return Exercise.Jerk
        case "bench":
            return Exercise.BenchPress
        case "pullup":
            return Exercise.Pullup
        case "dbpr":
            return Exercise.DumbellPress
        case _:
            raise ValueError(f"Invalid exercise: {ex}")
        
def get_scheme(sets: str, reps: str) -> Scheme:
    key = f"S{sets}_R{reps}"
    return Scheme[key]

def dump_program(program: Program) -> None:
    print("PROGRAM")
    print(program)
    print()

    for w_i, week in enumerate(program.weeks):
        # print(f"Week[{w_i}]:", week)
        print(f"Week[{w_i}]:")
        print("  days:")

        for d_i, day in enumerate(week.days):
            # print(f"    Day[{d_i}]:", day)
            print(f"    Day[{d_i}]:")
            print("      exercises:")

            for e_i, ex in enumerate(day.exercises):
                print(f"        [{e_i}]:", ex)

        print()



def main():
    lines: list[str] = get_template_lines("templates/test.txt")
    prog: Program = parse_program(lines)
    dump_program(prog)
    
      
     
if __name__ == "__main__":
    main()