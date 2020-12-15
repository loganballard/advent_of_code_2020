import os
dir_path = os.path.dirname(os.path.realpath(__file__))

file_input = open("".join([dir_path, "/", "input.txt"]), "r")
txt = file_input.read().splitlines()

visited_steps = set()
accumulator = 0
instr_pointer = 0

def get_instruction(line: str):
    inst, val = line.split()
    return inst, int(val)


while True:
    if instr_pointer in visited_steps:
        print(accumulator)
        break
    instr, val = get_instruction(txt[instr_pointer])
    visited_steps.add(instr_pointer)
    if instr == 'nop':
        instr_pointer += 1
        continue
    if instr == 'acc':
        accumulator += val
        instr_pointer += 1
    if instr == 'jmp':
        instr_pointer += val