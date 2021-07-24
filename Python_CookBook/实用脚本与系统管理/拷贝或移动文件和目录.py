import shutil

# shutil.copy('01.txt', '02.txt')  # 相当于cp src dst
# shutil.copy2('01.txt', '03.tgz')  # 相当于cp -p src dst
# # shutil.copytree(src=" ", dst=" ")  # 相当于cp -R src dst
# shutil.move('01.txt', '../并发')

# def ignore_pyc_files(dirname, filenames):
#     return [name in filenames if name.endwith('.pyc')]
#
#
# try:
#     shutil.copytree(ignore=ignore_pyc_files)
# except shutil.Error as e:
#     for src, dst, msg in e.args[0]:
#         print(src, dst, msg)
# shutil.copytree(src='', dst='', ignore=shutil.ignore_patterns('*~', '*.pyc'))

# shutil.unpack_archive('03.tgz')  # 解压
# shutil.make_archive('py33', 'zip', '02.txt')  # 压缩
# print(shutil.get_archive_formats())


