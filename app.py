DATE_PARCEL = 7
FIRST_CHANGE_COUNT = 3
SECOND_CHANGE_COUNT = 5


def get_max_key_values(hash_map):
    # sort hash map based on its values in decreasing order (returns only names as keys)
    sorted_key_list = sorted(
        hash_map, key=lambda k: hash_map[k], reverse=True)
    # get our max value
    max_val = hash_map[sorted_key_list[0]]
    # create our list of best programmers with heighest change count
    max_key_values = [sorted_key_list[0]]

    # while there are more who have equal change count add them
    i = 1
    while hash_map[sorted_key_list[i]] == max_val:
        max_key_values.append(sorted_key_list[i])
        i += 1

    return max_key_values


with open("gitlog.txt", "r") as log:
    # we create our own eof variable which triggers if a line is None since python doesnt have one from what i know
    end_of_file = False
    while not end_of_file:
        # reset all programmers
        programmers = {}

        # read new lines until there is one from which we can get date and set it to previous line
        new_line = log.readline()
        while new_line == "\n":
            new_line = log.readline()
        prev_line = new_line

        # get new date which we set to current and previous date
        prev_date = curr_date = new_line.split()[0][:DATE_PARCEL]

        # while the dates match
        while curr_date == prev_date:
            curr_line = log.readline()

            # reaches EOF so break this loop print last month and break main loop
            if not curr_line:
                end_of_file = True
                break

            # if we find space as first character we know we reached the main line
            if curr_line[0] == " ":
                # from prev_line we will get date and name
                prev_line_arr = prev_line.split("|")
                # from curr_line we will get change count
                curr_line_arr = curr_line.split()
                curr_date = prev_line_arr[0][:DATE_PARCEL]
                name = prev_line_arr[1].strip("\n")
                change_count = int(curr_line_arr[FIRST_CHANGE_COUNT])

                # sometimes there isnt both additions and deletions so we have to check to not get out of bounds err
                if len(curr_line_arr) > SECOND_CHANGE_COUNT:
                    change_count += int(curr_line_arr[SECOND_CHANGE_COUNT])

                # we have to check if we need to create a new programmer and set his new count or just add to it
                if name in programmers:
                    programmers[name] += change_count
                else:
                    programmers[name] = change_count

            # shift the lines
            prev_line = curr_line

        # get all programmers with max change count
        best_programmers = get_max_key_values(programmers)

        #########################################################################
        # if there is only signle best programmer we could use
        # best_programmers = []
        # best_programmers.append(max(programmers, key=lambda k: programmers[k]))
        #########################################################################

        # print this for every programmer in our array
        for programmer in best_programmers:
            print(
                f"{prev_date}: {programmer} added or deleted {programmers[programmer]} lines.")
