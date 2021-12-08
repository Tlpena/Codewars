# def reverse_words(s):
#    return " ".join(str.split(" ")[::-1])
#    print(s.split(" ")[::-1])
#
#
# reverse_words("hello world")
#
# def largest_pair_sum(numbers):
#     return sum(sorted(numbers)[-2:])
#
# print(largest_pair_sum([10, 14, 2, 23, 19]))
#
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if distance_to_pump//mpg == fuel_left:
#         return True
#     else:
#         return False
#
#
# print(zero_fuel(50, 25, 2))
# print(zero_fuel(100, 50, 1))
#
# def reverse_bits(n):
#     return int(bin(n)[:1:-1], 2)
#
# print(reverse_bits(58))
#
# def find_average(numbers):
#     return (sum(numbers)/len(numbers))
#
#
# print(find_average([1, 2, 3]))
#
# def valid_spacing(s):
#     return s == ' '.join(s.split())
#
# print(valid_spacing('Hello world'))
#
# def flip(d, a):
#     if d == 'R':
#         return sorted(a, reverse=False)
#     else:
#         return sorted(a, reverse=True)
#
#     return sorted(a, reverse=d=='L')
#
# print(flip('R', [3, 2, 1, 2]))
# print(flip('L', [1, 4, 5, 3, 5]))
#
# def people_with_age_drink(age):
#     if age < 14:
#         print('drink toddy')
#     if 14<= age > 18:
#         print('drink coke')
#     if 18 <= age >= 20:
#         print('drink beer')
#     if age >= 21:
#         print('drink whisky')
#
# print(people_with_age_drink(13))
#
# def get_count(input_str):
#     num_vowels = 0
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for i in input_str:
#         if i in vowels:
#             num_vowels = num_vowels + 1
#
#     return num_vowels
#
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")
#
# print(get_count('abracabasdiouhoda'))
#
# def bmi(weight, height):
#     b = weight/(height^2)
#     if b <= 18.5:
#         return "Underweight"
#     if 18.5 < b <= 25:
#         return "Normal"
#     if 25 < b <= 30:
#         return "Overweight"
#     else:
#         return "Obese"
#
# def even_last(numbers):
#     return sum(numbers[::2]) * numbers[-1] if numbers else 0
#
# def make_upper_case(s):
#     return s.upper()
#
# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# def goose_filter(birds):
#     new_list = []
#     for bird in birds:
#         if bird not in geese:
#             new_list.append(bird)
#     return new_list
#
#     return [bird for bird in birds if bird not in geese]
#
# def calculate(s):
#     return str(sum(int(n) for n in s.replace("minus", "plus-").split("plus")))
#
# print(calculate('1plus2plus3plus4'))
#
# def nb_year(p0, percent, aug, p, n=0):
#     while p > p0:
#         p0 += p0*percent/100 + aug
#         n += 1
#     return n
#
# print(nb_year(1500, 5, 100, 5000))
#
# def mygcd(x, y):
#     while y:
#         x, y=y, x%y
#     return x
#
#
#
# print(mygcd(30, 12))

# def quarter_of(month):
#     quarter1 = [1, 2, 3]
#     quarter2 = [4, 5, 6]
#     quarter3 = [7, 8, 9]
#     quarter4 = [10, 11, 12]
#
#     if month in quarter4:
#         return 4
#     if month in quarter3:
#         return 3
#     if month in quarter2:
#         return 2
#     else:
#         return 1
# print(quarter_of(8))
#
# def last_survivor(letters, coords):
#     l = [x for x in letters]
#     [l.pop(x) for x in coords]
#     return l[0]
#
# print(last_survivor('abc', [1, 1]))
#
# def game(words):
#     new_list = []
#     c = 0
#     for word in words:
#         if word == "":
#             return new_list
#         if not(c):
#             last = word[-1]
#             new_list.append(word)
#             c += 1
#             continue
#         if word[0] == last:
#             last = word[-1]
#             new_list.append(word)
#         else:
#             return new_list
#     return new_list
#
# # print(game(["dog","goose","elephant","tiger","rhino","or","cat"]))
#
# def area_or_perimeter(l, w):
#     if l == w:
#         return l * w
#     else:
#         return (l*2 + w*2)
#
# def decode(string):
#     return string.translate(str.maketrans("1234567890", "9876043215"))
#
# print(decode("4103432323"))
#
# def grid_map(inp, op):
#     return [list(map(op, i)) for i in inp]
#
#
# x = [[1, 2, 3], [4, 5, 6]]
# print(grid_map(x , lambda x: x + 1))
#
# def sum_differences_between_products_and_LCMs(pairs):
#     from fractions import gcd
#     return sum(a*b - a*b//gcd(a,b) for a, b in pairs if a and b)
#
#
# print(sum_differences_between_products_and_LCMs([[15,18], [4,5], [12,60]]))
#
# def switcher(arr):
#     d = {str(i): chr(123-i) for i in range(1,27)}
#     d.update({'27':'!'})
#     d.update({'28':'?'})
#     d.update({'29':' '})
#     d.update({'0':''})
#     return ''.join([d[str(i)] for i in arr])
#
# def small_enough(array, limit):
#     for i in array:
#         if not i <= limit: return False
#     return True
#
#
#
# print(small_enough([78, 117, 110, 99, 104, 117, 107, 115] , 100))
#
# def solve(arr):
#     final_list = []
#     for num in arr[::-1]:
#         if num not in final_list:
#             final_list.append(num)
#     return final_list[::-1]
#
# print(solve([3, 4, 4, 3, 6, 3]))
#
# def odd_or_even(arr):
#     return 'even' if sum(arr) % 2 == 0 else 'odd'
#
# print(odd_or_even([1, 1, 2]))
#
# def not_visible_cubes(num):
#     return max(num - 2, 0) ** 3
#
# print(not_visible_cubes(3))
#
#
# def get_position(n):
#     return n%3, n//3%3, n//9%3
#
# print(get_position(98))

# def printer_errors(s):
#     bad = []
#     for i in range(0, len(s)):
#         if s[i] in 'nopqrstuvwyxz':
#             bad.append(s[i])
#         else:
#             continue
#     return f"{len(bad)}/{len(s)}"
#
#     return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
#
# print(printer_errors("aaaxbbbbyyhwawiwjjjwwm"))
#
# def order_food(lst):
#     vegetarian_list = []
#     standard_list = []
#     vegan_list = []
#     for i in range(0, len(lst)):
#         if lst[i]['meal'] == 'vegetarian':
#             vegetarian_list.append(i)
#         if lst[i]['meal'] == 'standard':
#             standard_list.append(i)
#         else:
#             vegan_list.append(i)
#
#     return f"('vegetarian': {len(vegetarian_list)}, 'standard': {len(standard_list)}, 'vegan': {len(vegan_list)}}"
#
# print(order_food([
#     { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
#     { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
#     { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
#     { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
# ]))
#
# def vowel_indices(word):
#     return [i for i,x in enumerate(word,1) if x.lower() in 'aeiouy']
#
# print(vowel_indices("apple"))
#
# def travel(r, zipcode):
#     streets = []
#     nums = []
#     addresses = r.split(',')
#     for address in addresses:
#         if ' '.join(address.split()[-2:]) == zipcode:
#             streets.append(' '.join(address.split()[1:-2]))
#             nums += address.split()[:1]
#     return '{}:{}/{}'.format(zipcode, ','.join(streets), ','.join(nums))
#
# def f(iterable, integer):
#     return len(integer) if len(integer) > integer else 0
#
# f=lambda t,n:len(t)*(len(t)>n)
#
# def swap(s, n):
#     n = str(bin(n))[2:]
#     index = 0
#     new_s = ''
#     for letter in s:
#         if letter.isalpha():
#             if n[index%len(n)]=='1':
#                 new_s += letter.swapcase()
#             else:
#                 new_s += letter
#             index+=1
#         else:
#             new_s += letter
#     return new_s
#
#
# print(swap("Hello world!", 10))
#
# def check_sequence(sequence, L, N):
#     return sum(1 for r in sequence.replace('HT', 'H T').replace('TH', 'T H').split() if len(r) == L) == N
#
# print(check_sequence('HHHHTTHTHHTH', 4, 1))
#
# def high_and_low(numbers):
#     nn = [int(s) for s in numbers.split(" ")]
#     return "%i %i" % (max(nn),min(nn))
#
# print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
#
# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
#
# print(accum("Abcd"))
#
# def disemvowel(string_):
#     return "".join(c for c in string_ if c.lower() not in "aeiou")
#
#
# print(disemvowel("This website is for losers LOL!"))
#
# from math import ceil
#
# def new_avg(arr, newavg):
#      value = int(ceil((len(arr)+1) * newavg - sum(arr)))
#      if value < 0:
#           raise ValueError
#
#      return value
#
# print(new_avg([14, 30, 5, 7, 9, 11, 16], 90))
#
# def first_non_consecutive(arr):
#     first = arr[0]
#     for i in arr:
#         if i == first:
#             first += 1
#         else:
#             return i
#
# print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))
#
# def hoop_count(n):
#     return 'Great, now move on to tricks' if n >= 10 else 'Keep at it until you get it'
#
# print((hoop_count(3)))
#
# def solution(string, ending):
#     return string.endswith(ending)
#
# print(solution('samurai', 'ai'))
#
# def waterbombs(fire, w):
#     new = fire.split('Y')
#     bombs = 0
#
#     for i in range(0, len(new)):
#         if len(new[i]) <= w:
#             bombs += 1
#         else:
#             continue
#     return bombs
#
#
# print(waterbombs('xxxxYxYx', 4))
#
# def connotation(strng):
#     new = strng.split(' ')
#     positive = 0
#     for i in range(0, len(new)):
#         if new[i][0] in 'abcdefghijklmABCDEFGHIJKLM':
#             positive += 1
#         i += 1
#     return True if positive >= len(new)/2 else False
#
#     lst = s.upper().split()
#     return sum('A'<=w[0]<='M' for w in lst) >= len(lst)/2
#
#
# print(connotation("A big brown fox caught a bad rabbit"))

# def task(w, n, c):
#     if w == 'Monday':
#         name = 'James'
#     if w == 'Tuesday':
#         name = 'John'
#     if w == 'Wednesday':
#         name = 'Robert'
#     if w == 'Thursday':
#         name = 'Michael'
#     if w == 'Friday':
#         name = 'William'
#     return f'It is {w} today, {name}, you have to work, you must spray {n} tress and you need {n*c} dollars to buy liquid'
#
# print(task('Wednesday', 10, 2))
#
# def to_time(seconds):
#     if round(seconds/60/60) < 1:
#         x = 0
#     else:
#         x = round(seconds/60/60)
#     return f'{x} hour(s) and {round(seconds/60%60)} minute(s)'
#
# print(to_time(3660))
#
# def strange_math(n, k):
#     return sorted(range(n+1), key=str).index(k)
#
# print(strange_math(11, 2))
#
# def chess_knight(cell):
#     x, y = (ord(c) - ord(origin) for c, origin in zip(cell, 'a1'))
#     return sum(0 <= x + dx < 8 and 0 <= y + dy < 8 for dx, dy in (
#         (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)))
#
# print(chess_knight('a1'))
#
# def each_cons(lst, n):
#     return [lst[i:i+n] for i in range(len(lst) - n + 1)]
#
# print(each_cons([3, 5, 8, 13], 2))
#
# def distance_between_points(a, b):
#     return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** .5
# def twice_as_old(dad_years_old, son_years_old):
#     new = son_years_old * 2
#     return abs(dad_years_old - new)
#
# def pipe_fix(nums):
#     new_list = []
#     for i in range(nums[0], nums[-1]+1):
#         new_list.append(i)
#         i += 1
#     return new_list
#
#
#
# print(pipe_fix([1, 2, 3, 5, 6, 8, 9]))
#
#
# def crusoe(n, d, ang, dist_mult, ang_mult):
#     import math
#     x = 0
#     y = 0
#     for i in range(n):
#
#         x += d * math.cos((ang/180)*math.pi)
#         y += d * math.sin((ang/180)*math.pi)
#         d = d * dist_mult
#         ang = ang * ang_mult
#
#     return (x,y)
#
#
#
# print(crusoe(8, 0.22, 3, 1.01, 1.15))
#
#
# def solve(arr):
#    return [sum(c == chr(97+i) for i,c in enumerate(w[:26].lower())) for w in arr]
#
#
# print(solve(["abode","ABc","xyzD"]))
#
#
# def last_survivors(string):
#     ans = list(string); abc = list(map(chr, range(97, 123)))
#     abc.append('a')
#     for f in range(len(string)):
#         for i in ans:
#             if ans.count(i) >= 2:
#                 index = abc.index(i)
#                 ans.remove(i); ans.remove(i)
#                 ans.append(abc[index + 1])
#
#     return "".join(ans)
#
#
# print(last_survivors('zzzab'))
#
# def get_real_floor(n):
#     if 0 < n < 13:
#         return n - 1

