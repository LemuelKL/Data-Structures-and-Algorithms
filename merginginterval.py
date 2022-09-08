# {{6,8},{1,9},{2,4},{4,7}}
# {{1,9}}

intervals = [[6, 8], [1, 9], [2, 4], [4, 7]]


def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    print(intervals)
    merged = []
    for interval in intervals:
        print("Processing interval: ", interval)

        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

        print(merged)
    return merged


if __name__ == "__main__":
    print(merge(intervals))
