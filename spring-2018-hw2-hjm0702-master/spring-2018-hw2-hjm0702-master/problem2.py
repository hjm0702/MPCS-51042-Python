import itertools

def full_paths(path_components, base_path='/'):
    raw = [ [i] if isinstance(i,str) else i for i in path_components]
    producted_list = list(itertools.product(*raw))
    slashed_list = ["/".join(i) for i in producted_list]
    final = [base_path + i for i in slashed_list]

    return final

if __name__ == "__main__":
    print (full_paths(['usr', ['lib', 'bin'], 'config', ['x', 'y', 'z']]))
    print (full_paths(['codes', ['python', 'c', 'c++'], ['Makefile']], base_path='/home/user/'))
