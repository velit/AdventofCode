#!/usr/bin/env python3
import re

with open("input.txt") as f:
    inputs = f.read()

pp_strings = inputs.split("\n\n")

required_fields = "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"

def has_valid_fields(pp_string):
    return all(field in pp_string for field in required_fields)

def parse_pp(pp_string):
    fields = [field.split(":") for field in pp_string.split()]
    return {name: value for (name, value) in fields}

def validate_pp(pp):
    byr = 1920 <= int(pp["byr"]) <= 2002
    iyr = 2010 <= int(pp["iyr"]) <= 2020
    eyr = 2020 <= int(pp["eyr"]) <= 2030

    if pp["hgt"][-2:] == "cm":
        hgt = 150 <= int(pp["hgt"][:-2]) <= 193
    elif pp["hgt"][-2:] == "in":
        hgt = 59 <= int(pp["hgt"][:-2]) <= 76
    else:
        hgt = False

    hcl = re.fullmatch(r"#[a-f0-9]{6}", pp["hcl"]) and True
    ecl = pp["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    pid = re.fullmatch(r"[0-9]{9}", pp["pid"]) and True
    validation = byr, iyr, eyr, hgt, hcl, ecl, pid
    return all(validation)


full_pps = [parse_pp(pp) for pp in pp_strings if has_valid_fields(pp)]
print(len([1 for pp in full_pps if validate_pp(pp)]))
