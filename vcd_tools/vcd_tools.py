from vcdvcd import VCDVCD
import questionary

def vcd_tools_fun():

    vcd_path = questionary.path(
    "Enter path to vcd file."
    ).ask()

    # Do the parsing.
    vcd = VCDVCD(vcd_path)

    # List all human readable signal names.
    #print(vcd.references_to_ids.keys())
    chc_lst = []
    for i,key in enumerate(vcd.references_to_ids.keys()):
        print(key)
        chc_lst.append(questionary.Choice(f"{key}",value=f"chc{i}",checked=False))

    options = questionary.checkbox('Select Options:', chc_lst).ask()

    sigs_lst = []
    for i,key in enumerate(vcd.references_to_ids.keys()):
        if chc_lst[i].value in options:
                print(key)
                sigs_lst.append(vcd[key])

    num_sigs = len(sigs_lst)

    # last time value
    last_time = 0
    for trc in range(num_sigs):
        last_time = sigs_lst[trc].tv[-1][0] if sigs_lst[trc].tv[-1][0] > last_time else last_time
    beat_cnt = 0
    for i in range(last_time):

        # AND all selected signals together
        beat_valid = True
        for trc in range(num_sigs):
            print(sigs_lst[trc][i])
            if sigs_lst[trc][i] == '0':
                beat_valid = False

        if beat_valid:
            beat_cnt += 1


    print(beat_cnt)

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


