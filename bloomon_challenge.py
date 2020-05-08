from collections import defaultdict
from os.path import exists
import re
from operator import sub

print('-'*20)
print('Greetings!')
print('Welcome to Bloomon')
print('-'*20)

while True:
    try:
        designs_amount = int(input('Please enter amount of bouquet designs : '))
    except:
        print("ERROR, must be INT")
        continue
    break
print('We have ', designs_amount, ' bouquet design(s)')

bouquet_designs = []

for i in range(designs_amount):
    bouquet_designs.append(input('Enter bouquet design : '))

print("Enter filename and its path to open a list of available flowers (expl, c:\\folder\\filename.txt):")
filename = input("=> ")

while exists(filename) != True:
    print("File with name %r does not exist." % filename, '\n')
    print("Enter filename:", '\n')
    filename = input("=> ")

def read_from_file(filename: str):
    global total_flowers
    total_flowers = defaultdict(int)
    with open(filename, 'r') as f:
        for line in f:
            if len(line) == 3:
                total_flowers[line.strip()] += 1
    return total_flowers

read_from_file(filename)

sum_of_flowers = (sum([v for k, v in total_flowers.items()], 0))
# amount_of_flowers = []

print('-'*20)
print('Available flowers : ')
for k in sorted(total_flowers):
    print(k, ' -> ', total_flowers[k])
    # amount_of_flowers.append(total_flowers[k])
print('-'*20)
print('Total amount of flowers : ', sum_of_flowers)
print('\n')

for each in bouquet_designs:
    if each[1] == 'L':
        # initializing search key string
        search_key = 'L'
        # Using filter() + lambda
        # Substring Key match in dictionary
        res = filter(lambda elem_flower: search_key in elem_flower[0], total_flowers.items())
        sorted_res = sorted(res)
        sorted_res_out = list(sum(sorted_res, ()))
        for item in sorted_res_out:
            if item.isalpha():
                sorted_res_out.remove(item)

        test_str = each

        match_bouquet = re.match(r"([A-Z][LS])((\d+[a-z])+)(\d+)", test_str)
        flower_specie_and_size = match_bouquet.groups()[0]
        flowers = match_bouquet.groups()[1]
        sum_of_flowers_in_bouquet = int(match_bouquet.groups()[3])
        match_flowers = re.findall(r'\d+[a-z]', flowers)
        match_flowers_nums = re.findall(r'\d+', flowers)
        result_array = []
        for elem in match_flowers_nums:
            result_array.append(int(elem))
        match_flowers_nums = result_array
        # printing result
        print("Relevant flowers for design ", each + '  ' + str(sorted_res))
        print('Flowers needed for this bouquet ', match_flowers_nums)
        print("We have  ", sorted_res_out)

        if sum_of_flowers_in_bouquet == sum(match_flowers_nums):
            print("OK, sum of flowers in design = sum of flowers we need")
        elif sum_of_flowers_in_bouquet > sum(match_flowers_nums):
            print("We need extra flowers!")

        else:
            BlockingIOError("ERROR")

        remaining_flowers = map(sub, sorted_res_out, match_flowers_nums)
        print("Bouquet created! Remaining flowers : ", list(remaining_flowers))

        print("\n")

    elif each[1] == 'S':
        search_key = 'S'
        res = filter(lambda item_flower: search_key in item_flower[0], total_flowers.items())
        sorted_res = sorted(res)
        sorted_res_out = list(sum(sorted_res, ()))
        for item in sorted_res_out:
            if item.isalpha():
                sorted_res_out.remove(item)

        test_str = each

        match_bouquet = re.match(r"([A-Z][LS])((\d+[a-z])+)(\d+)", test_str)
        flower_specie_and_size = match_bouquet.groups()[0]
        flowers = match_bouquet.groups()[1]
        sum_of_flowers_in_bouquet = int(match_bouquet.groups()[3])
        match_flowers = re.findall(r'\d+[a-z]', flowers)
        match_flowers_nums = re.findall(r'\d+', flowers)
        result_array = []
        for elem in match_flowers_nums:
            result_array.append(int(elem))
        match_flowers_nums = result_array
        if len(sorted_res_out) > len(match_flowers_nums):
            sorted_res_out.pop()
        print("Relevant flowers for design ", each + '  ' + str(sorted_res))
        print('Flowers needed for this bouquet ', match_flowers_nums)
        print("We have  ", sorted_res_out)

        if sum_of_flowers_in_bouquet == sum(match_flowers_nums):
            print("OK, sum of flowers in design = sum of flowers we need")
        elif sum_of_flowers_in_bouquet > sum(match_flowers_nums):
            subtr_flowers = sum_of_flowers_in_bouquet - sum(match_flowers_nums)
            print("We need extra flower(s)! - ", subtr_flowers)
            max_index = sorted_res_out.index(max(sorted_res_out))
            match_flowers_nums[max_index] = match_flowers_nums[max_index] + subtr_flowers

        else:
            BlockingIOError("ERROR")

        remaining_flowers = map(sub, sorted_res_out, match_flowers_nums)
        print("Bouquet created! Remaining flowers : ", list(remaining_flowers))
        print("\n")

