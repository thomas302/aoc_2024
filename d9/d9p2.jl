using Base.Iterators
using .Threads

function is_numeric(x::String)::Bool
    return !isnothing(tryparse(Int,x))
end

function calc_checksum(data::Array{String,1})::Int
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

struct diskVal
    len::Int
    fileID::Union{Int, Nothing}
end

function disk_to_string_arr(data::Array{diskVal,1})::Array{String,1}
    str = Array{String,1}()
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

function find_first_large_gap(data::AbstractVector{String}, min_len::Int)::Union{Tuple{Int,Int},Nothing}
    s = 1
    while s <= length(data)
        gap_start = findnext(x -> x == "_", data, s)
        if isnothing(gap_start)
            return nothing
        end

        gap_end = findnext(x -> x != "_", data, gap_start)

        if isnothing(gap_end)
            gap_end = length(data)
        else
            gap_end -= 1
        end

        gap_length = gap_end - gap_start + 1
        if gap_length >= min_len
            return (gap_start, gap_end)
        end
        s = gap_end + 1
    end
    return nothing
end

function compress_disk_alt(data::Array{diskVal,1})::Array{String,1}
    seen_id = Set{String}()
    push!(seen_id, "_")
    data_str_arr::Array{String,1} = disk_to_string_arr(data)
    while true
        last_val::Union{Int,Nothing} = findlast(x -> !(x in seen_id), data_str_arr)

        if isnothing(last_val)
            break
        end

        push!(seen_id, data_str_arr[last_val])

        len_vals::Union{Int,Nothing} = findlast(x-> x == data_str_arr[last_val], @view data_str_arr[last_val:-1:1])

        gap::Union{Tuple{Int,Int},Nothing} = find_first_large_gap(data_str_arr, len_vals)

        if isnothing(gap) || gap[1] > last_val
            continue
        end

        for i in 0:1:len_vals-1
           data_str_arr[gap[1]+i] = data_str_arr[last_val-i]
           data_str_arr[last_val-i] = "_"
        end
    end
    return data_str_arr
end

function main()
    f = open("input", "r")
    input = strip(read(f, String))

    if length(input)%2 == 1
        input *= "0"
    end

    total_len::Int = length(input)

    data::Array{Tuple{Int,Int},1} = [(parse(Int, s[1]), parse(Int, s[2])) for s in [t for t in Iterators.partition(input, 2)]]

    temp::Array{diskVal,1} = similar([], diskVal,total_len)
    for (i::Int, v::Tuple{Int,Int}) in enumerate(data)
        temp[2*i-1] = diskVal(v[1], i-1)
        temp[2*i]   = diskVal(v[2], nothing)
    end
    
    println(calc_checksum(compress_disk_alt(temp)))
end

@time "Runtime: " main()