#     if n >= 13:
#         return n -2
#     else:
#         return n
#
#
#
# print((get_real_floor(15)))
#
# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number = i * number
#     return number
#
# print(factorial(5))
#
# def average(array):
#     return round(sum(array)/len(array))
#
# print(average([5, 78, 52, 900, 1]))
#
# def cool_string(s):
#     return s.isalpha() and all(x.islower() != y.islower() for x, y in zip(s, s[1:]))
#
# print(cool_string("aQwFdA"))
#
# def plant(seed, water, fert, temp):
#     ans = ''
#     if temp > 30 or temp < 20:
#         return ('-'*water)*water + seed
#     else:
#         ans = ans + ('-'*water+ seed*fert)*water
#     return ans
#
#
# print(plant(";", 9, 10, 30))
#
# def nb_dig(n, d):
#     return sum(str(i*i).count(str(d)) for i in range(n+1))
#
# print(nb_dig(5750, 0))
#
# def max_rot(n):
#     n = str(n)
#     first = n[1:] + n[0]
#     second = first[0] + first[2:] + first[1]
#     third = second[0:2] + second[3:] + second[2]
#     fourth = third[0:3] + third[4:] + third[3]
#     list = sorted([first, second, third, fourth])
#     return int(list[-1])
#
#
# print(max_rot(56789))
#
# import math
# def pyramid(balls):
#     i = 1
#     while i <= balls:
#         balls = balls - i
#         i += 1
#     return i-1
#
# print(pyramid(20))
#
# def bumps(road):
#
#     return "Woohoo!" if road.count('n') <= 15 else "Car Dead"
#
# print(bumps('nnnnnnn'))
#
# def fly_by(lamps, drone):
#     return lamps.replace('x', 'o', (drone.find('T')+1))
#
# print(fly_by('xxxxxx', '====T'))
#
# def switcheroo(s):
#     return s.translate(str.maketrans('ab', 'ba'))
#
#
# print(switcheroo('aaaaabbbccccaaaa'))
#
# def paint_letterboxes(start, finish):
#     new = ''
#     for i in range(start, finish + 1):
#         new += str(i)
#     return [new.count('0'), new.count('1'), new.count('2'), new.count('3'), new.count('4'), new.count('5'), new.count('6'), new.count('7'), new.count('8'), new.count('9'),]
#
# print(paint_letterboxes(125, 132))
#
# def circle_of_numbers(n, fst):
#     if fst + n/2 < n:
#         fst = fst + n/2
#     else:
#         fst = fst - n/2
#     return fst
#
# print(circle_of_numbers(10, 7))
#
# def solution(value):
#     return "Value is %05d" % value
# print(solution(109))
#
# def is_isogram(string):
#     return len(string) == len(set(string.lower()))
#
# print(is_isogram('aba'))
#
# def count_name(arr, name):
#     return MAINLIST.count(name)
#
# MAINLIST = ["Bob","Ted","Amy","Alice","Bob","Ted","Amy","Ted","Amy","Fred"]
# print(count_name(MAINLIST, "Ted"))
#
# def fit_in(a, b, m, n):
#     return 2*(a*b) <= m*n
#
#
# print(fit_in(1, 2, 1, 2))
#
# def alternate_case(s):
#     return s.swapcase()
#
#
# print(alternate_case("ABC"))
#
# def well(x):
#     points = {'life': 0, 'eating': 1, 'kata': 5, 'Petes kata': 10}
#     misery = sum(map(points.get, x))
#     return ['Miserable!', 'Sad!', 'Happy!', 'Super happy!'] \
#         [(misery<40)+(misery<70)+(misery<100)]
#
# print(well(['life', 'eating', 'life']))
#
# def gps(s, x):
#     return max([(n-m)*3600/s for (m,n) in zip(x,x[1:])])
#
# print(gps(15, ))
#
# def sabb(s, val, happiness):
#     num = 0
#     for letter in s:
#         if letter.lower() in 'sabbatical':
#             num += 1
#     if num + val + happiness > 22:
#         return 'Sabbatical! Boom!'
#     else:
#         return 'Back to your desk, boy.'
#
# print(sabb('Please calm down', 9, 1))
#
# def stray(arr):
#     for number in arr:
#         if arr.count(number) < 2:
#             return number
#
# print(stray([1, 1, 1, 1, 1, 1, 2]))
#
# def filter_long_words(sentence, n):
#     return [word for word in sentence.split() if len(word) > n]
#
#
# print(filter_long_words("The quick brown fox jumps over the lazy dog", 4))
#
# def broken(inp):
#
#     return inp.translate(str.maketrans('10', '01'))
#
# print(broken('0000001001010000111110101000'))
#
# def solution(nums):
#     return sorted(nums) if nums else []
#
#
# print(solution([1, 2, 3, 9, 5]))
# import string
#
#
# def the_janitor(word):
#     return [word.rindex(c) - word.index(c) + 1 if c in word else 0 for c in string.ascii_lowercase]
#
# print(the_janitor('abacaba'))
#
# def min_permutation(n):
#     f = n < 0
#     s = "".join(sorted(str(abs(n))))
#     n = s.count("0")
#     s = s.replace("0", "")
#     return int(s[:1] + "0" * n + s[1:]) * (-1 if f else 1)
#
#
# print(min_permutation(29394))
#
# def buy(x, arr):
#     for i, y in enumerate(arr[:-1]):
#         for j, z in enumerate(arr[i+1:]):
#             if y + z == x:
#                 return [i, i + j + 1]
#
# print(buy(5,[5,2,3,4,5]))
#
# def divisions(n, divisor):
#     times = 0
#     while n >= divisor:
#         n = n // divisor
#         times += 1
#
#     return times
#
#     from math import log
#     return int(log(n, divisor))
#
# print(divisions(100, 2))
#
# def meeting(rooms):
#     return rooms.index('O') if 'O' in rooms else "None available!"
#
# print(meeting(['X', 'O', 'X']))
#
# def easyline(n):
#     import math
#     return math.factorial(2*n)/(math.factorial(n)**2)
#
# print(easyline(4))
#
# def reverse_number(n):
#     return int(str(n)[::-1])
#
# print(reverse_number(123))
#
# def binary_array_to_number(arr):
#     return int(''.join(str(i) for i in arr), 2)
#
# print(binary_array_to_number([0,0,1,0]))
#
# def olympic_ring(string):
#     counter = 0
#     for letter in string:
#         if letter in 'abdegoqpADQROP':
#             counter += 1
#         if letter in 'B':
#             counter += 1
#     if counter//2 >= 3:
#         return 'Gold!'
#     if counter//2 < 1:
#         return 'Not even a medal!'
#     if 2 > counter//2 >= 1:
#         return 'Bronze!'
#     if 3 > counter//2 >= 2:
#         return 'Silver!'
#
# print(olympic_ring('wHjMudLwtoPGocnJ'))
#
# def gordon(a):
#     return '!!!! '.join(a.upper().split()).translate(str.maketrans('AEIOU', '@****'))+'!!!!'
#
# print(gordon('What feck damn cake'))
#
# def adjacent_element_product(array):
#     return max(a*b for a,b in zip(array, array[1:]))
#
# print(adjacent_element_product([1, 5, 10, 9]))
#
#
# import string
# def sort_transform(arr):
#     new = ''
#     for number in arr:
#         new += chr(number)
#     answer = new[:2]
#     answer += new[-2:]
#     for number in sorted(arr):
#
#     # return f'{answer}-{answer}-{answer}-{answer}'
#
# print(sort_transform([111, 112, 113, 114, 115, 113, 114, 110]))
import collections
import math
import string


#
#
# def move_ten(st):
#     return ''.join(chr(ord(i)+10) if i<'q' else chr(ord(i)-16) for i in st)
#
# print(move_ten('testcase'))
#
# def has_unique_chars(string):
#     return len(string) == len(set(string))
#
# print(has_unique_chars('++-'))
#
# def sum_cubes(n):
#     # new = []
#     # for i in range(1, n+1):
#     #     new.append(i**3)
#     # return sum(new)
#
#     return sum((i**3) for i in range(1, n+1))
#
# print(sum_cubes(3))
#
# def find_deleted_number(arr, mixed_arr):
#     return sum(arr) - sum(mixed_arr)
#
# print(find_deleted_number([1, 2, 3, 4, 5], [3, 4, 1, 5]))
#
# def solution(s):
#     return sum(1 for i in range(len(s)) if i and s[i-1]==s[i])
#
# print(solution('RGBRGBRRGGRBBGBBBRGRBRBGRBGRG'))
# import math
# def shortest_distance(a, b, c):
#     d1 = math.sqrt(a**2 + b**2)
#     d2 = math.sqrt(d1**2 + c**2)
#     return d2
#
# print(shortest_distance(1, 2, 3))
#
# def plane_seat(a):
#     front, middle, back = (range(1,21), range(21,41), range(41,61))
#     left, center, right = ('ABC', 'DEF', "GHK")
#     x, y = ('', '')
#
#     if int(a[:-1]) in front:
#         x = 'Front-'
#     if int(a[:-1]) in middle:
#         x = 'Middle-'
#     if int(a[:-1]) in back:
#         x = 'Back-'
#
#     if a[-1] in left:
#         y = 'Left'
#     if a[-1] in center:
#         y = 'Middle'
#     if a[-1] in right:
#         y = 'Right'
#
#     return x+y if all((x,y)) else 'No Seat!!'
#
#
# print(plane_seat('2B'))
#
# def inverse_slice(items, a, b):
#     return items[:a] + items[b:]
#
# def sort_vowels(s):
#     try:
#         return '\n'.join('|' + i  if i.lower() in 'aioue' else i + '|' for i in s)
#     except:
#         return ''
#
#
# print(sort_vowels('Codewars'))
#
# def cat_mouse(x):
#     return 'Escaped!' if x.count('.') > 3 else 'Caught!'
#
# print(cat_mouse('C....m'))
#
# def likes(names):
#     if len(names) == 1:
#         return f'{names[0]} likes this'
#     if len(names) == 2:
#         return f'{names[0]} and {names[1]} like this'
#     if len(names) == 3:
#         return f'{names[0]}, {names[1]} and {names[2]} like this'
#     if len(names) >= 4:
#         return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
#     else:
#         return 'no one likes this'
#
# print(likes(['Peter']))

