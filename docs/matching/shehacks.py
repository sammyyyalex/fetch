#not functional, but an attempt at the code
receivers = [
    {
        "name": "A",
        "needs_device": True,
        "type_of_device": ["laptop"],
        "latest_year_of_production": ["2015"],
    },
    {
        "name": "B",
        "needs_device": True,
        "type_of_device": ["laptop"],
        "latest_year_of_production": ["2016"],
    },
    {
        "name": "C",
        "needs_device": True,
        "type_of_device": ["phone"],
        "latest_year_of_production": ["2017"],
    },
    {
        "name": "D",
        "needs_device": True,
        "type_of_device": ["phone"],
        "latest_year_of_production": ["2018"],
    },
    {
        "name": "E",
        "needs_device": True,
        "type_of_device": ["tablet"],
        "latest_year_of_production": ["2019"],
    },
]

donors = [
    {
        "name": "10",
        "can_donate_device": True,
        "type_of_device": ["laptop"],
        "year_of_production": ["2015"],
    },
    {
        "name": "20",
        "can_donate_device": True,
        "type_of_device": ["laptop"],
        "year_of_production": ["2016"],
    },
    {
        "name": "30",
        "can_donate_device": True,
        "type_of_device": ["phone"],
        "year_of_production": ["2017"],
    },
    {
        "name": "40",
        "can_donate_device": True,
        "type_of_device": ["phone"],
        "year_of_production": ["2018"],
    },
    {
        "name": "50",
        "can_donate_device": True,
        "type_of_device": ["tablet"],
        "year_of_production": ["2019"],
    },
]

def is_matched_to(person):
    for r in receivers:
        if r["name"] == person:
            return m["matched_to"]

    for d in donors:
        if d["name"] == person:
            return d["matched_to"]

    return True


def is_matched(person):
    for r in receivers:
        if r["name"] == person:
            if r["matched_to"] != "":
                return True

    for d in donors:
        if d["name"] == person:
            if d["matched_to"] != "":
                return True

    return False


def device_preferred(person, candidate1, candidate2):
    for r in receivers:
        if r["name"] == person:
            for x in range(0, len(receivers)):
                if candidate1 == r["preferences"][x]:
                    return candidate1
                if candidate2 == r["preferences"][x]:
                    return candidate2

    for d in donors:
        if d["name"] == person:
            for x in range(0, len(receivers)):
                if candidate1 == d["preferences"][x]:
                    return candidate1
                if candidate2 == d["preferences"][x]:
                    return candidate2


def engage(sampleReceiver, sampleDonor):
    for r in receivers:
        if r["name"] == sampleReceiver:
            r["matched_to"] = sampleDonor
            r["needs_device"] = False

    for d in donors:
        if d["name"] == sampleDonor:
            d["matched_to"] = sampleReceiver
            d["is_free"] = False


def get_name_from_ranking(sampleDonor, rank):
    for r in receivers:
        if r["name"] == sampleDonor:
            return r["latest_year_of_production"][rank]


def main():
    while (True):
        numberOfPairs = len(receivers)
        good = 1
        for r in receivers:
            sampleReceiver = r["name"]
            if (r["needs_device"] == True) and (len(r["latest_year_of_production"]) != numberOfPairs):
                good += 1
                if good == numberOfPairs:
                    print("\n\n\nSuccess!")
                    return

            for x in range(0, numberOfPairs):
                if not is_matched(sampleReceiver):
                    if x not in r["matched_to"]:
                        r["matched_to"].append(x)

                        donor = get_name_from_ranking(sampleReceiver, x)

                        if is_matched(donor):
                            currentReceiver = is_matched_to(donor)

                            betterpartner = device_preferred(
                                donor, currentReceiver, sampleReceiver)

                            match(betterpartner, donor)

                        else:
                            match(sampleReceiver, donor)


def happyend():
    print("Resolution:\n")
    for r in receivers:
        sampleReceiver = r["name"]
        sampleDonor = r["matched_to"]

        print("{} <---> {}".format(sampleReceiver, sampleDonor))


main()
happyend()