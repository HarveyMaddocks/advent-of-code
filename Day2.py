def test_report(report: list) -> bool:
    first = report[0]
    last = report[-1]

    if first < last:
        sort_report = sorted(report)
    elif last < first:
        sort_report = sorted(report, reverse=True)
    else:
        return False

    if sort_report != report:
        return False

    diffs = [abs(j - i) for i, j in zip(report, report[1:])]
    if (max(diffs) > 3) or (min(diffs) < 1):
        return False

    return True


def test_report_dampener(report: list) -> bool:
    new_reports = [report[:i] + report[i + 1:] for i in range(len(report))]
    return any(test_report(i) for i in new_reports)


with open(r"Data/Day2.txt") as f:
    data = f.readlines()

data = [[int(j) for j in i.split()] for i in data]

safe_reports = []
unsafe_reports = []
for report in data:
    if test_report(report):
        safe_reports.append(report)
    else:
        unsafe_reports.append(report)

dampened_unsafes = [i for i in unsafe_reports if test_report_dampener(i)]

print(f"Original Safe Report: {len(safe_reports)}")
print(f"Dampened Safe Reports: {len(dampened_unsafes)}")
print(f"Total Safe Reports: {len(safe_reports + dampened_unsafes)}")