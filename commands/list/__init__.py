def import_commands():
    import glob
    import importlib
    module = glob.glob("commands/list/**/*.py", recursive=True)
    module.sort()
    module.pop(0)
    for m in module:
        module_name = m[:-3].replace("/", ".").replace("\\", ".")
        importlib.import_module(module_name)


import_commands()
