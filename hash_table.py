voted = {}


def check_voter(name):
    if voted.get(name):
        print(f'kick this {name} out!')
    else:
        voted[name] = True
        print(f'let {name} vote!')


cache = {}


def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data


check_voter('tom')
check_voter('vanya')
check_voter('tom')
print(voted)
