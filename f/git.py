def process_files(): 
    files = [ 
        {"name": "utf-8.txt", "encoding": "utf-8"}, 
        {"name": "windows1251.txt", "encoding": "windows-1251"}, 
    ] 
 
    for file in files: 
        try: 
            with open(file["name"], "r", encoding=file["encoding"]) as f: 
                content = f.read() 
                print(f"Содержимое {file['name']} до изменений: {content}") 
 
            with open(file["name"], "a", encoding=file["encoding"]) as f: 
                f.write("\nмир") 
 
            print(f'Строка "мир" добавлена в файл {file["name"]}.') 
        except Exception as e: 
            print(f"Ошибка обработки файла {file['name']}: {e}") 
 
process_files()