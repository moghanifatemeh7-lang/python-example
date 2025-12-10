from datetime import datetime
events = {
     '2025-01-01': 'sal miladi',
 '2025-03-21': 'noroz',
 '2025-04-02': 'meli shodan naft',
 '2025-06-15': 'tavalod emam reza',
 '2025-07-11': 'roz ghalam',
 '2025-08-23': 'ghadir khom',
 '2025-09-21': 'shab yalda',
 '2025-11-12': 'roz danesh amoz',
 '2025-12-05': 'vafat hazrat masome',
 '2025-12-30': 'pirozi enghelab eslami'
}

def check_event(date_str):
 
        parsed_date = datetime.strptime(date_str, '%Y/%m/%d')
        date_key = parsed_date.strftime('%Y-%m-%d')

        if date_key in events:
         return f"('monasebat emroz'{date_str}): {events[date_key]} 🎉"
        else:
         return f"('baray tarikh' {date_str}،monasebati tarif nashode"


user_date = input("tarikh ro vared kon mesl (2025/03/21): ")
result = check_event(user_date)
print(result)