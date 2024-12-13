
def f_read_file(url):
    try:
        with open(url, mode='r') as file:
            result = []
            temp = file.read()
            temp =  temp.split('\n')
        for q in temp:
            if not q:
                continue
            result.append(q.strip())
        return result           
    except FileNotFoundError:
            return None
    
