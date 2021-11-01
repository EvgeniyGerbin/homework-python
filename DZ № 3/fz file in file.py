input_filename = "fizzbuzz.txt"
output_filename = "outfizzbuzz.txt"

file_fb_input = open(input_filename, "r")
file_fb_output = open(output_filename, "w")
for line in file_fb_input:
    fizz, buzz, c = line.split()
    fizz = int(fizz)
    buzz = int(buzz)
    c = int(c)

    for x in (range(1, c + 1)):
        if x % fizz == 0 and x % buzz == 0:
            file_fb_output.write(' FB ')
        elif x % fizz == 0:
            file_fb_output.write(" B ")
        elif x % buzz == 0:
            file_fb_output.write(" F ")
        else:
            file_fb_output.write(" " + str(x) + " ")
    file_fb_output.write("\n")

file_fb_input.close()
file_fb_output.close()
