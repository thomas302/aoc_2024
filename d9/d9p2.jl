using Base.Iterators

function is_numeric(x::String)
    return !isnothing(tryparse(Int,x))
end

function calc_checksum(data::Array)
    cnt = 0
    for (i,v) in enumerate(data)
        if is_numeric(v)
            cnt += (i-1)*parse(Int, v)
        else
            continue
        end
    end
    return cnt   
end

mutable struct diskVal
    len::Int
    fileID::Union{Int, Nothing}
end

function compress_disk(data::Array)
    while true
        first_gap = findfirst(x -> "_" == x, data)
        last_val = findlast(x -> is_numeric(x) , data)
        if first_gap > last_val
            break
        end
        data[first_gap] = data[last_val]
        data[last_val] = "_" 
    end
    return data
end

function disk_to_string_arr(data::Array{diskVal,1})
    str = []
    for i::diskVal in data
        if !isnothing(i.fileID)
            for j in 1:1:i.len
                push!(str, string(i.fileID))
            end
        else
            for j in 1:1:i.len
                push!(str, "_")
            end
        end
    end
    return str
end


function find_gap(data::Array{String, 1}, start::Int)
    s = findnext(x->"_"==x, data, start)
    if isnothing(s)
        return nothing
    end

    e = findnext(x -> is_numeric(x), data, s)
    
    if isnothing(e)
        return (s,length(data))
    end
    return (s,e-1)
end

function find_all_gaps(data)
    s = 1
    out = []
    while true
        x = find_gap(data, s)
        if !isnothing(x)
            push!(out, x)
            s = x[2]+1
        else
            break
        end
    end
    return out
end

function compress_disk_alt(data::Array{diskVal,1})
    seen_id = Set()
    push!(seen_id, "_")
    data = disk_to_string_arr(data)
    while true
        last_val =  findlast(x -> !(x in seen_id), data)

        if isnothing(last_val)
            break
        end

        push!(seen_id, data[last_val])

        len_vals = findlast(x-> x == data[last_val], data[last_val:-1:1])

        gaps = find_all_gaps(data)
        gap = findfirst(x->x[2]-x[1]+1 >= len_vals, gaps)

        if isnothing(gap) || gaps[gap][1] > last_val
            continue
        end

        for i in 0:1:len_vals-1
           data[gaps[gap][1]+i] = data[last_val-i]
           data[last_val-i] = "_"
        end
    end
    return data
end

f = open("input", "r")
input = strip(read(f, String))

println(length(input))
if length(input)%2 == 1
    input *= "0"
end

temp = [s for s in Iterators.partition(input, 2)]

data = [(parse(Int, s[1]), parse(Int, s[2])) for s in temp]

temp = empty([diskVal(0, 0)])
for (i, v) in enumerate(data)
    push!(temp, diskVal(v[1], i-1))
    push!(temp, diskVal(v[2], nothing))
end

println(calc_checksum(compress_disk_alt(temp)))