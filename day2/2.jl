password_data = [split(line, " ") for line in readlines()];

valid_passwords = 0;

for data in password_data
    (yes, no) = (parse(Int, num) for num in split(data[1], "-"));

    policy = data[2][1];

    password = data[3];

    if (password[yes] == policy) ⊻ (password[no] == policy)
        global valid_passwords += 1;
    end
end

println(valid_passwords);