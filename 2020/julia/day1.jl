
INPUT_FILE = "../inputs/day1_input.txt"

function load_data()
    data = readlines(INPUT_FILE)
    data = [parse(Int32,strip(x)) for x in data]
    return data
end

function find_nums(data)
    for i in 1:length(data)
        for j in i:length(data)
            if data[i] + data[j] == 2020
                return data[i] * data[j]
            end
        end
    end
end


data = load_data()
mult = find_nums(data)
println(mult)