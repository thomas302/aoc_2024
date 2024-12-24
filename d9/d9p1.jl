using Base.Iterators

f = open("input", "r")
input = strip(read(f, String))

println(length(input))
if length(input)%2 == 1
    input *= "0"
end

temp = [s for s in Iterators.partition(input, 2)]

data = [(parse(Int, s[1]), parse(Int, s[2])) for s in temp]

temp = [repeat(string(id-1),v[1])*repeat("_",v[2]) for (id,v) in enumerate(data)]

data =[]
for i in temp
    for c in i
        push!(data, c)
    end
end

while true
    first_gap = findfirst(x -> x == '_', data)
    last_val = findlast(x -> isdigit(x), data)

    if first_gap > last_val
        break
    end

    data[first_gap] = data[last_val]
    data[last_val] = '_' 
end

cnt = 0
for (i,v) in enumerate(data)
    if isdigit(v)
        global cnt += (i-1)*parse(Int, v)
    else
        break
    end
end

println(cnt)