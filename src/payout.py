import argparse


class SalaryReport:

    def __init__(self, files: tuple):
        self.files = files

    def get_data_from_report(self):  # получаем данные из отчётов
        data = []
        for f in self.files:
            with open(f) as file:
                column = file.readline().strip().split(',')
                for i in range(len(column)):
                    if column[i] in ('hourly_rate', 'salary'):
                        column[i] = 'rate'
                        break
                for string in file.readlines():
                    data.append({col: s for col, s in zip(column, string.strip().split(','))})
        return data

    def get_salary_report(self):
        report = {'department': {key['department']: {'name': [], 'hours': [], 'rate': [], 'payout': []} for key in
                                 self.get_data_from_report()}}
        for i in self.get_data_from_report():
            report['department'][i['department']]['name'].append(i['name'])
            report['department'][i['department']]['hours'].append(int(i['hours_worked']))
            report['department'][i['department']]['rate'].append(i['rate'])
            report['department'][i['department']]['payout'].append(float(i['rate']) * float(i['hours_worked']))
        with open(f'report.txt', 'a', encoding='utf-8') as file:
            self.number_report += 1
            col_name = f"{'name':>19}{'hours':>27}{'rate':>10}{'payout':>11}\n"
            file.write(col_name)
            print(col_name)
            for i in sorted(report['department']):
                depart_name = i + '\n'
                file.write(depart_name)
                print(depart_name)
                name = report['department'][i]['name']
                hours = report['department'][i]['hours']
                rate = report['department'][i]['rate']
                payout = report['department'][i]['payout']
                for n, h, r, p in zip(name, hours, rate, payout):
                    file.write(f"{'-' * 14} {n:>1}{' ' * (26 - len(n))}{h}{r:>10}{'$':>8}{p}\n")
                    print(f"{'-' * 14} {n:>1}{' ' * (26 - len(n))}{h}{r:>10}{'$':>8}{p}")
                sum_hours = sum(hours)
                sum_payout = sum(payout)
                file.write(f"{sum_hours:>44} {'$':>17}{sum_payout}\n")
                print(f"{sum_hours:>44} {'$':>17}{sum_payout}")


parser = argparse.ArgumentParser(description='Отчет по заработной плате')
parser.add_argument('file', nargs='+', help='файлы с данными')
parser.add_argument('--report', choices=['payout'], required=True)
args = parser.parse_args()
salary = SalaryReport((args.file))
get_reports = {'payout': salary.get_salary_report()}
