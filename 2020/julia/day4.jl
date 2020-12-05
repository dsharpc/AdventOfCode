INPUT_FILE = "inputs/day4_input.txt"

function load_data()
    data = read(INPUT_FILE, String)
    return data
end

function get_passports(data)
    passports = split(data, "\n\n")
    return passports
end

function clean_passports(passport)
    dictio = Dict()
    passport = replace(passport, "\n" => " ")
    keyvalues = split(passport)
    for keyvalue in keyvalues
        key, value = split(keyvalue, ":")
        dictio[key] = value
    end
    return dictio
end

function validate_passport(passport)
    REQUIRED_KEYS = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    for key in REQUIRED_KEYS
        if ~ haskey(passport, key)
            return 0
        end
    end
    return 1
end


function validate_passport_keys(passport)
    try
        @assert 1920 < parse(Int32,passport["byr"]) <= 2002
        @assert 2010 <= parse(Int32, passport["iyr"]) <= 2020
        @assert 2020 <= parse(Int32, passport["eyr"]) <= 2030
        if occursin("cm", passport["hgt"])
            height = replace(passport["hgt"], "cm" => "")
            @assert 150 <= parse(Int32, height) <= 193
        elseif occursin("in", passport["hgt"])
            height = replace(passport["hgt"], "in" => "")
            @assert 59 <= parse(Int32, height) <= 76
        else
            @assert 1 == 0
        end
        hair_color = match(r"^#[0-9a-f]{6}$", passport["hcl"])
        @assert ~ isnothing(hair_color)
        @assert passport["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]
        passport_id = match(r"^[0-9]{9}$", passport["pid"])
        @assert ~ isnothing(passport_id)
    catch
        return 0
    end
    return 1
end

function part1()
    data = load_data()
    passports = get_passports(data)
    valid_passports = 0
    for passport in passports
        dictio = clean_passports(passport)
        valid_passports+=validate_passport(dictio)
    end
    println(valid_passports)
end

function part2()
    data = load_data()
    passports = get_passports(data)
    valid_passports = 0
    for passport in passports
        dictio = clean_passports(passport)
        validity=validate_passport(dictio)
        if validity == 1
            valid_passports += validate_passport_keys(dictio)
        end
    end
    println(valid_passports)
end


part2()
