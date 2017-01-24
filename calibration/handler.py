from shutil import move
from shutil import copyfile
from os import remove, close
from tempfile import mkstemp


def replace_word(file_path, pattern, subst):  # idf파일에서, 설계변수의 수치를 변경하는 모듈
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    remove(file_path)
    move(abs_path, file_path)


def remove_file(src):
    remove(src)


def copy_file(src, dst):
    copyfile(src, dst)


