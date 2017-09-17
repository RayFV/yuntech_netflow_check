import winsound
import requests, lxml.html, bs4
import datetime, time
import configparser
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from win10toast import ToastNotifier
from random import randint
'''
record:
winsound and pygame.mixer.sound cant play 32bits .wav file . So we need to convert 32bits to 16bits before us start to code. (Example:Audacity)
'''

def notifications(netflow, type, alert_type):
    def show_toast(warning_text):
        toaster.show_toast(warning_text, "Your netflow used {0}{1}".format(netflow, type),
                           icon_path="yuntech_icon.ico", duration=10)
    # Random Text :)
    alert_type1_text = {1: "同學，你脫魯了嗎", 2: "同學，你好嗎", 3: "同學！！！！！請注意！！！！！！\n謝謝你的注意"}
    alert_type2_text = {1: "同學，你的宿網已超過你設定的流量", 2: "同學，請注意自己的流量哦！", 3:"小心流量"}
    alert_type3_text = {1: "同學，你的網路快爆了！！！！\n建議：少上網，多運動，還可以脫魯哦",
                        2: "快爆了快爆了快爆了快爆了快爆了快爆了！",
                        3: "同學，你的網路快爆了！！！！\n建議：關閉電腦，出去看松鼠",
                        4: "同學，你的網路快爆了！！！！\n建議：關閉電腦，乖乖讀書",
                        5: "同學，你的網路快爆了！！！！\n建議：沖一波華山"}

    toaster = ToastNotifier()
    warning_text = ""
    if alert_type == 1:
        warning_text = alert_type1_text[randint(1, len(alert_type1_text))]
    if alert_type == 2:
        warning_text = alert_type2_text[randint(1, len(alert_type2_text))]
    if netflow > 6 and type == 'GB':
        warning_text = alert_type3_text[randint(1, len(alert_type3_text))]
        show_toast(warning_text)
        # if netflow greater than netflow_alert, play the noisy sound
        play_sound()
    show_toast(warning_text)


def play_sound():
    winsound.PlaySound('sound.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_ALIAS)
    time.sleep(10)
    winsound.PlaySound(None, winsound.SND_ASYNC)

class Setting:

    def __init__(self):
        # read config file
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.default = self.config['DEFAULT']

        ## SETTING
        self.ip_addr = self.default['IP']
        self.URL = self.default['URL']
        self.netflow_alert = float(self.default['netflow_alert'])
        self.alert_type = self.default['alert_type']
        self.notifac_intervals_minutes = int(self.default['notifac_intervals_minutes'])

# Main
def main():
    # SCRAPY
    setting = Setting()
    s = requests.session()

    ### Here, we're getting the netflow page and then grabbing hidden form
    ### fields.  We're probably also getting several session cookies too.
    netflow = s.get(setting.URL)
    netflow_html = lxml.html.fromstring(netflow.text)

    #get csrf token
    hidden_inputs = netflow_html.xpath(r'//form//input[@type="hidden"]')
    form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}

    # add IP
    form['query_ip'] = setting.ip_addr
    response = s.post(setting.URL, data=form)
    response.encoding = 'unicode'

    #print(response.text)

    soup = bs4.BeautifulSoup(response.text, "lxml")
    netflow_data = soup.select("table.table.table-hover.sortable tr")

    data_list = []
    amount = 0
    max_amount = 2

    for table_row in netflow_data:
        # Each tr (table row) has 9 td HTML elements
        # But we only interest date and total of the netflow
        cells = table_row.findAll('td')

        # Our table has one exception -- a row without any cells.
        # Let's handle that special case here by making sure we
        # have more than zero cells before processing the cells
        if len(cells) > 0:
            # date: column-1; total_netflow: column-8
            date = cells[1].text
            total_netflow = cells[8].text

            data = {'date': date, 'total_netflow': total_netflow}
            data_list.append(data)
            amount += 1
        # We dont need too much data
        if amount == max_amount:
            break

    today_day = datetime.datetime.now().day

    for data in data_list:
        # We only need today netflow
        date = data['date']
        date = datetime.datetime.strptime(date, "%Y年%m月%d日").date()

        if date.day == today_day:
            current_netflow = data['total_netflow']
            current_netflow, flow_type = float(current_netflow[:-2]), current_netflow[-2:]

            if setting.alert_type == '2':
               if current_netflow > setting.netflow_alert and flow_type == 'GB':
                    notifications(current_netflow, flow_type, 2) # notification only

            if setting.alert_type == '1':
                notifications(current_netflow, flow_type, 1) # notification every times

# do
main()
notifac_intervals_minutes = Setting().notifac_intervals_minutes
# SCHEDULE
schedule = BlockingScheduler()
trigger = IntervalTrigger(minutes=notifac_intervals_minutes)
schedule.add_job(main, trigger)
schedule.start()
