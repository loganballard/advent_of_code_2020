import os, copy
dir_path = os.path.dirname(os.path.realpath(__file__))

file_input = open("".join([dir_path, "/", "input.txt"]), "r")
txt = file_input.read().splitlines()


def make_instruction_list(txt):
    ins_list = []
    for line in txt:
        ins_list.append(get_instruction(line))
    return ins_list


def get_instruction(line: str):
    inst, val = line.split()
    return [inst, int(val)]


def check_inf_loop(instr_list):
    visited_steps = set()
    instr_pointer = 0
    accumulator = 0
    while True:
        if instr_pointer in visited_steps:
            return True
        instr, val = instr_list[instr_pointer][0], instr_list[instr_pointer][1]
        visited_steps.add(instr_pointer)
        if instr == 'nop':
            instr_pointer += 1
            continue
        if instr == 'acc':
            accumulator += val
            instr_pointer += 1
        if instr == 'jmp':
            instr_pointer += val
        if instr_pointer == len(instr_list):
            print(accumulator)
            break
    return False


inst_list = make_instruction_list(txt)


for indx in range(len(inst_list)):
    ins_line = inst_list[indx]
    ins, val = ins_line[0], int(ins_line[1])
    if ins not in ('nop', 'jmp'):
        continue
    modified_ins_list = copy.deepcopy(inst_list)
    new_ins = 'nop' if ins == 'jmp' else 'jmp'
    modified_ins_list[indx][0] = new_ins
    if not check_inf_loop(modified_ins_list):
        break
