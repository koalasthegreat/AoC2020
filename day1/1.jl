nums = readlines();

nums = [parse(Int, n) for n in nums];

for (index, num) in enumerate(nums)
    for (other_index, other_num) in enumerate(nums)
        if index != other_index
            sum = num + other_num;
            
            if sum == 2020
                println(num * other_num);
                exit();
            end
        end
    end
end
