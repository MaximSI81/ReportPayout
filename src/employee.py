import argparse


class SalaryEmployees:

    def __init__(self, files: tuple):
        self.files = files

    def get_data_from_report(self):  # получаем данные из файлов csv
        data = []
        for f in self.files:
            with open(f) as file:
                column = file.readline().strip().split(",")
                for i in range(len(column)):
                    if column[i] in ("hourly_rate", "salary"):
                        column[i] = "rate"
                        break
                for string in file.readlines():
                    data.append({col: s for col, s in zip(column, string.strip().split(","))})
        return data

    def get_salary_report(self):  # создам отчет с выводом в консоль и записью данных в файл txt и json
        data_report = []
        report = {"department": {key["department"]: {"name": [], "hours": [], "rate": [], "payout": []} for key in
                                 self.get_data_from_report()}}
        for i in self.get_data_from_report():
            report["department"][i["department"]]["name"].append(i["name"])
            report["department"][i["department"]]["hours"].append(int(i["hours_worked"]))
            report["department"][i["department"]]["rate"].append(i["rate"])
            report["department"][i["department"]]["payout"].append(float(i["rate"]) * float(i["hours_worked"]))
        col_name = f'{"name":>19}{"hours":>27}{"rate":>10}{"payout":>11}'
        data_report.append(col_name)
        for i in sorted(report["department"]):
            depart_name = i
            data_report.append(depart_name)
            name = report["department"][i]["name"]
            hours = report["department"][i]["hours"]
            rate = report["department"][i]["rate"]
            payout = report["department"][i]["payout"]
            for n, h, r, p in zip(name, hours, rate, payout):
                data_employee = f'{"-" * 14} {n:>1}{" " * (26 - len(n))}{h}{r:>10}{"$":>8}{p}'
                data_report.append(data_employee)
            sum_hours = sum(hours)
            sum_payout = sum(payout)
            result_sum = f'{sum_hours:>44} {"$":>17}{sum_payout}'
            data_report.append(result_sum)
        with open("./reports_result/report_file.json", "w") as f:  # записываем json
            f.write(str(report).replace("'", '"'))
        with open("./reports_result/report_res.txt", "w") as f:  # записываем файл txt
            f.write("\n".join(data_report))
        with open("./reports_result/report_res.txt", 'r') as f:  # вывод в консоль
            print(f.read())
        return data_report

    def get_avg_rate_department(self):  # возможность добавления отчёта средней ставки
        print("возможность добавления отчёта средней ставки")
        pass


def main():
    parser = argparse.ArgumentParser(description="Отчет по заработной плате")
    parser.add_argument("file", nargs="+", help="файлы с данными")
    parser.add_argument("--report", choices=["payout", "avg_rate"], required=True)
    args = parser.parse_args()
    report_result = SalaryEmployees(args.file)
    args = parser.parse_args()
    if args.report == "payout":
        report_result.get_salary_report()
    elif args.report == "avg_rate":
        report_result.get_avg_rate_department()


if __name__ == "__main__":
    main()
