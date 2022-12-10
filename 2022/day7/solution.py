# https://adventofcode.com/2022/day/6
def get_folder_size(folder):
    return sum([f.size if f.type == 'file' else get_folder_size(folders[f.path]) for f in folder.children])


class Child:
    def __init__(self, name, parent, type="file", size=0):
        self.name = name
        self.size = size
        self.type = type
        self.path = parent

    def __str__(self) -> str:
        return "{} <{} {}>".format(self.type, self.name, self.size)

    def __repr__(self):
        return self.__str__()


class Folder:
    def __init__(self, path, parent=None):
        self.path = path
        self.parent = parent
        self.children = []
        self.size = 0

    def addChild(self, f):
        self.children.append(f)

    def __str__(self) -> str:
        return "{} {}".format(self.path, self.size)

    def __repr__(self):
        return self.__str__()


file = open('input.txt', 'r')
# file = open('sample.txt', 'r')
input = file.read().splitlines()

folders = {'/': Folder('/', '')}

curr_folder: Folder = None
for l in input:
    l = l.split()
    if (l[0], l[1]) == ('$', 'cd'):
        if l[2] == '..':
            curr_folder = folders[curr_folder.parent]
        elif l[2] == '/':
            curr_folder = folders['/']
        else:
            new_path = curr_folder.path+l[2]+'/'
            folders[new_path] = Folder(new_path, curr_folder.path)
            try:
                temp_folder = folders[new_path]
                curr_folder = temp_folder
            except KeyError:
                curr_folder = Folder(
                    curr_folder.path+l[2]+'/', curr_folder.path)
                folders[curr_folder.path] = curr_folder
    elif l[0] != '$':
        if l[0] == 'dir':
            path = curr_folder.path+l[1]+'/'
            folders[path] = Folder(path, curr_folder.path)
            curr_folder.addChild(Child(l[1], path, "folder"))
        else:
            curr_folder.addChild(Child(l[1], path, "file", int(l[0])))

# Part I solution
for f in folders.values():
    f.size = get_folder_size(f)
out = [folders[k].size for k in folders.keys()]
out = sum([i for i in out if i < 100_000])
print('1. What is the sum of the total sizes of those directories? =>', out)
# End part I
# Your puzzle answer was 1453349.

# Part II solution
disk_size, upd_req = 70_000_000, 30_000_000
unused_space = disk_size-folders['/'].size
needed_space = upd_req-unused_space
out = sorted(folders.values(), key=lambda e: e.size)
out = [f for f in out if f.size >= needed_space]
out = out[0].size
print('2. What is the total size of that directory? =>', out)
# End part II
# Your puzzle answer was 2948823.
