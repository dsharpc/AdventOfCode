import StatsBase: countmap

INPUT_FILE = "inputs/day2_input.txt"

function load_data()
    data = readlines(INPUT_FILE)
    return data
end

function parse_data(line)
    policy, password = split(line, ":")
    rule, required_letter = split(policy, " ")
    mini, maxi = split(rule, "-")
    mini = parse(Int32, mini)
    maxi = parse(Int32, maxi)
    password = strip(password)
    return mini, maxi, required_letter, password
end

function validate_password(mini, maxi, required_letter, password)
    counted = countmap(password)
    req_letter_count = get(counted, required_letter[1], 0)
    if (req_letter_count >= mini) & (req_letter_count <= maxi)
        return true
    else
        return false
    end
end


function validate_password_part_2(mini, maxi, required_letter, password)
    exists_in_mini = required_letter[1] in password[mini]
    exists_in_maxi = required_letter[1] in password[maxi]
    

    if exists_in_mini + exists_in_maxi == 1
        return true
    else
        return false
    end
end


function main()
    data = load_data()
    valid_passwords = 0
    for el in data
        res = parse_data(el)
        valid = validate_password_part_2(res...)
        if valid
            valid_passwords += 1
        end
    end
    println(valid_passwords)
end

main()