# def alphabet_position(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
#
# print(alphabet_position('Hello'))
#
# def unique_in_order(iterable):
#     output_list = []
#     current_letter = None
#     for letter in iterable:
#         if letter != current_letter:
#             output_list.append(letter)
#             current_letter = letter
#     return output_list
#
#
# print(unique_in_order('AAAABBBBCCCCDDDABB'))
#
# def is_prime(num):
#     divisors = []
#     if num <= 1:
#         return False
#     for i in range(1, num+1):
#         if num % i == 0:
#             divisors.append(i)
#             if len(divisors) > 2:
#                 return False
#     return True
#
# print(is_prime(75))
#
# import string
#
# def is_pangram(s):
#     return set(string.ascii_lowercase) <= set(s.lower())
#
# def delete_nth(order, max_e):
#     for i in str(order):
#         if
#
#
# print(delete_nth([20, 37, 20, 21], 1))
#
# import math
#
# def is_square(n):
#     if n == 0:
#         return True
#     if n < 0:
#         return False
#     if math.sqrt(n) == round(math.sqrt(n)):
#         return True
#     else:
#         return False
#
#
# def xo(s):
#     return s.count('x') == s.count('o')
#
# def sum_two(numbers):
#     return sum(sorted(numbers)[0:2])
#
# print(sum_two([19, 5, 42, 2, 77]))
#
# def find_unique(arr):
#     a = sorted(arr)
#     return a[0] if a[0] != a[1] else a[-1]
#
# print(find_unique([1, 1, 1, 2, 1, 1]))
#
# def tickets(people):
#     till = {100.0:0, 50.0:0, 25.0:0}
#
#     for paid in people:
#         till[paid] += 1
#         change = paid-25.0
#
#     for bill in (50,25):
#         while (bill <= change and till[bill] > 0):
#             till[bill] -= 1
#             change -= bill
#
#     if change != 0:
#         return 'NO'
#
#     return 'YES'
#
# print(tickets([25, 50, 25, 100]))
#
# def tower_builder(n):
#     return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
#
# print(tower_builder(4))
#
# def longest(a1, a2):
#     return ''.join(sorted(set(a1+a2)))
#
# print(longest("aretheyhere", "yestheyarehere"))
#
# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()
#
#
# print(validate_pin('1a23'))
#
# def open_or_senior(data):
#     return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
#
# print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
#
# def is_triangle(a, b, c):
#     return a+b>c and a+c>b and b+c>a
#
#
# print(is_triangle(1, 2, 2))
#
#
# def high(x):
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
#
# print(high('man i need a taxi up to ubud'))
#
# def count(string):
#     return {i: string.count(i) for i in string}
#
# print(count('aba'))
#
# def solution(romans):
#     roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
#     i = 0
#     num = 0
#     while i < len(romans):
#         if i + 1 < len(romans) and romans[i:i+2] in roman:
#             num += roman[romans[i:i+2]]
#             i += 2
#         else:
#             num += roman[romans[i]]
#             i += 1
#     return num
#
# print(solution("V"))
#
# def reverse_words(text):
#     return ' '.join(s[::-1] for s in text.split(' '))
#
# print(reverse_words('apple is good'))
# import math
#
# def comp(array1, array2):
#     try:
#         return sorted([i ** 2 for i in array1]) == sorted(array2)
#     except:
#         return False
#
#
# print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))
#
# def dont_give_me_five(start, end):
#     return ('5' not in str(i) for i in range(start, end + 1))
#
#
#
# print(dont_give_me_five(4, 17))
#
# def is_anagram(test, original):
#     if sorted(test.lower()) == sorted(original.lower()):
#         return True
#     else:
#         return False
#
#
# print(is_anagram("foefet", "toffee"))
#
# def remove_smallest(numbers):
#     a = numbers[:]
#     if a:
#         a.remove(min(a))
#     return a
#
# print(remove_smallest([2, 1, 3, 4, 5]))
#
# def sum_digits(number):
#     return sum(int(d) for d in str(abs(number)))
#
#
# print(sum_digits(99))
#
# def triangular(n):
#     return n * (n + 1) // 2 if n > 0 else 0
#
#
# print(triangular(4))
#
# def capitalize(s):
#     answer1 = ''
#     answer2 = ''
#     for a,b in enumerate(s):
#         if a%2 == 0:
#             answer1 += b.upper()
#             answer2 += b.lower()
#         else:
#             answer1 += b.lower()
#             answer2 += b.upper()
#
#     return [answer1, answer2]
#
# print(capitalize('abcdef'))
#
# def min_max(lst):
#     lst = sorted(lst)
#     return [lst[0], lst[-1]]
#
# print(min_max([1, 2, 3, 4, 5]))
#
# def bouncing_ball(h, bounce, window):
#     if not 0 < bounce < 1: return -1
#     count = 0
#     while h > window:
#         count += 1
#         h *= bounce
#         if h > window: count += 1
#     return count or -1
#
#
#
# print(bouncing_ball(30, .66, 1.5))
#
# def find(n):
#     return sum([i for i in range(0, n+1) if i%3==0 or i%5==0])
#
# print(find(10))
#
# def valid_braces(string):
#     braces = {"(": ")", "[": "]", "{": "}"}
#     stack = []
#     for character in string:
#         if character in braces.keys():
#             stack.append(character)
#         else:
#             if len(stack) == 0 or braces[stack.pop()] != character:
#                 return False
#     return len(stack) == 0
#
# print(valid_braces('(({})'))
#
# def mxdiflg(a1, a2):
#     if len(a2) == 0:
#         return -1
#     if len(a1) == 0:
#         return -1
#     else:
#         answer = []
#         answer1 = []
#         for word in a1:
#             answer.append(len(word))
#         for word in a2:
#             answer1.append(len(word))
#         if max(answer1) - min(answer) > max(answer) - min(answer1):
#             return max(answer1) - min(answer)
#         else:
#             return max(answer) - min(answer1)
#
# print(mxdiflg(["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzaqaqgpssaqaqsa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
#               , ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]))
#
# def predict_age(*ages):
#     return sum(a*a for a in ages)**.5//2
#
# print(predict_age(65, 60, 75, 55, 60, 63, 64, 45))
#
# def remove_url_anchor(url):
#     return url.split("#")
# print(remove_url_anchor("www.codewars.com#about"))
#
# def arithmetic(a, b, operator):
#     return {'add': a+b, 'subtract': a-b, 'multiply': a*b, 'divide': a/b}[operator]
#
# print(arithmetic(1, 2, 'add'))
#
# def gimme(input_array):
#     return input_array.index(sorted(input_array)[1])
#
# print(gimme([2, 3, 1]))
#
# def min_value(digits):
#     return int("".join(map(str,sorted(set(digits)))))
#
# print(min_value([4, 7, 5, 7]))
#
# def validPhoneNumber(phoneNumber):
#     answer = ''
#     if phoneNumber.replace('-', '1') == phoneNumber:
#         return False
#     else:
#         for number in phoneNumber:
#             if number != '(':
#                 if number != ')':
#                     if number != '-':
#                         if number != ' ':
#                             answer += number
#         for n in answer:
#             if n.isdigit():
#                 return True
#             else:
#                 return False
#
#
# print(validPhoneNumber('(a23) 456-7890'))
#
# def expanded_form(num):
#     result = []
#
#     for index, digit in enumerate(str(num)[::-1]):
#         if int(digit) != 0:
#             result.append(digit + ('0' * index))
#
#     return ' + '.join(result[::-1])
#
# print(expanded_form(124))
#
# def goodVsEvil(good, evil):
#     points_good = [1, 2, 3, 3, 4, 10]
#     points_evil = [1, 2, 2, 2, 3, 5, 10]
#
#     good = sum([int(x)*y for x, y in zip(good.split(), points_good)])
#     evil = sum([int(x)*y for x, y in zip(evil.split(), points_evil)])
#
#     result = 'Battle Result: '
#
#     if good < evil:
#         return result +'Evil eradicates all trace of Good'
#     elif good > evil:
#         return result + 'Good triumphs over Evil'
#     else:
#         return result + 'No victor on this battle field'
#
#
# print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
#
# def parse(data):
#     answer = 0
#     returned = []
#     for letter in data:
#         if letter == 'o':
#             returned.append(answer)
#         if letter == 'i':
#             answer += 1
#         if letter == 'd':
#             answer -= 1
#         if letter == 's':
#             answer = answer**2
#     return returned
#
# print(parse('isoisoiso'))
#
# def clean_string(s):
#     stk = []
#     for c in s:
#         if c=='#' and stk: stk.pop()
#         elif c!='#':       stk.append(c)
#     return ''.join(stk)
#
# print(clean_string('abc#d##c'))
#
# def kebabize(s):
#     return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')
#
# print(kebabize('camelsHaveThreeHumps'))
#
# def find_squares(n):
#     m = (n-1)//2
#     return f'{(m+1)**2}-{m**2}'
#
# print(find_squares(9))
#
# def round_to_next5(n):
#     if n%5 == 0:
#         return n
#     else:
#         return n + (5 - n % 5)
#
# print(round_to_next5(7))
#
# def angle(n):
#     return (n-2)*180
#
# print(angle(4))
#
# def flatten_and_sort(array):
#
#     return sorted([j for i in array for j in i])
#
# print(flatten_and_sort([[3, 2, 1], [4, 6, 5], [9, 8, 7]]))
#
# def dashatize(num):
#     num_str = str(num)
#     for i in ['1','3','5','7','9']:
#         num_str = num_str.replace(i,'-' + i + '-')
#     return num_str.strip('-').replace('--','-')
#
# print(dashatize(5311))
# import math
#
# def nbr_of_laps(x, y):
#
#     answer = math.lcm(x, y)
#     return (answer//x, answer//y)
#
#
# print(nbr_of_laps(5, 3))
# print(nbr_of_laps(4, 6))
# print(nbr_of_laps(5, 5))
#
# import re
#
# PATTERN = re.compile(r'(\d{1,3})')
#
# def is_sum_of_cubes(s):
#     found = list(filter(lambda nStr: int(nStr) == sum(int(d)**3 for d in nStr), PATTERN.findall(s)))
#     return "Unlucky" if not found else "{} {} {}".format(' '.join(found), sum(map(int, found)), 'Lucky')
#
#
# print(is_sum_of_cubes('QK29a45[&erui9026315'))
#
#
# def restaurant(single_tables, double_tables, visitors):
#     kicked = 0
#     half = 0
#     for i in visitors:
#         if i == 1:
#             if single_tables > 0:
#                 single_tables -= 1
#             elif double_tables > 0:
#                 double_tables -= 1
#                 half += 1
#             elif half > 0:
#                 half -= 1
#             else:
#                 kicked += 1
#         if i == 2:
#             if double_tables > 0:
#                 double_tables -= 1
#             else:
#                 kicked += 2
#     return kicked
#
#
# print(restaurant(1, 1, [1, 1, 2, 1]))
#
# def capitals(word):
#     return [i for (i,c) in enumerate(word) if c.isupper()]
#
# print(capitals('fuZzdosIXTJIDcqTuaQaykilOcTPxq'))
#
# def solve(s):
#     combos = 0
#     another = []
#     answer = ''
#     for i in s:
#         if i in 'aeiou':
#             answer += ','
#         else:
#             answer += i
#     answer = answer.replace(',,', ',')
#     answer = answer.split(',')
#     for i in answer:
#         if len(i) == 1:
#             another.append(ord(i)-96)
#         if len(i) > 1:
#             for n in i:
#                 combos += (ord(n)-96)
#             another.append(combos)
#             combos = 0
#     return (another)

