import sys
import csv
from tabulate import tabulate


class Dataset():
    """A class handling the data set and the information about it."""
    def __init__(self):
        self.values = {}
        self.results_list = []
        self.user_selection = []
        self.output_list = []

    def __str__(self):
        """Returns the results of the calculations on the dataset in a clean formatted table."""
        if len(sys.argv) > 2:
            self.user_selection = [arg.lower().strip() for arg in sys.argv[2:]]
            if "*all" in self.user_selection:
                self.user_selection = self.values.keys()

        for key in self.user_selection:
            self.results_list.clear()
            try:
                self.results(self.values[key])
            except KeyError:
                sys.exit(f"{key} is not a header in the file.")
            self.output_list.append(f"\n{key.title()}:\n{tabulate(self.results_list, tablefmt="rst", colalign=("left",))}")
        return "".join(self.output_list)

    def openfile(self):
        """Opens file given in argv[1]. If headers are provided in argv[2] and beyond -> do each column calculation separately.
        If no column header is provided by the user, it will add all the data in a single list for calculation."""
        try:
            with open(sys.argv[1]) as file:
                if len(sys.argv) == 2:
                    self.values["Result"] = []
                    self.user_selection.append("Result")
                    reader = csv.reader(file)
                    for row in reader:
                        for i in row:
                            try:
                                self.values["Result"].append(float(i))
                            except (TypeError, ValueError):
                                pass
                else:
                    reader = csv.DictReader(file)
                    for row in reader:
                        for i in row:
                            try:
                                if i.lower() in self.values:
                                    self.values[i.lower()].append(float(row[i]))
                                else:
                                    self.values[i.lower()] = [float(row[i])]
                            except (ValueError, TypeError):
                                pass
        except FileNotFoundError:
            sys.exit("File not found. Input correct filepath")

    def get_data(self):
        """A method to ask the user for a list of numbers to use as data."""
        print("Type in your list, one number at a time. Type 'Quit' when you are done: ")
        self.values["Result"] = []
        self.user_selection.append("Result")
        while True:
            try:
                user_input = input().strip().lower()
                if user_input in ("q", "quit"):
                    break
                else:
                    self.values["Result"].append(float(user_input))
            except (ValueError, TypeError, KeyboardInterrupt):
                print("Only input numerical data")
                pass

    def results(self, a_list):
        """This method will compile all the calculation results into the results_list attribute."""
        self.results_list.append(["Range: ", f"{sorted(a_list)[-1] - (sorted(a_list)[0])}  |  Minimum:  {min(a_list)}  |  Maximum:  {max(a_list)}  |  Mid Range:  {mean([min(a_list), max(a_list)])}"])
        self.results_list.append(["Mean: ", mean(a_list)])
        self.results_list.append(["Median: ", median(a_list)])
        mode_results = mode(a_list)
        if mode_results[1] == 0:
            self.results_list.append(["Mode: ", "None"])
        else:
            self.results_list.append(["Mode: ", f"{', '.join(str(e) for e in mode_results[0])} | Occurrences: {mode_results[1]}"])
        self.results_list.append(["Variance: ", variance(a_list)])
        self.results_list.append(["Standard Deviation: ", standard_deviation(a_list)])
        self.results_list.append(["Left Quartile: ", left_quarter(a_list)])
        self.results_list.append(["Right Quartile: ", right_quarter(a_list)])
        self.results_list.append(["Interquartile Range: ", interquartile_range(a_list)])
        self.results_list.append(["Without Outliers: ", remove_outliers(a_list)])
        self.results_list.append(["Mean Abs. Dev.: ", mean_absolute_deviation(a_list)])
        self.results_list.append(["Z Score: ", z_score(a_list)])


def main():
    data = Dataset()
    if len(sys.argv) >= 2:
        data.openfile()
    else:
        data.get_data()
    for i in data.values:
        if len(data.values[i]) < 2:
            sys.exit("Not enough Data. Needs at least 2 numbers")
    print(data)


def mean(a_list, rnd=4):
    """Calculates the arithmetic mean in a list of numbers. Optional rnd for rounding digits."""
    return round(sum(a_list)/len(a_list), rnd)


def median(a_list):
    """Calculates the middle number in the list, or 50th percentile."""
    s_list = sorted(a_list)
    if len(s_list) % 2 == 1:
        return s_list[len(s_list) // 2]
    else:
        l_middle = s_list[(len(s_list) // 2) - 1]
        r_middle = s_list[(len(s_list) // 2)]
        return mean([l_middle, r_middle])


def left_quarter(a_list):
    """Calculates the first quartile, or 25th percentile."""
    s_list = sorted(a_list)
    left_half = s_list[:len(a_list) // 2]
    return median(left_half)


def right_quarter(a_list):
    """Calculates the third quartile, or 75th percentile."""
    s_list = sorted(a_list)
    if len(s_list) % 2 == 1:
        right_half = s_list[(len(a_list) // 2) + 1:]
    else:
        right_half = s_list[(len(a_list) // 2):]
    return median(right_half)


def remove_outliers(a_list):
    """Remove outliers in the dataset, that are farther away than 1.5 interquartile ranges from either Q1 or Q3."""
    s_list = sorted(a_list)
    cleaned_list = []
    q1 = left_quarter(a_list)
    q3 = right_quarter(a_list)
    iqr = interquartile_range(a_list)
    for n in s_list:
        if q1 - iqr * 1.5 < n < q3 + iqr * 1.5:
            cleaned_list.append(n)
    return cleaned_list


def interquartile_range(a_list):
    """Calculates the range between the first and the third quartiles."""
    return right_quarter(a_list) - left_quarter(a_list)


def mode(a_list):
    """Calculates the value that occurs the most often in the data list, and returning it as a tuple containing two values: the mode list, and the count of occurences."""
    max_count = 1
    mode_list = []
    for n in a_list:
        if not n in mode_list:
            if a_list.count(n) > max_count:
                mode_list.clear()
                mode_list.append(n)
                max_count = a_list.count(n)
            elif a_list.count(n) == max_count:
                mode_list.append(n)
    if max_count == 1:
        return "No mode", 0
    else:
        return mode_list, max_count


def variance(a_list, sample=False, rnd=4):
    """Calculates the spread of a data distribution, by returning the average squared distance between data points and the mean
    Optional rnd for rounding digits."""
    mean_val = mean(a_list)
    datapoint_minus_mean_sum = sum([((e - mean_val)**2) for e in a_list])
    if sample:
        return round(datapoint_minus_mean_sum/(len(a_list)-1), rnd)
    else:
        return round(datapoint_minus_mean_sum/len(a_list), rnd)


def standard_deviation(a_list, sample=False, rnd=4):
    """Calculates the spread of the data distribution, measuring the typical distance between the data points and the mean,
    by calculating the square root of variance. Optional rnd for rounding digits."""
    return round(variance(a_list, sample)**0.5, rnd)


def z_score(a_list):
    """For each data point in the list, calculates how many standard deviations they are away from above or below the mean."""
    z_mean = mean(a_list)
    z_dev = standard_deviation(a_list)
    if z_dev == 0:
        return None
    else:
        return ([round(((e - z_mean) / z_dev), 2) for e in a_list])


def mean_absolute_deviation(a_list, rnd=4):
    """Returns the average distance between each data point and the mean. Optional rnd for rounding digits."""
    listmean = mean(a_list)
    return round(sum([abs(e - listmean) for e in a_list]) / len(a_list), rnd)


if __name__ == "__main__":
    main()
