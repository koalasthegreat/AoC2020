password_data = [split(line, " ") for line in readlines()];

valid_passwords = 0;

for data in password_data
    (minimum, maximum) = (parse(Int, num) for num in split(data[1], "-"));

    policy = data[2][1];

    password = data[3];

    count = 0;

    for char in password
        if char == policy
            count += 1;
        end
    end

    if (count >= minimum) & (count <= maximum)
        global valid_passwords += 1;
    end
end

println(valid_passwords);
