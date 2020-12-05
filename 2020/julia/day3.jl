INPUT_FILE = "inputs/day3_input.txt"

function load_data()
    data = readlines(INPUT_FILE)
    data = [strip(x) for x in data]
end

function toboggan(forest, slope=(1,3))
    row=1
    col=1
    trees=0
    while row < length(forest)
        println("Row: $row, col: $col, trees: $trees")
        row+=slope[1]
        col+=slope[2]
        if (col > length(forest[row]))
            col-=length(forest[row])
        end
        if forest[row][col] == '#'
            trees+=1
        end
    end
    return trees
end

function part1()
    data = load_data()
    trees = toboggan(data)
    println("##### DAY ONE RESULT #####")
    println(trees)
end

function part2()
    data = load_data()
    slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)]
    trees_mult = 1
    for slope in slopes
        trees = toboggan(data, slope)
        trees_mult = trees_mult * trees
    end
    println("##### DAY TWO RESULT #####")
    println(trees_mult)
end

part2()