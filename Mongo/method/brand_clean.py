from tqdm import tqdm


'''============清洗[brand_country]欄位==========='''
def brandWash(datas):
    error_list = []
    fixed_list = []
    new_data = []
    print(f'開始清洗brand_country欄位')
    for data in tqdm(datas):

        try:
            brand = data['brand_country']
        except Exception as e:
            error_list.append(data)
            data_name = data['whiskey_name']
            print(f'預期外錯誤: {e}\n發現錯誤資料: {data_name}')

        #   type check
        if type(brand) != str:
            data['brand_country'] = str(brand)
        
        #   '?' fixed 
        if '?' in brand:
            if '//' in brand:
                if 'Ol??Major' in brand.split('//')[0].strip():
                    data['brand_country'] = "OL\' MAJOR"
                    fixed_list.append(data['name'])

                elif 'Kaiy?' in brand.split('//')[0].strip():
                    data['brand_country'] = 'Kaiyo'
                    fixed_list.append(data['name'])

                elif  'Ballantine?s' in brand.split('//')[0].strip():
                    data['brand_country'] = 'Ballantine\'s'
                    fixed_list.append(data['name'])

                elif 'KROB?R' in brand.split('//')[0].strip():
                    data['brand_country'] = 'Krobar'
                    fixed_list.append(data['name'])

                elif 'Muirhead?s' in brand.split('//')[0].strip():
                    data['brand_country'] = 'MUIRHEAD\'S'
                    fixed_list.append(data['name'])

                elif 'Gibson?s' in brand.split('//')[0].strip():
                    data['brand_country'] = 'Gibson\'s'
                    fixed_list.append(data['name'])

                elif 'Hy?go Prefecture' in brand.split('//')[0].strip():
                    data['brand_country'] = 'Hyogo Prefecture'
                    fixed_list.append(data['name'])

                elif 'Gibson?s' in brand.split('//')[0].strip():
                    data['brand_country'] = 'Gibson\'s'
                    fixed_list.append(data['name'])

            if 'Ko?' in brand:
                data['brand_country'] = 'KO\'OLAU'
                fixed_list.append(data['name'])
        new_data.append(data)
    print(f'已修改{len(list(set(fixed_list)))}筆資料')
    
    if error_checker(error_list) == True:
        return new_data
    else:
        return f'尚有{len(error_list)}錯誤資料未處理'

        
'''============錯誤紀錄============='''
def error_checker(error_list):
    if error_list == []:
        return True
    else:
        return f'尚有{len(error_list)}筆資料未處理'