# print(solve('chruschtschov'))
#
# def encode(s, t=str.maketrans("aeiou", "12345")):
#     return s.translate(t)
#
# def decode(s, t=str.maketrans("12345", "aeiou")):
#     return s.translate(t)
#
# print(encode('hello'))
#
# def sum_dig_pow(a, b):
#     return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]
#
#
# print(sum_dig_pow(1, 100))
#
# def add(n):
#     return lambda x:x + n
#
# print(add(3))
#
# def evaporator(content, evap_per_day, threshold):
#     n = 0
#     current = 100
#     percent = 1 - evap_per_day / 100.0
#     while current > threshold:
#         current *= percent
#         n += 1
#     return n
#
# print(evaporator(10, 10, 10))
#
# def largest_pair_sum(numbers):
#     return sum(sorted(numbers)[-2:])
#
# print(largest_pair_sum([10, 14, 2, 23, 19]))
#
# def power_of_two(x):
#     return x != 0 and ((x & (x - 1)) == 0)
#
# print(power_of_two(1024))
#
# def play_pass(s, n):
#     # Step 1, 2, 3
#     shiftText = ""
#     for char in s:
#         if char.isdigit():
#             shiftText += str(9 - int(char))
#         elif char.isalpha():
#             shifted = ord(char.lower()) + n
#             shiftText += chr(shifted) if shifted <= ord('z') else chr(shifted - 26)
#         else:
#             shiftText += char
#
#     # Step 4
#     caseText = ""
#     for i in range(len(shiftText)):
#         caseText += shiftText[i].upper() if i % 2 == 0 else shiftText[i].lower()
#
#     # Step 5
#     return caseText[::-1]
#
# print(play_pass('BORN IN 2015!', 1))
#
# def sum_of_minimums(numbers):
#     answer = []
#     for i in numbers:
#         answer.append(min(i))
#     return sum(answer)
#
# print(sum_of_minimums([ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]))
#
# def is_valid_IP(strng):
#     lst = strng.split('.')
#     passed = 0
#     for sect in lst:
#         if sect.isdigit():
#             if sect[0] != '0':
#                 if 0 < int(sect) <= 255:
#                     passed += 1
#     return passed == 4
#
# print(is_valid_IP('12.255.56.1'))
#
# from collections import Counter
#
#
# def highest_rank(arr):
#     if arr:
#         c = Counter(arr)
#         m = max(c.values())
#         return max(k for k, v in c.items() if v == m)
#
#
# print(highest_rank([12, 10, 8, 4, 12, 7, 6, 4,4, 4, 10, 12]))
#
# from itertools import groupby
#
# def sum_consecutives(s):
#     return [sum(group) for c, group in groupby(s)]
#
# print(sum_consecutives([1,4,4,4,0,4,3,3,1]))
#
# def caffeine_buzz(n):
#     return ['mocha_missing!','Java','JavaScript','CoffeeScript'][sum([n%3==0,n%4==0,n%2==0])]
#
#
# print(caffeine_buzz(3))
#
# def group_by_commas(n):
#     return f'{n:,}'
#
# print(group_by_commas(100))
# print(group_by_commas(1000))
# print(group_by_commas(100000))
# print(group_by_commas(1000000))
# print(group_by_commas(1000000000))
#
# from collections import Counter
#
# def find_it(seq):
#     n = len(seq)
#     count_map = Counter(seq)
#
#     for i in range(0, n):
#
#         if (count_map[seq[i]] % 2 != 0):
#             return seq[i]
#
# print(find_it([5,4,3,2,1,5,4,3,2,10,10]))
#
# def parts_sum(ls):
#     new = []
#     ls = list(reversed(ls))
#     running_sum = 0
#     for number in ls:
#         running_sum += number
#         new.append(running_sum)
#     answer = list(reversed(new))
#     answer.append(0)
#     return answer
#
# print(parts_sum([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]))
#
# def triangle_type(a, b, c):
#     new = sorted([a, b, c])
#     if new[0] + new[1] <= new[2]:
#         return 0
#     if new[0]**2 + new[1]**2 > new[2]**2:
#         return 1
#     if new[0]**2 + new[1]**2 == new[2]**2:
#         return 2
#     if new[0]**2 + new[1]**2 < new[2]**2:
#         return 3
#
# print(triangle_type(7, 3, 2))
# print(triangle_type(8, 5, 7))
#
# def get_order(order):
#     menu = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke']
#     clean_order = ''
#     for i in menu:
#         clean_order += (i.capitalize() + ' ') * order.count(i)
#     return clean_order[:-1]
#
# print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))
#
# def twos_difference(lst):
#     return [(num, num+2) for num in sorted(lst) if num+2 in lst]
#
#
# print(twos_difference([1, 2, 3, 4]))
#
# def mineLocation(field):
#     for subfield in field:
#         if 1 in subfield: return [field.index(subfield), subfield.index(1)]
#
#
# print(mineLocation([ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0] ]))
#
# opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
#
# def dirReduc(plan):
#     new_plan = []
#     for d in plan:
#         if new_plan and new_plan[-1] == opposite[d]:
#             new_plan.pop()
#         else:
#             new_plan.append(d) 
#     return new_plan
#
#
# print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
#
# def extract_file_name(dirty_file_name):
#     first = dirty_file_name.split('_')
#     del first[0]
#     second = '_'.join(first)
#     second = second.split('.')
#     del second[-1]
#     return '.'.join(second)
#
# print(extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"))
#
# def to_nato(words):
#     answer = []
#     d = {
#         'A': 'Alpha',  'B': 'Bravo',   'C': 'Charlie',
#         'D': 'Delta',  'E': 'Echo',    'F': 'Foxtrot',
#         'G': 'Golf',   'H': 'Hotel',   'I': 'India',
#         'J': 'Juliett','K': 'Kilo',    'L': 'Lima',
#         'M': 'Mike',   'N': 'November','O': 'Oscar',
#         'P': 'Papa',   'Q': 'Quebec',  'R': 'Romeo',
#         'S': 'Sierra', 'T': 'Tango',   'U': 'Uniform',
#         'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
#         'Y': 'Yankee', 'Z': 'Zulu'}
#     for x in words.upper().split(' '):
#         for y in x:
#             if y in ',.!? ':
#                 answer.append(y)
#             else:
#                 answer.append(d[y])
#
#     return ' '.join(answer)
#
# print(to_nato('If you can read'))
#
# def up_array(arr):
#     if not arr or min(arr) < 0 or max(arr) > 9:
#         return None
#     else:
#         return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]
# print(up_array([9, 9, 9]))
#
# import re
# def is_alt(s):
#     return not re.search('[aeiou]{2}|[^aeiou]{2}',s)
#
# print(is_alt('apple'))
#
# def move_zeros(array):
#     new = []
#     zeros = []
#
#     for i in range(len(array)):
#         if array[i] == 0 or array[i] == 0.0:
#             if type(array[i]) == int or type(array[i]) == float:
#                 zeros.append(array[i])
#             else: new.append(array[i])
#         else:
#             new.append(array[i])
#
#     return new + zeros
#
#
# print(move_zeros([0, 0, 2, 1]))
#
# def sort_by_length(arr):
#     return sorted(arr, key=len)
#
# print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))
#
# def averages(arr):
#     answer = []
#     for i,j in zip(arr, arr[1:]):
#         answer.append((i+j)/2)
#     return answer
#
# print(averages([1, 3, 5, 1, -10]))
#
# def alphabet_war(fight):
#     d = {'w':4,'p':3,'b':2,'s':1,
#          'm':-4,'q':-3,'d':-2,'z':-1}
#     r = sum(d[c] for c in fight if c in d)
#
#     return {r==0:"Let's fight again!",
#             r>0:"Left side wins!",
#             r<0:"Right side wins!"
#             }[True]
#
#
# print(alphabet_war('wqbs'))
#
# def circle_area(r):
#     if type(r) != int:
#         return False
#     if r <= 0:
#         return False
#     else:
#         return round(math.pi*r**2, 2)
#
# print(circle_area(68))
#
# def max_multiple(divisor, bound):
#     return bound - (bound%divisor)
#
# print(max_multiple(2, 7))
#
# def find_missing_number(numbers):
#     n = len(numbers)
#     total = (n + 1)*(n + 2)/2
#     sum_of_A = sum(numbers)
#     return total - sum_of_A
#
# print(find_missing_number([2, 3, 4]))
#
# def solution(items, index, default_value):
#     if abs(index) > len(items):
#         return default_value
#     else:
#         return items[index]
#
#
# data = ['a', 'b', 'c']
# print(solution(data, 1, 'd'))
#
# def order_weight(strng):
#     return ' '.join(sorted(sorted(strng.split(' ')), key=lambda x: sum(int(c) for c in x)))
#
# print(order_weight('56 65 74 100 99 68 86 180 90'))
#
# def first_non_repeating_letter(string):
#     low_str = []
#     for i in string:
#         low_str.append(i.lower())
#     for i in string:
#         if low_str.count(i.lower()) == 1:
#             return i
#     return ''
#
# print(first_non_repeating_letter('stress'))
#
#
# def max_sequence(arr):
#     if len(arr) < 1:
#         return 0
#     max_so_far = arr[0]
#     max_ending_here = 0
#
#     for i in range(0, len(arr)):
#         max_ending_here = max_ending_here + arr[i]
#         if max_ending_here < 0:
#             max_ending_here = 0
#
#         elif (max_so_far < max_ending_here):
#             max_so_far = max_ending_here
#
#     return max_so_far if max_so_far > 0 else 0
#
# print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
#
# def who_is_next(names, r):
#     while r > len(names):
#         r = (r - (len(names)-1)) // 2
#     return names[r-1]
#
# print(who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951))
#
# def rot13(message):
#     new = []
#     answer = ''
#     for i in message:
#         if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVYWXZ':
#             if 96 < ord(i) <= 122:
#                 if ord(i)+13 > 122:
#                     new.append(ord(i)-13)
#                 else:
#                     new.append(ord(i)+13)
#             elif 65 <= ord(i) <= 90:
#                 if ord(i)+13>90:
#                     new.append(ord(i)-13)
#                 else:
#                     new.append(ord(i)+13)
#             else:
#                 new.append(ord(i)+13)
#         else:
#             new.append(i)
#     for n in new:
#         if type(n) == int:
#             answer+=chr(n)
#         else:
#             answer+=n
#     return answer
#
# print(rot13('Test!'))
#
# def find_longest(arr):
#     for i in arr:
#         if len(str(i)) == len(str(sorted(arr)[-1])):
#             return i
#
# print(find_longest([1, 10, 100]))
#
# def bingo(ticket, win):
#     return 'Winner!' if sum(chr(n) in s for s, n in ticket) >= win else 'Loser!'
#
# print(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 2))
#
# class Omnibool:
#     def __eq__(self, _):
#         return True
#
# omnibool = Omnibool()
#
# def score_throws(radii):
#     if len(radii) < 1:
#         return 'Empty list'
#     total = 0
#     hundo = []
#     for i in radii:
#         if i > 10:
#             pass
#         if 5 <= i <= 10:
#             total += 5
#         if i < 5:
#             total += 10
#             hundo.append(1)
#     if len(hundo) == len(radii):
#         return (total+100)
#     else:
#         return total
#
# print(score_throws([1, 5, 11]))
#
# def reverse_alternate(string):
#     return " ".join(y[::-1] if x%2 else y for x,y in enumerate(string.split()))
#
# print(reverse_alternate('this is a dumb problem'))
#
# def string_transformer(s):
#     s = s.split(' ')
#     answer = []
#     for i in s[::-1]:
#         answer.append(i.swapcase())
#     return ' '.join(answer)
#
# print(string_transformer('Example Input'))
#
# def what_century(year):
#     n = (int(year) - 1) // 100 + 1
#     return str(n) + ("th" if n < 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))
#
# print(what_century('2001'))
#
# def compute_sum(n):
#     return sum(int(c) for i in range(1, n+1) for c in str(i))
#
# print(compute_sum(12))
#
# def grabscrab(word, possible_words):
#     answer = []
#     for i in possible_words:
#         if sorted(i) == sorted(word):
#             answer.append(i)
#     return answer
#
# print(grabscrab("ainstuomn", ["mountains", "hills", "mesa"]))
#
# N = ['zero','one','two','three','four','five','six','seven','eight','nine']
#
# def average_string(s):
#     try:
#         return N[sum(N.index(w) for w in s.split()) // len(s.split())]
#     except (ZeroDivisionError, ValueError):
#         return 'n/a'
#
#
# print(average_string('one two three four five'))
#
# def what_time_is_it(angle):
#
#     hr = int(angle // 30)
#     mn = int((angle % 30) * 2)
#     if hr == 0:
#         hr = 12
#     return '{:02d}:{:02d}'.format(hr, mn)
#
# print(what_time_is_it(32))
#
# def create_message(s):
#     answer = []
#     for i in s:
#         if len(i) > 0:
#             answer.append(i)
#         else:
#             return ' '.join(answer)
#
#
# print(create_message("Hello")("World!")("how")("are")("you?")())
#
# def count_deaf_rats(town):
#     counter = 0
#     town = town.replace(' ', '')
#     for i in town[::2]:
#         if i == 'O':
#             counter += 1
#         else:
#             pass
#     return counter
#
# print(count_deaf_rats('~O~O~O~O P'))
# print(count_deaf_rats("P O~ O~ ~O O~"))
# print(count_deaf_rats("~O~O~O~OP~O~OO~"))
#
# def compare_attack_types(first_type, second_type):
#     if first_type == second_type:
#         return 0.5
#     if first_type == "fire":
#         if second_type == "grass":
#             return 2
#         if second_type == "water":
#             return 0.5
#     if first_type == "grass":
#         if second_type == "fire":
#             return 0.5
#         if second_type == "water":
#             return 2
#     if first_type == "electric":
#         if second_type == "water":
#             return 2
#     if first_type == "water":
#         if second_type == "fire":
#             return 2
#         if second_type == "grass":
#             return 0.5
#         if second_type == 'electric':
#             return 0.5
#
#     return 1
#
# def calculate_damage(own_type, opponent_type, attack, defense):
#     return 50 * (attack / defense) * compare_attack_types(own_type, opponent_type)
#
# print(calculate_damage("fire", "water", 100, 100))
#
# def sortme(words):
#     return sorted(words, key=str.lower)
#
# print(sortme(["Hello", "there", "I'm", "fine"]))
#
# from ipaddress import ip_address
#
# def ips_between(start, end):
#     return int(ip_address(end)) - int(ip_address(start))
#
# print(ips_between("10.0.0.0", "10.0.0.50"))
#
# def arrange(s):
#     t = []
#     left, right = 0, len(s)-1
#     for i in range(len(s)):
#         if ((i+1)//2) % 2 == 0:
#             t.append(s[left])
#             left += 1
#         else:
#             t.append(s[right])
#             right -= 1
#     return t
#
# print(arrange([4, 3, 2]))
#
# def increment_string(strng):
#     head = strng.rstrip('0123456789')
#     tail = strng[len(head):]
#     if tail == "": return strng+"1"
#     return head + str(int(tail) + 1).zfill(len(tail))
#
# print(increment_string('foo'))
# print(increment_string('foo01'))
#
# def solution(n):
#     return (round(n*2))/2 if n != 4.25 else 4.5
#
# print(solution(4.25))
#
# def flatten(lst):
#     return sum(([i] if not isinstance(i, list) else i for i in lst), [])
#
# print(flatten([[1,2,3],["a","b","c"],[1,2,3]]))
#
# from math import factorial as fac
#
# def factorial(n):
#     if 0 > n > 12:
#         raise ValueError('A very specific bad thing happened.')
#     else:
#         return fac(n)
#
# print(factorial(-3))
#
# def row_weights(array):
#     return sum(array[::2]), sum(array[1::2])
#
# print(row_weights([50,60,70,80]))
#
# def growing_plant(upSpeed, downSpeed, desiredHeight):
#     day = 0
#     h = 0
#     while h <= desiredHeight:
#         h += upSpeed
#         day += 1
#         if h <  desiredHeight:
#             h -= downSpeed
#         else:
#             return day
#
# print(growing_plant(100, 90, 910))
#
# def shifted_diff(first, second):
#     return (second + second).find(first) if len(first) == len(second) else - 1
#
#
# print(shifted_diff('eecoff', 'coffee'))
#
# def isLeapYear(year):
#     return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0
#
# print(isLeapYear(2004))
#
# def show_sequence(n):
#     total = 0
#     answer = ''
#     if n == 0:
#         return '0=0'
#     elif n < 0:
#         return f'{n}<0'
#     else:
#         for i in range(0, n+1):
#             total += i
#             answer += f'{i}+'
#     answer = answer.rstrip(answer[-1])
#     answer += f' = {total}'
#     return answer
#
# print(show_sequence(6))
#
# def get_missing_element(seq):
#     for i in range(0, len(seq)+1):
#         if i not in seq:
#             return i
#
#
# print(get_missing_element([0,5,1,3,2,9,7,6,4]))
#
# def max_number(n):
#     return int(''.join(sorted(str(n), reverse=True)))
#
# print(max_number(213))
#
# def spam(number):
#     return 'hue'*number
#
# print(spam(1))
#
# def alphabetized(s):
#     return "".join(sorted(filter(str.isalpha, s), key=str.lower))
#
#
# print(alphabetized("The Holy Bible"))
#
# def shorter_reverse_longer(a, b):
#     if len(a) >= len(b):
#         return b+a[::-1]+b
#     else:
#         return a+b[::-1]+a
#
#
# print(shorter_reverse_longer('first', 'abcde'))
#
# def sort_the_inner_content(words):
#     answer = []
#     words = words.split(' ')
#     for word in words:
#         if len(word) <= 3:
#             answer.append(word)
#         else:
#             answer.append(word[0] + ''.join(sorted(word[1:-1], reverse=True)) + word[-1])
#     return ' '.join(answer)
#
# print(sort_the_inner_content('wait for me'))
#
# def service(score):
#     turn = sum(int(i) for i in score.split(":"))
#     condition = (turn%10 < 5) if turn < 40 else (turn%4 < 2)
#     return "first" if condition else "second"
#
# print(service('0:5'))
#
# def encrypt(text, rule):
#     return "".join(chr((ord(i)+rule)%256) for i in text)
#
# print(encrypt('a', 1))
#
# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)
#
# print(solution('helloWorld'))
#
# def camel_case(s):
#     return s.title().replace(" ", "")
#
#
# print(camel_case('test case'))
#
# def men_from_boys(arr):
#     evens = []
#     odds = []
#     arr = set(arr)
#     for i in arr:
#         if i%2 == 0:
#             if i not in evens:
#                 evens.append(i)
#         else:
#             if i not in odds:
#                 odds.append(i)
#     answer = sorted(evens)+sorted(odds, reverse=True)
#
#
#
# print(men_from_boys([7, 3, 14, 17]))
#
# def pattern(n):
#     answer = ''
#     if n >= 1:
#         for i in range(1, n+1):
#             answer += f'{str(i)*i}\n'
#     else:
#         return answer
#     return answer.rstrip(answer[-1])
#
# print(pattern(2))
#
# def solve(s):
#     counter = 0
#     for i in s:
#         if i.isupper():
#             counter += 1
#     if counter > len(s)/2:
#         return s.upper()
#     else:
#         return s.lower()
#
# print(solve('cODE'))
#
# def multiples(m, n):
#     return [(i*n) for i in range(1, m+1)]
#
# print(multiples(3, 5))
#
# def digitize(n):
#     return [int(i) for i in str(n)]
#
# print(digitize(123))
#
# def numericals(s):
#     dictio = {}
#     t = ""
#     for i in s:
#         dictio[i] = dictio.get(i,0) + 1
#         t += str(dictio[i])
#     return t
#
# print(numericals('aaaaaaaaaa'))
#
# import math
#
# def greatest_common_factor(seq):
#     return math.gcd(*seq)
#
# print(greatest_common_factor([46, 14, 20, 88]))
#
# def box_capacity(length, width, height):
#     return (length * 12 // 16) * (width * 12 // 16) * (height * 12 // 16)
#
# print(box_capacity(32, 64, 16))
#
# def over_the_road(address, n):
#     return n*2 - address+1
#
# print(over_the_road(7, 11))
#
# def f(n, m):
#     new = 0
#     for i in range(1, n+1):
#         new+=(i%m)
#     return (new)
#
# print(f(15, 10))
#
# def chess_board_cell_color(a, b):
#     return (ord(a[0]) + int(a[1])) % 2 == (ord(b[0]) + int(b[1])) % 2
#
# print(chess_board_cell_color('A1', 'C3'))
#
# def fizzbuzz(n):
#     answer = []
#     for i in range(1, n+1):
#         if i%3 == 0 and i%5 != 0:
#             answer.append('Fizz')
#         elif i%5 == 0 and i%3 != 0:
#             answer.append('Buzz')
#         elif i%5 == 0 and i%3 == 0:
#             answer.append('FizzBuzz')
#         else:
#             answer.append(i)
#
#     return answer
#
# print(fizzbuzz(3))
#
# def count_by(x, n):
#     return [i*x for i in range(1, n+1)]
#
# print(count_by(2, 5))
#
# def add_arrays(arr1, arr2):
#     if len(arr1) != len(arr2):
#         raise "Input arguments are not of equal length"
#     return [x + y for x, y in zip(arr1, arr2)]
#
#
# print(add_arrays([1, 2], [4, 5]))
#
# def solution(*args):
#     for i in args:
#         if args.count(i) > 1:
#             return True
#     return False
#
#
# print(solution(1, 2, 3, 1, 2))
#
# def longest_repetition(chars):
#     max_char, max_count = '', 0
#     char, count = '', 0
#     for c in chars:
#         if c != char:
#             count, char = 0, c
#         count += 1
#         if count > max_count:
#             max_char, max_count = char, count
#     return max_char, max_count
#
# print(longest_repetition('bbaaaabbbaaaa'))
#
# def is_int_array(a):
#     return isinstance(a, list) and all(isinstance(x, (int, float)) and x == int(x) for x in a)
#
# print(is_int_array([1.0, 2.0, 3.0001]))
#
# import re
# def camelize(s):
#     return "".join([w.capitalize() for w in re.split("\W|_", s)])
#
# print(camelize('java Script'))
#
# def divisors(n):
#     return sum(1 for i in range(1, n + 1) if n % i == 0)
#
# print(divisors(5))
#
# def valid_parentheses(string):
#     cnt = 0
#     for char in string:
#         if char == '(': cnt += 1
#         if char == ')': cnt -= 1
#         if cnt < 0: return False
#     return True if cnt == 0 else False
#
# print(valid_parentheses("hi())("))
#
# def zeros(n):
#     if(n < 0):
#         return -1
#     count = 0
#     while(n >= 5):
#         n //= 5
#         count += n
#     return count
#
# print(zeros(6))
#
# def solve(s):
#     t = None
#     while t != s:
#         t, s = s, s.replace('()', '')
#     return -1 if len(s) % 2 else sum(1 + (a == tuple(')(')) for a in zip(*[iter(s)] * 2))
#
# print(solve("())()))))()()("))
#
# def smallest(n):
#     answer = []
#     answer.append(sorted(str(n))[0])
#     if answer[0] <= n[0]:
#
#     return answer
#
# print(smallest(261235))
#
# opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
#
# def dirReduc(plan):
#     new_plan = []
#     for d in plan:
#         if new_plan and new_plan[-1] == opposite[d]:
#             new_plan.pop()
#         else:
#             new_plan.append(d)
#     return new_plan
#
# def sequence_sum(begin_number, end_number, step):
#     return sum(i for i in range(begin_number, end_number+1, step))
#
# print(sequence_sum(1, 5, 1))
#
# def multiplication_table(size):
#     return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]
#
# print(multiplication_table(3))
#
# def dup(arry):
#     news = []
#     for w in arry:
#         temp = []
#         for i,t in enumerate(w):
#             if t not in temp or t != temp[-1]:
#                 temp.append(t)
#         news.append("".join(temp))
#     return news
#
# print(dup(["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]))
#
# def pofi(n):
#     return ['1','i','-1','-i'][n%4]
#
# print(pofi(3))
#
# from math import factorial as fact
#
# def sum_arrangements(n):
#     s = str(n)
#     perms = fact(len(s)-1)
#     coefAll = int('1'*len(s))
#     return coefAll*perms*sum(map(int,s))
#
# print(sum_arrangements(98))
#
# def content_weight(bottle_weight, scale):
#     number1 = []
#     for i in scale:
#         if i.isdigit():
#             number1.append(i)
#     if 'larger' in scale:
#         divisor = int(''.join(number1))
#         return divisor*(bottle_weight/(divisor+1))
#     else:
#         divisor = int(''.join(number1))
#         return (bottle_weight/(divisor+1))
#
# print(content_weight(120, '2 times smaller'))
#
# def words_to_marks(s):
#
#     return sum((ord(i)-96) for i in s)
#
# print(words_to_marks('attitude'))
#
# def counting(arr):
#     answer = {}
#     for i in arr:
#         answer[i] = arr.count(i)
#     return answer
#
# print(counting(['james', 'james', 'john']))
#
# def remove_duplicate_words(s):
#     answer = []
#     s = s.split(' ')
#     for i in s:
#         if i in answer:
#             pass
#         else:
#             answer.append(i)
#     return ' '.join(answer)
#
#
# print(remove_duplicate_words('h a s d f s s'))
#
# def cube_odd(arr):
#     answer = []
#     new = []
#
#     for i in (arr):
#         if type(i) == int:
#             answer.append(i**3)
#         else:
#             return None
#     for x in answer:
#         if x%2!=0:
#             new.append(x)
#     return sum(new)
#
# print(cube_odd([1, 2, 3, 4]))
#
# def find_smallest(numbers, to_return):
#     return sorted(numbers)[0] if to_return == 'value' else numbers.index(sorted(numbers)[0])
#
# print(find_smallest([5, 4, 3, 2, 1], 'index'))
#
# def vampire_test(x, y):
#     return sorted(str(x * y)) == sorted(str(x) + str(y))
#
# print(vampire_test(204, 615))
#
# def repeats(arr):
#     answer = []
#     for i in arr:
#         if arr.count(i) == 1:
#             answer.append(i)
#     return sum(answer)
#
# print(repeats([4,5,7,5,4,8]))
#
# def is_narcissistic(i):
#     return sum(int(x)**len(str(i)) for x in str(i))
#
# print(is_narcissistic(1634))
#
# def div_con(x):
#     numbers = 0
#     s = 0
#     for i in x:
#         if type(i) == int:
#             numbers += i
#         else:
#             s += int(i)
#     return numbers-s
#
# print(div_con([9, 3, '7', '3']))
#
# def solve(a, b):
#     s = set(a) & set(b)
#     return ''.join(c for c in a+b if c not in s)
#
# print(solve('xyabb', 'xzca'))
#
# def is_sorted_and_how(arr):
#     if sorted(arr) == arr:
#         return 'yes, ascending'
#     if sorted(arr, reverse=True) == arr:
#         return 'yes, descending'
#     else:
#         return 'no'
#
# print(is_sorted_and_how([1, 2]))
#
# def square_digits(num):
#     answer = []
#     for i in str(num):
#         answer.append(str(int(i)**2))
#     return int(''.join(answer))
#
# print(square_digits(91119))
#
# def solution(arr, n):
#     return [i*n for i in arr]
#
# print(solution([1, 2, 3], 2))
#
# def halving_sum(n):
#     s=0
#     while n:
#         s+=n ; n>>=1
#     return s
#
# print(halving_sum(25))
#
# def filtering_string(string):
#     answer = ''
#     for i in string:
#         if i.isdigit():
#             answer+=(i)
#     return int(answer)
#
# print(filtering_string('a1b2c3'))
#
# def largest(n, xs):
#     xs = sorted(xs)
#     return xs[-n:]
#
# print(largest(3,[5,1,5,2,3,1,2,3,5]))
#
# def my_languages(results):
#     answer = []
#     for i in sorted(results, key=results.get, reverse=True):
#         if results[i] >= 60:
#             answer.append(i)
#     return answer
#
# print(my_languages({"Java": 10, "Ruby": 80, "Python": 65}))
#
# import math
#
# def strong_num(number):
#     return "STRONG!!!!" if sum(math.factorial(int(i)) for i in str(number)) == number else "Not Strong !!"
#
# print(strong_num(145))
#
# def find_screen_height(width, ratio):
#     ratio = ratio.split(':')
#     answer = width*(int(ratio[-1])/(int(ratio[0])))
#     return f'{width}x{int(answer)}'
#
# print(find_screen_height(1024, '4:3'))
#
# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
#
# print(accum('RqaEzty'))
#
# import re
#
# def sum_of_integers_in_string(s):
#     return sum(int(x) for x in re.findall(r"(\d+)", s))
#
# print(sum_of_integers_in_string("12.4"))
#
# def in_array(array1, array2):
#     res = []
#     for a1 in array1:
#         for a2 in array2:
#             if a1 in a2 and not a1 in res:
#                 res.append(a1)
#     res.sort()
#     return res
#
# print(in_array(["arp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]))
#
# def append_arrays(seq1, seq2):
#     for i in seq2:
#         seq1.append(i)
#     return seq1
#
# print(append_arrays([1,2],[3,4]))
#
# def get_sum(a, b):
#     return sum(range(min(a, b), max(a, b) + 1))
#
# print(get_sum(1, 2))
#
# def squares(x, n):
#     return [x**(2**i) for i in range(n)]
#
# print(squares(2, 5))
#
# def even_or_odd(s):
#     even = 0
#     odd = 0
#     for i in s:
#         if int(i)%2==0:
#             even += int(i)
#         else:
#             odd += int(i)
#
#     if even == odd:
#         return 'Even and Odd are the same'
#     if even > odd:
#         return 'Even is greater than Odd'
#     else:
#         return 'Odd is greater than Even'
#
# print(even_or_odd('1234'))
#
#
# import re
#
# powers = {
#     'w': -4, 'p': -3, 'b': -2, 's': -1,
#     'm': +4, 'q': +3, 'd': +2, 'z': +1,
# }
#
#
# def alphabet_war(fight):
#     fight = re.sub('.(?=\*)|(?<=\*).', '', fight)
#     result = sum(powers.get(c, 0) for c in fight)
#     if result < 0:
#         return 'Left side wins!'
#     elif result > 0:
#         return 'Right side wins!'
#     else:
#         return "Let's fight again!"
#
#
# print(alphabet_war("zz*zzs"))
#
# def is_merge(s, part1, part2):
#     if not part1:
#         return s == part2
#     if not part2:
#         return s == part1
#     if not s:
#         return part1 + part2 == ''
#     if s[0] == part1[0] and is_merge(s[1:], part1[1:], part2):
#         return True
#     if s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]):
#         return True
#     return False
#
# print(is_merge('codewars', 'code', 'wars'))
# print(is_merge('codewars', 'cdw', 'oears'))
# print(is_merge('codewars', 'cod', 'wars'))
#
# from math import ceil
#
# def get_participants(h):
#     return int(ceil(0.5 + (0.25 + 2 * h) ** 0.5))
#
# print(get_participants(7))
#
# def count_adjacent_pairs(st):
#     words = st.lower().split(' ')
#     currentWord = None
#     count = 0
#     for i, word in enumerate(words):
#         if i+1 < len(words):
#             if word == words[i+1]:
#                 if word != currentWord:
#                     currentWord = word
#                     count += 1
#             else:
#                 currentWord = None
#
#     return count
#
# print(count_adjacent_pairs('banana banana banana terracotta banana terracotta terracotta pie!'))
#
# def sum_square_even_root_odd(nums):
#     counter = 0
#     for i in nums:
#         if i%2 == 0:
#             counter+=(i**2)
#         else:
#             counter+=(math.sqrt(i))
#     return round(counter, 2)
#
# print(sum_square_even_root_odd([4,5,7,8,1,2,3,0]))
# import re
#
# def textin(txt):
#     return re.sub(r'(two|too|to)', '2', txt, flags=re.I)
#
# print(textin('I love to text'))
#
# def spoonerize(words):
#     words = words.split(' ')
#     return f'{words[1][0]}{words[0][1:]} {words[0][0]}{words[1][1:]}'
#
# print(spoonerize('nit picking'))
#
# def create_array_of_tiers(n):
#     answer = []
#     for i in range(0,len(str(n))):
#         answer.append(str(n)[0:i+1])
#     return answer
#
# # print(create_array_of_tiers(420))
#
# def db_sort(arr):
#     return sorted(arr, key=lambda x: (isinstance(x,str),x))
#
# print(db_sort(['come', 'on', 110, '2500', 10, '!', 7, 15, 5, 6, 6]))
#
# def build_palindrome(s):
#     n = 0
#     while s[n:] != s[n:][::-1]: n += 1
#     return s + s[:n][::-1]
#
# print(build_palindrome("abcdc"))
#
# def unlock(message):
#     return message.lower().translate(message.maketrans("abcdefghijklmnopqrstuvwxyz","22233344455566677778889999"))
#
# print(unlock('Nokia'))
#
# def center(strng, width, fill=' '):
#     d = max(width - len(strng), 0)
#     return fill * ((d + 1) // 2) + strng + fill * (d // 2)
#
# print(center('a', 3))
#
# def split_in_parts(s, n):
#     return ' '.join([s[i:i+n] for i in range(0, len(s), n)])
#
# print(split_in_parts('supercalifragilisticexpialidocious', 3))
#
# def sum_ppg(player_one, player_two):
#     return player_one['ppg'] + player_two['ppg']
#
# print(sum_ppg({ 'team': '76ers', 'ppg': 11.2 }, { 'team': 'bulls', 'ppg': 20.2 }))
#
# def consecutive(arr):
#     if len(arr) > 1:
#         return (max(arr)-min(arr)+1-len(arr))
#     else:
#         return 0
#
# print(consecutive([4, 8, 6]))
#
# def is_lucky(n):
#     answer = []
#     for i in str(n):
#         answer.append(int(i))
#     if sum(answer) == 0 or sum(answer)%9 == 0:
#         return True
#     else:
#         return False
#
# print(is_lucky(1892377))
#
# def fill_gaps(timesheet):
#     result = timesheet[:]
#     v, i = None, None
#     for j, w in enumerate(timesheet):
#         if w is not None:
#             if w==v:
#                 for k in range(i+1, j):
#                     result[k] = v
#             else:
#                 v = w
#             i = j
#     return result
#
#
# print(fill_gaps([1, None, None, 1]))
# GIFTS = {
#     1: 'Toy Soldier',
#     2: 'Wooden Train',
#     4: 'Hoop',
#     8: 'Chess Board',
#     16: 'Horse',
#     32: 'Teddy',
#     64: 'Lego',
#     128: 'Football',
#     256: 'Doll',
#     512: "Rubik's Cube"
# }
#
# def gifts(number):
#     return sorted(v for k, v in GIFTS.items() if k & number)
#
# print(gifts(22))
# import re
# def replace_dashes_as_one(s):
#     return (re.sub(r"[\w\-]*(.\-)\1+[\w\-]*", "", s))
#
#
# print(replace_dashes_as_one("a---b- - -c"))
#
# def abundant_number(num):
#     return True if sum(i for i in range(1, num) if num%i==0) > num else False
#
# print(abundant_number(18))
#
# from itertools import combinations
#
# def digits(num):
#     return list(map(sum, combinations(map(int,str(num)),2)))
#
#
# print(digits(156))
#
# def closest_multiple_10(i):
#     if i%10 < 5:
#         return i-(i%10)
#     else:
#         return i+(10-(i%10))
#
# print(closest_multiple_10(22))
# print(closest_multiple_10(26))
#
# def letter_pattern(words):
#     return ''.join(e[0] if len(set(e)) == 1 else '*' for e in zip(*words))
#
# print(letter_pattern(['general', 'admiral', 'piglets', 'secrets']))
#
# def can_jump(arr):
#     if arr[0] == 0 or len(arr) == 1:
#         return False
#
#     if arr[0] >= len(arr):
#         return True
#
#     for jump in range(1, arr[0] +1):
#         if can_jump(arr[jump:]):
#             return True
#
#     return False
#
#
# print(can_jump([2,0,1,5,0,0,3,0,0,3,1,0]))
#
# def split_odd_and_even(n):
#
#     import re
#     return [int(i) for i in re.findall(r"[2468]+|[13579]+", str(n))]
#
#
# print(split_odd_and_even(135246))
#
# def read_zalgo(zalgotext):
#     answer = []
#     for i in zalgotext:
#         if i.isascii() == True:
#             answer.append(i)
#     return ''.join(answer)
#
# print(read_zalgo("H̗̪͇͓̙͎̣̄ͬa͚̯̦͉̖̥v͆ͩ̃͆̓̐ͥe̟͎͖͕͍̎ ̰͚̩̟͕̰͊̽̍ͯ̌͊ā̖̪͉͍̥͙̿ͩ̃ͅ ̬̥͎͑̿ͧg̰̳̺͔̦͉ͫ̀̐̓̐r̝̫̱̘̰͐͋ͯͭͭͭ͆e͙͕̖̗͙̰͌ͭä͓͚̝͓́̌͑ͪ͊ṱͥ ̱ͣd͎͔͎͇̫̪̘̃͐̇à͕̮̈͋ͪy̼̳̱ͮ!̳̥̰̭͇̔ͮ̽̓"))
# import re
#
# def initialize_names(name):
#     return re.sub(' (.).*?(?= )', r' \1.', name)
#
# print(initialize_names('Lois Mary Lane'))
#
# def encode(s):
#     answer = []
#     for i in s:
#         if i.isalpha() == True:
#             answer.append(str(ord(i.lower())-96))
#         else:
#             answer.append(str(i))
#     return ''.join(answer)
#
# print(encode('abc'))
#
# def test_it(a, b):
#     a = sum( [int(x) for x in str(a)] )
#     b = sum( [int(x) for x in str(b)] )
#     return a * b
#
# print(test_it(0, 1))
# print(test_it(1, 2))
# print(test_it(5, 6))
# print(test_it(10, 10))
# print(test_it(200, 200))
# print(test_it(12, 34))
#
# def simplify(s):
#     d, r, c = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}, {(0, 0): ""}, (0, 0)
#     for z in s:
#         x, y = d[z]
#         nc = (c[0] + x, c[1] + y)
#         r[nc] = r[nc] if nc in r and r[c].startswith(r[nc]) else r[c] + z
#         c = nc
#     return r[c]
#
# print(simplify('<>>'))
#
# def motif_locator(sequence, motif):
#     res, i = [], 0
#     while True:
#         i = sequence.find(motif, i) + 1
#         if not i: return res
#         res.append(i)
#
# print(motif_locator("ACGTTACAACGTTAG", "ACGT"))
#
# def no_space(x):
#     return x.replace(' ', '')
#
# print(no_space('8aaaaa dddd r     '))
#
# import re
# def initialize_names(name):
#     return re.sub(' (.).*?(?= )', r' \1.', name)
#
# print(initialize_names('Lois Mary Lane'))
#
# def filter_even_length_words(words):
#     return [i for i in words if len(i)%2==0]
#
# print(filter_even_length_words(["Hello", "World"]))
# import re
# def solve(s):
#     return max(map(int, re.findall(r'(\d+)', s)))
#
# print(solve('2ti9iei7qhr5'))
#
# def cube_sum(n, m):
#     if n>m:
#         return sum(i**3 for i in range(m+1, n+1))
#     if m>n:
#         return sum(i**3 for i in range(n+1, m+1))
#     else:
#         return 0
#
#
# print(cube_sum(5, 0))
#
# def candies(s):
#     counter = 0
#     s = sorted(s)
#     if len(s) > 1:
#         for i in s:
#             counter+=(s[-1]-i)
#         return counter
#     else:
#         return -1
#
# print(candies([5, 8, 6, 4]))
#
# def duplicate_count(text):
#     count = 0
#     for c in set(text.lower()):
#         if text.lower().count(c) > 1:
#             count += 1
#     return count
#
# print(duplicate_count("abBcdeaa"))
#
# def encode(message):
#     return message.translate(str.maketrans('GgaADdeERryYPpoOLluUKkiI', 'AagGEedDYyrROopPUulLIikK'))
#
# print(encode('ABCDabcd'))
#
# def magical_well(a, b, n):
#     answer = 0
#     while n > 0:
#         answer+=(a*b)
#         n = n-1
#         a = a+1
#         b = b+1
#     return answer
#
# print(magical_well(1, 2, 2))
#
# def unusual_sort(array):
#     return sorted(array, key=lambda item: (str(item).isdigit(), str(item), isinstance(item, str)))
#
# print(unusual_sort(['0', '9', '8', '1', '7', '2', '6', '3', '5', '4']))
#
# def longest_palindrome(s):
#     longest = 0
#     for left in range(len(s)):
#         for right in range(len(s), left, -1):
#             if s[left:right] in (s[left:right])[::-1]:
#                 longest = max(right-left, longest)
#                 break
#     return longest
#
# print(longest_palindrome('aab'))
#
# def build_or_buy(hand):
#     d = {'bw': 'road', 'bwsg': 'settlement', 'ooogg': 'city', 'osg': 'development'}
#     res = []
#     for r, build in d.items():
#         if all(hand.count(i) >= r.count(i) for i in set(r)):
#             res.append(build)
#     return res
#
# print(build_or_buy('bwoo'))
#
# import re
# def is_vowel(s):
#     return bool(re.fullmatch(r'[aeiou]', s, re.I))
#
# print(is_vowel('a'))
#
# def calculate(s):
#     answer = []
#     s = s.split(' ')
#     for i in s:
#         if i.isdigit():
#             answer.append(i)
#     return int(answer[0])-int(answer[1]) if 'loses' in s else int(answer[0])+int(answer[1])
#
#
# print(calculate("Panda has 48 apples and loses 4"))
#
# def zebulans_nightmare(function):
#     answer = []
#     function = function.split('_')
#     for i in function:
#         if function.index(i) > 0:
#             answer.append(i.title())
#         else:
#             answer.append(i)
#     return ''.join(answer)
#
# print(zebulans_nightmare('convert_to_uppercase'))
#
# def house_of_cats(legs):
#     number = legs//2
#     if number%2==0:
#         return [i for i in range(0, number+1, 2)]
#     else:
#         return [i for i in range(1, number+1, 2)]
#
#
# print(house_of_cats(8))
#
# def solution(st, limit):
#     return st[:limit]+'...' if len(st)>limit else st
#
# print(solution('Testing String',8))
#
# def cup_and_balls(b, arr):
#     for switch in arr:
#         if b in switch:
#             b = sum(switch) - b
#     return b
#
# print(cup_and_balls(2,[[1,3],[1,2],[2,1],[2,3]]))
#
# def unique_sum(lst):
#     return sum(set(lst)) if len(lst) > 0 else None
#
# print(unique_sum([1, 3, 8, 1, 8]))
#
# def solve(n):
#     if n%10: return -1
#     c, billet = 0, iter((500,200,100,50,20,10))
#     while n:
#         x, r = divmod(n, next(billet))
#         c, n = c+x, r
#     return c
#
# print(solve(770))
#
# def reverse_by_center(s):
#     n = len(s)//2
#     return s[-n:]+s[n:-n]+s[:n]
#
# print(reverse_by_center('agent'))
#
# def killer(suspect_info, dead):
#     for name, seen in suspect_info.items():
#         if set(dead) <= set(seen):
#             return name
#
# print(killer({'James': ['Jacob', 'Bill', 'Lucas'],
#               'Johnny': ['David', 'Kyle', 'Lucas'],
#               'Peter': ['Lucy', 'Kyle']}
#              , ['Lucas', 'Bill']))
#
# def find_employees_role(name):
#     name = name.split(' ')
#     if len(name) > 1:
#         for i in employees:
#             if i['first_name'] == name[0]:
#                 if i['last_name'] == name[1]:
#                     return i['role']
#     return 'Does not work here!'
#
# print(find_employees_role('Dipper Pines'))
#
# def cheapest_quote(n):
#     prices = [(40, 3.85), (20, 1.93), (10, 0.97), (5, 0.49), (1, 0.10)]
#     result = 0
#     for q, c in prices:
#         result += n // q * c
#         n = n % q
#     return round(result, 2)
#
# print(cheapest_quote(5))
#
# def reverser(s):
#     s = s.split(' ')
#     return ' '.join([i[::-1] for i in s])
#
# print(reverser('Hi mom'))
#
# def sum_of_a_beach(beach):
#     answer = []
#     counter = 0
#     words = ('sand', 'water', 'fish', 'sun')
#     for i in words:
#         answer.append(beach.count(i))
#     return sum(answer)
#
# print(sum_of_a_beach('sunsunsunsun'))
#
# def check_three_and_two(array):
#     return sum([array.count(x) for x in array]) == 13
#
# print(check_three_and_two(["a", "a", "a", "a", "a"]))
#
# def find_the_key(message, code):
#     diffs = "".join( str(c - ord(m) + 96) for c, m in zip(code, message) )
#     for size in range(1, len(code) +1):
#         key = diffs[:size]
#         if (key * len(code))[:len(code)] == diffs:
#             return int(key)
# print(find_the_key("nomoretears", [15, 17, 14, 17, 19, 7, 21, 7, 2, 20, 20]))
#
# def jumping(arr, n):
#     i = 0
#     while i < len(arr):
#         x = arr[i]
#         arr[i] += 1 if x < n else -1
#         i += x
#     return arr.count(n)
#
# print(jumping([0,3,0,1,-3],3))
#
# def freq_seq(s, sep):
#     return ''.join([str(s.count(i))+sep for i in s])[:-1]
#
# print(freq_seq('hello world', '-'))
#
# def nth_char(words):
#     return ''.join(w[i] for i,w in enumerate(words))
#
# print(nth_char(["yoda", "best", "has"]))
#
# def cog_RPM(l):
#     return (-1 + len(l) % 2 * 2) * l[0] / l[-1]
# print(cog_RPM([100, 75]))
#
# def lottery(s):
#     answer = []
#     for i in s:
#         if i.isdigit():
#             if i not in answer:
#                 answer.append(i)
#     return ''.join(answer) if len(answer) > 0 else 'One more run!'
#
# print(lottery("wQ8Hy0y5m5oshQPeRCkG"))
#
# def computer_to_phone(numbers):
#     return numbers.translate(str.maketrans('0789456123', '0123456789'))
#
# print(computer_to_phone("0789456123"))
#
# def sum_even_numbers(seq):
#     return sum(i for i in seq if i%2==0)
#
# print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#
# def initials(name):
#     names = name.split()
#     return '.'.join(x[0].upper() for x in names) + names[-1][1:]
#
# print(initials('barack hussein obama'))
#
# def zipvalidate(postcode):
#     return len(postcode) == 6 and postcode.isdigit() and postcode[0] not in "05789"
#
# print(zipvalidate('198328'))
#
# def typist(s):
#     up=False
#     t=len(s)
#     for c in s:
#         if c.isupper() and not up:
#             up=True
#             t+=1
#         elif c.islower() and up:
#             up=False
#             t+=1
#     return t
#
# print(typist('aa'))
#
# from itertools import product
#
# mapping = {
#     '0': '0',
#     '1': '1',
#     '2': 'ABC',
#     '3': 'DEF',
#     '4': 'GHI',
#     '5': 'JKL',
#     '6': 'MNO',
#     '7': 'PQRS',
#     '8': 'TUV',
#     '9': 'WXYZ',
# }
#
# def telephoneWords(digits):
#     digits = map(lambda x: mapping[x], digits)
#     return map(''.join, product(*digits))
#
# print(telephoneWords('0002'))
#
# from math import sin, radians
#
# def find_time_to_break(bearing_A, bearing_B):
#     a = radians(abs(bearing_A - bearing_B) / 2)
#     return 40 / (3 * sin(a)) if a else float("inf")
#
# print(find_time_to_break(0, 90))
#
# def passer_rating(attempts, yards, completions, touchdowns, interceptions):
#     a = (completions / attempts - .3) * 5
#     b = (yards / attempts - 3) * .25
#     c = (touchdowns / attempts) * 20
#     d = 2.375 - (interceptions / attempts * 25)
#     a, b, c, d = (max(0, min(x, 2.375)) for x in (a, b, c, d))
#     return round((a + b + c + d) / 6 * 100, 1)
#
# print(passer_rating(432, 3554, 291, 28, 2))
#
# def differences(l):
#     answer = []
#     for i, x in enumerate(l):
#         answer.append(i-x)
#     return answer
#
# print(differences([1, 2, 3]))
#
# def find_dup(arr):
#     answer = []
#     for i in arr:
#         if i in answer:
#             return i
#         else:
#             answer.append(i)
#
#
# print(find_dup([5, 4, 3, 2, 1, 1]))
#
# def flatten(*a):
#     r = []
#     for x in a:
#         if isinstance(x, list):
#             r.extend(flatten(*x))
#         else:
#             r.append(x)
#     return r
#
# print(flatten(1, [2, 3], 4, 5, [6, [7]]))
#
# def get_score(n):
#     return (n+1)*(25*n)
#
# print(get_score(1))
# print(get_score(2))
# print(get_score(3))
# print(get_score(4))
# print(get_score(5))
#
# def sum_of_digits(digits):
#     answer = []
#     for digit in digits:
#         if digit.isdigit():
#             answer.append((digit))
#
#     return ''.join(answer)
#
# print(sum_of_digits('3433'))
#
# def test(r):
#     d = {'h': 0, 'a': 0, 'l': 0}
#     for mark in r:
#         if mark >= 9:
#             d['h'] += 1
#         elif mark >= 7:
#             d['a'] += 1
#         else:
#             d['l'] += 1
#
#     if d['a'] + d['l'] == 0:
#         return [round(sum(r)/len(r), 3), d, 'They did well']
#     else:
#         return [round(sum(r)/len(r), 3), d]
#
# print(test([10, 9, 9, 10, 9, 10, 9]))
#
# def candies_to_buy(n):
#     xx = 1
#     for i in range(n):
#         x = xx
#         while xx % (i+1):
#             xx += x
#     return xx
#
# print(candies_to_buy(5))
#
# def ranks(a):
#     sortA = sorted(a, reverse=True)
#     return [sortA.index(s) + 1 for s in a]
#
# print(ranks(ranks([9,3,6,10])))
#
# def word_mesh(arr):
#     result = ""
#
#     for a, b in zip(arr, arr[1:]):
#         while not a.endswith(b):
#             b = b[:-1]
#         if not b:
#             return "failed to mesh"
#         result += b
#
#     return result
#
# print((word_mesh(["beacon", "condominium", "umbilical", "california"])))
#
# def missing_values(seq):
#     x = 0
#     y = 0
#     for i in seq:
#         if seq.count(i) == 1:
#             x = i
#         if seq.count(i) == 2:
#             y = i
#     return x * x * y
#
# print(missing_values([1, 1, 1, 2, 2, 3]))
#
# def seven_ate9(str_):
#     while "797" in str_:
#         str_ = str_.replace("797", "77")
#     return str_
#
# print(seven_ate9('797'))
#
# def infected(s):
#     population = len(s.replace('X', ''))
#     if population == 0:
#         return 0
#     s = s.split('X')
#     survivors = 0
#     for i in s:
#         if '1' not in i:
#             survivors += len(i)
#     return 100 - (survivors/population)*100
#
#
# print(infected("01000000X000X011X0X"))
#
# def string_task(s):
#     answer = ''
#     for i in s:
#         if i not in 'aeiouAEIOU':
#             answer += f'.{i.lower()}'
#     return answer
#
# print(string_task('Codewars'))
#
# def solve(s,a,b):
#     return s[:a]+s[a:b+1][::-1]+s[b+1:]
#
# print(solve('codewars', 1, 5))
#
# def get_larger_numbers(a, b):
#     return [i if i>=x else x for i,x in zip(a,b)]
#
# print(get_larger_numbers([13, 64, 15, 17, 88], [23, 14, 53, 17, 80]))
#
# def snail(column, day, night):
#     counter = 0
#     current = 0
#     while current < column:
#         current+=day
#         counter+=1
#         if current < column:
#             current-=night
#
#     return counter
#
# print(snail(10, 3, 1))
#
# def short_form(s):
#     return s[0]+''.join(x for x in s[1:-1] if x not in 'aeiouAEIOU')+s[-1]
#
# print(short_form('assault'))
#
# from math import pi
# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#         self.volume = 4*pi * self.radius**3 / 3
#         self.surface = 4*pi* self.radius**2
#     def get_radius(self):
#         return self.radius
#     def get_mass(self):
#         return self.mass
#     def get_volume(self):
#         return round(self.volume,5)
#     def get_surface_area(self):
#         return round(self.surface,5)
#     def get_density(self):
#         return round(self.mass/self.volume, 5)
#
# class Block(object):
#     def __init__(self, dimensions):
#         self.width = dimensions[0]
#         self.length = dimensions[1]
#         self.height = dimensions[2]
#         self.volume = self.width*self.length*self.height
#         self.surface_area = (2*self.length*self.height)+(2*self.length*self.width)+(2*self.width*self.height)
#
#     def get_width(self):
#         return self.width
#     def get_length(self):
#         return self.length
#     def get_height(self):
#         return self.height
#     def get_volume(self):
#         return self.volume
#     def get_surface_area(self):
#         return self.surface_area
#
# def shape_area(n):
#     return (n**2)+((n-1)**2)
#
# print(shape_area(3))
#
# def add(*args):
#     return sum((i+1)*v for i,v in enumerate(args))
#
# print(add(1, 2, 3))
#
# def duplicate_sandwich(arr):
#     start, end = [i for i, x in enumerate(arr) if arr.count(x) > 1]
#     return arr[start+1:end]
#
#
# print(duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8]))
#
# import re
#
# def testit(s):
#     return len(re.findall(r'w.*?o.*?r.*?d', s, re.I))
#
#
# print(testit("word"))
# print(testit("hello world"))
# print(testit("I love codewars."))
# print(testit("My cat waiting for a dog."))
# print(testit("We often read book, a word hidden in the book."))
# print(testit("When you in order to do something by a wrong way, your heart will missed somewhere."))
#
# def catch_sign_change(lst):
#     count = 0
#     for i in range(1,len(lst)):
#         if lst[i] < 0 and lst[i-1] >= 0:
#             count += 1
#         if lst[i] >= 0 and lst[i-1] < 0:
#             count += 1
#     return count
#
#
# print(catch_sign_change([1, -3, -4, 0, 5]))
#
# def close_to_zero(t):
#     return min(map(int, t.split()), key=lambda t: (abs(t), -t), default=0)
#
# print(close_to_zero('-1 50 -4 20 22 -7 10 -8'))
#
# def add(a, b):
#     s = ""
#     while a+b:
#         a,p = divmod(a,10)
#         b,q = divmod(b,10)
#         s = str(p+q)+s
#     return int(s or'0')
# print(add(2, 11))
#
# def word_needed(project_minutes, free_lances):
#     free_time = 0
#     for i in range(0, len(free_lances)):
#         free_time+=((free_lances[i][0]*60)+free_lances[i][1])
#
#     if project_minutes > free_time:
#         return f'I need to work {(project_minutes-free_time)//60}hour(s) and {(project_minutes-free_time)%60}minute(s)'
#     else:
#         return "Easy Money!"
#
# print(word_needed(60, [(0, 0)]))
#
# def stanton_measure(arr):
#     return arr.count(arr.count(1))
#
# print(stanton_measure([1, 4, 3, 2, 1, 2, 3, 2]))
#
# def kill_count(counselors, jason):
#     answer = []
#     for i in counselors:
#         if i[-1] < jason:
#             answer.append(i[0])
#
#     return answer
#
# print(kill_count([["Mike", 7],["Alysa", 3]], 7))
#
# def count_animals(sentence):
#     counter = 0
#     sentence = sentence.split(' ')
#     for i in sentence:
#         if i.isdigit():
#             counter+=int(i)
#
#     return counter
#
# print(count_animals("I see 3 zebras, 5 lions and 6 giraffes."))
#
# def build_palindrome(strng):
#     n = 0
#     while strng[n:] != strng[n:][::-1]: n += 1
#     return strng + strng[:n][::-1]
#
#
# print(build_palindrome('abcdc'))
#
# def solve(arr):
#     arr = sorted(arr, reverse=True)
#     res = []
#     while len(arr):
#         res.append(arr.pop(0))
#         if len(arr):
#             res.append(arr.pop())
#     return res
#
# print(solve([15, 11, 10, 7, 12]))
#
# def scoreboard(string):
#     scores = {'nil': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
#     return [scores[x] for x in string.split() if x in scores]
#
# print(scoreboard("The score is four nil"))
#
# def elevator_distance(arr):
#     answer = 0
#     for i, x in zip(arr, arr[1:]):
#         answer+=abs(i-x)
#
#     return answer
#
# print(elevator_distance([5, 2, 8]))
#
# def sort_reindeer(reindeer_names):
#     return sorted(reindeer_names, key=lambda x:x.split(' ')[-1])
#
# print(sort_reindeer([
#     "Dasher Tonoyan",
#     "Dancer Moore",
#     "Prancer Chua",
#     "Vixen Hall",
#     "Comet Karavani",
#     "Cupid Foroutan",
#     "Donder Jonker",
#     "Blitzen Claus"
# ]))
#
# def arr_check(arr):
#     return all(isinstance(el, list) for el in arr)
#
# print(arr_check([]))
#
# def borrow(s):
#     answer = ''
#     for i in s:
#         if ord(i.lower()) > 96:
#             answer += i.lower()
#     return answer
#
# print(borrow('WhaT! Fick! daMN?'))
#
# def between_extremes(numbers):
#     return max(numbers)-min(numbers)
#
# print(between_extremes([1, -1]))
#
# def count_numbers(n, x):
#     return len([j for j in range(1,n+1) if x%j==0 and x/j <= n])
#
# print(count_numbers(5, 5))
#
# def change_count(change):
#     money = {'penny' : 0.01, 'nickel' : 0.05, 'dime' : 0.10, 'quarter' : 0.25, 'dollar' : 1.00}
#     count = 0
#     for coin in change.split():
#         count += money[coin]
#     result = "%.2f" % count
#     return '$' + result
#
# print(change_count('quarter quarter'))
#
# def is_lucky(ticket):
#     if len(ticket) == 6 and ticket.isdigit():
#         t = list(map(int, ticket))
#         return sum(t[:3]) == sum(t[3:])
#     return False
#
# print(is_lucky('123321'))
#
# def highest_value(a, b):
#     total = 0
#     for i in a:
#         total+=ord(i)
#     for x in b:
#         total -=ord(x)
#
#     return a if total >= 0 else b
#
# # print(highest_value("AaBbCcXxYyZz0189", "KkLlMmNnOoPp4567"))
#
# def high(x):
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
#
# print(high('man i need a taxi up to ubud'))
#
# def prev_mult_of_three(n):
#     while n%3 != 0:
#         n//=10
#     return n or None
#
# print(prev_mult_of_three(25))
#
# def count_letter_and_numbers(s):
#     return sum(1 for i in s if i.isalpha() or i.isnumeric())
#
# print(count_letter_and_numbers('wicked312345..!'))
#
# def is_substitution_cipher(s1, s2):
#     a1 = [s1.count(i) for i in s1]
#     a2 = [s2.count(x) for x in s2]
#     return True if a1 == a2 else False
#
# print(is_substitution_cipher("aaxxaaz","aazzaay"))
#
# def mormons(starting_number, reach, target):
#     missions = 0
#     while starting_number < target:
#         starting_number += starting_number * reach
#         missions += 1
#     return missions
#
#
# print(mormons(40, 2, 121))
#
# def get_winner(b):
#     for c in set(b):
#         if b.count(c) * 2 > len(b):
#             return c
#
# print(get_winner(("A", "A", "A", "B", "B", "B")))
#
# def string_letter_count(s):
#     s = s.lower()
#     m = ''
#     for i in sorted(list(set(s))):
#         if i.islower():
#             m += str(s.count(i)) + i
#     return m
#
# print(string_letter_count(("The time you enjoy wasting is not wasted time.")))
#
# def delete_digit(n):
#     s = str(n)
#     return int(max(s[:i] + s[i+1:] for i in range(len(s))))
#
# print(delete_digit(548217))
#
# def tail_swaps(strings):
#     answer = [strings[0].split(':'), strings[1].split(':')]
#     return [answer[0][0]+':'+answer[1][1], answer[1][0]+':'+answer[0][1]]
#
# print(tail_swaps(['abc:123', 'cde:456']))
#
# def modified_sum(a, n):
#     return sum(i**n for i in a)-sum(a)
#
# print(modified_sum([1, 2, 3], 3))
# import math
# def fraction(a, b):
#     d = math.gcd(a, b)
#     return (a//d)+(b//d)
#
# print(fraction(90, 120))
#
# def how_many_times(annual_price, individual_price):
#     return math.ceil(annual_price/individual_price)
#
# print(how_many_times(80, 15))
#
# import statistics
# def median(arr):
#     return statistics.median(arr)
#
# print(median([1, 2, 3, 4]))
#
# def get_ages(a,b):
#     x = (a+b)/2
#     y = (a-b)/2
#     return None if a<0 or b<0 or x<0 or y<0 else (x,y)
#
# print(get_ages(24, 4))
#
# def age(x, y):
#     return (x * y) / (y - 1)
# print(age(6, 3))
#
# def determine_time(arr):
#     hours = 0
#     minutes = 0
#     seconds = 0
#     for i in arr:
#         for x in i.split(':'):
#             if i.split(':').index(x) == 0:
#                 hours += int(x)
#             if i.split(':').index(x) == 1:
#                 minutes += int(x)
#             if i.split(':').index(x) == 2:
#                 seconds += int(x)
#
#     return True if (hours + minutes/60 + seconds/3600) < 24 else False
#
# print(determine_time(["01:00:00", "02:30:00", "22:00:00"]))
# print(determine_time(["01:00:00", "02:30:00"]))
#
# def find_page_number(pages):
#     n, miss = 1, []
#     for i in pages:
#         if i!=n:
#             miss.append(i)
#         else:
#             n+=1
#     return miss
#
# print(find_page_number([1,2,10,3,4,5,8,6,7]))
#
# def discover_original_price(discounted_price, sale_percentage):
#     return round(discounted_price/(1-(sale_percentage)/100), 2)
#
# print(discover_original_price(75, 25))
# print(discover_original_price(458.2, 17.13))
#
# def makeParts(arr, csize):
#     return [arr[i: i + csize] for i in range(0, len(arr), csize)]
#
#
# print(makeParts([1, 2, 3, 4, 5], 2))
#
# def solve(n,k):
#     res = list(range(n))
#     for i in range(n):
#         res = res[:i] + res[i:][::-1]
#     return res.index(k)
#
# print(solve(20, 8))
#
# def who_took_the_car_key(message):
#     answer = ''
#     for i in message:
#         an_integer = int(i, 2)
#         ascii_character = chr(an_integer)
#         answer += ascii_character
#
#     return answer
#
# print(who_took_the_car_key(['01000001', '01101100', '01100101', '01111000', '01100001', '01101110',
#                             '01100100', '01100101', '01110010']))
#
# def mn_lcm(m, n):
#     if m > n:
#         l = [i for i in range(n,m)]
#     if n > m:
#         l = [i for i in range(m,n)]
#     lcm = 1
#     for i in l:
#         lcm = lcm*i//math.gcd(lcm, i)
#     return lcm
#
# print(mn_lcm(1, 5))
# print(mn_lcm(5, 1))
#
# def covfefe(s):
#     return s.replace("coverage","covfefe") if "coverage" in s else s+" covfefe"
#
# print(covfefe('nothing'))
# print(covfefe('coverage'))
# print(covfefe('coverage coverage'))
#
# def remember(s):
#     seen = set()
#     res = []
#     for i in s:
#         res.append(i) if i in seen and i not in res else seen.add(i)
#     return res
#
# print(remember('apPle'))
# print(remember('pippi'))
#
# def ferry_loading(length, loads):
#     n, (l, r) = 0, ([t for t, side in loads if side == s] for s in ['left', 'right'])
#     while l or r:
#         n += 1
#         loaded = 0
#         while l and loaded + l[0] <= length * 100:
#             loaded += l.pop(0)
#         l, r = r, l
#     return n
#
#
# print(ferry_loading(20, [(380, "left"), (720, "left"), (1340, "right"), (1040, "left")]))
#
# def first_dup(s):
#     for x in s:
#         if s.count(x) > 1:
#             return x
#     return None
#
#
# print(first_dup('tweet'))

# Python program showing

# abstract base class work
#
# def problem(w,c):
#     answer = ''
#     for i in range(len(w)):
#         if i%2 == 0:
#             if c == 'S':
#                 answer += w+' '
#             else:
#                 answer += w+'\n'
#         else:
#             if c == 'S':
#                 answer += w[::-1]+' '
#             else:
#                 answer += w[::-1]+'\n'
#     return answer
#
# print(problem('Hello', 'D'))
#
# import math
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def getArea(self):
#         return math.ceil(3.14159265*radius*radius)
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def getArea(self):
#         return math.ceil(width*height)
#
# class Square:
#     def __init__(self, width):
#         self.width = width
#
#     def getArea(self):
#         return math.ceil(width*width)
#
# def zeros(n):
#     i = 5
#     zeros = 0
#     while n>=i:
#         zeros += n//i
#         i *= 5
#     return zeros

def language(text):
    answer = ''
    for i in text:
        if i in 'aeiou':
            if i == answer[-1]:
                answer += i
            else:
                answer += 'av' + i
        else:
            answer += i

    return answer

print(language('coodinggaame'))

