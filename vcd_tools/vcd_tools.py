import questionary
from vcdvcd import VCDVCD
from pathlib import Path


def file_selector():

    print(" - up/down selects current file/folder, enter selects file\n")
    caller_folder = Path.cwd()
    cdir = Path(caller_folder).absolute()
    basedir = Path(caller_folder).absolute()
    updirs = 0
    while 1:
        # get list of files/folders in current directory
        cdir_files = cdir.iterdir()
        cdir_files_filt = []
        for f in cdir_files:
            if not f.is_file() or '.vcd' in f.name:
                cdir_files_filt.append(f)
        flst = ['.. <up a directory>']  # add option for up a directory
        flst.extend([ f"{f}" for f in cdir_files_filt])
        choice = questionary.select(
            "Navigate to and select file (*.vcd)",
            choices=flst).ask()  # returns value of selection
        if choice == flst[0]:
            cdir = cdir.parent
            if basedir > cdir:
                basedir = cdir
                updirs = updirs + 1
        else:
            choice_index = flst.index(choice)
            choice_path = cdir_files_filt[choice_index-1]
            if choice_path.is_file():
                file_path = choice_path
                break
            else:
                cdir = choice_path

    return file_path


def parse(vcdfile=None):

    # Do the parsing.
    vcd = VCDVCD(vcdfile)
    return vcd


def beat_counter(vcd):

    # List all human readable signal names.
    # print(vcd.references_to_ids.keys())
    chc_lst = []
    for i, key in enumerate(vcd.references_to_ids.keys()):
        print(key)
        chc_lst.append(questionary.Choice(f"{key}", value=f"chc{i}", checked=False))

    options = questionary.checkbox("Select Options:", chc_lst).ask()

    sigs_lst = []
    for i, key in enumerate(vcd.references_to_ids.keys()):
        if chc_lst[i].value in options:
            print(key)
            sigs_lst.append(vcd[key])

    num_sigs = len(sigs_lst)

    # last time value
    last_time = 0
    for trc in range(num_sigs):
        last_time = (
            sigs_lst[trc].tv[-1][0]
            if sigs_lst[trc].tv[-1][0] > last_time
            else last_time
        )
    beat_cnt = 0
    for i in range(last_time):
        # AND all selected signals together
        beat_valid = True
        for trc in range(num_sigs):
            print(sigs_lst[trc][i])
            if sigs_lst[trc][i] == "0":
                beat_valid = False

        if beat_valid:
            beat_cnt += 1

    print(beat_cnt)

    return True

    # # tv is a list of Time/Value delta pairs for this signal.
    # tv = signal.tv
    # assert(tv[0] == (0, 'x'))
    # assert(tv[1] == (2, '0'))
    # assert(tv[2] == (6, '1'))

    # # Random access value of the signal at a given time.
    # # Note how it works for times between deltas as well.
    # assert(signal[0] == 'x')
    # assert(signal[1] == 'x')
    # assert(signal[2] == '0')
    # assert(signal[3] == '0')

def find_binary_pattern(vcd,pattern_lst=None):

    # List all human readable signal names.
    chc_lst = []
    for i, key in enumerate(vcd.references_to_ids.keys()):
        print(key)
        chc_lst.append(questionary.Choice(f"{key}", value=f"chc{i}", checked=False))

    options = questionary.checkbox("Select signal:", chc_lst).ask()

    sigs_lst = []
    for i, key in enumerate(vcd.references_to_ids.keys()):
        if chc_lst[i].value in options:
            print(key)
            sigs_lst.append(vcd[key])

    num_sigs = len(sigs_lst)

    # last time value
    last_time = 0
    for trc in range(num_sigs):
        last_time = (
            sigs_lst[trc].tv[-1][0]
            if sigs_lst[trc].tv[-1][0] > last_time
            else last_time
        )

        width = int(sigs_lst[trc].size,10)
        print(f'Hunting for patterns {pattern_lst} in {sigs_lst[trc].references}')
        # create big binary string
        binstr_lst = []
        binstr_reversed_lst = []
        for i in range(last_time):
            binstr = f"{int(sigs_lst[trc][i],2):0{width}b}"
            binstr_lst.append(binstr)
            binstr_reversed_lst.append(binstr[::-1])

        binstr_full = "".join(binstr_lst)
        binstr_reversed_full = "".join(binstr_reversed_lst)

        for pattern in pattern_lst:

            if pattern in binstr_full:
                print(f"found {pattern}")
                print(binstr_full.split(pattern))
            if pattern in binstr_reversed_full:
                print(f"found {pattern} when each vcd entry is bit reversed")
                print(binstr_reversed_full.split(pattern))

        print(binstr_full)
        print(binstr_reversed_full)

    return True



