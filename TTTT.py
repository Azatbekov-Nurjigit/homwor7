



with open('test_regs.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    mega_list = re.findall(r'\+996 (?:55[0-9]|755|99[0579]) \d{2} \d{2} \d{2}', content)
    print(f'{len(mega_list)}: {mega_list}')
    beeline_list = re.findall(r'\+996 (?:77[0-9]|22[0-57]) \d{2} \d{2} \d{2}', content)
    print(f'{len(beeline_list)}: {beeline_list}')
    o_list = re.findall(r'\+996 (?:50[0-27-945]|70[0-9]) \d{2} \d{2} \d{2}', content)
    print(f'{len(o_list)}: {o_list}')
    r'\+996 (?:77[0-9]|22[0-57]) \d{2} \d{2} \d{2}'


