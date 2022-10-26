import os
import shutil

PROJECT_DIRECTORY = os.getcwd()

if __name__ == '__main__':

    src_template = '{}/TCMLApiTemplate/templates/src'.format(os.path.dirname(PROJECT_DIRECTORY))
    src_target = '{}/src'.format(PROJECT_DIRECTORY)

    if not os.path.exists(src_target):
        os.makedirs(src_target)

    print('COPY .gitignore')
    shutil.copy2('{}/TCMLApiTemplate/.gitignore'.format(os.path.dirname(PROJECT_DIRECTORY)), '{}/.gitignore'.format(PROJECT_DIRECTORY))

    print('COPY github actions')
    github_template = '{}/TCMLApiTemplate/templates/.github'.format(os.path.dirname(PROJECT_DIRECTORY))
    github_target = '{}/.github'.format(PROJECT_DIRECTORY)
    shutil.copytree(github_template, github_target)

    print('COPY test directory')
    test_template = '{}/TCMLApiTemplate/templates/test'.format(os.path.dirname(PROJECT_DIRECTORY))
    test_target = '{}/test'.format(PROJECT_DIRECTORY)
    shutil.copytree(test_template, test_target)

    print('COPY wsgi file')
    shutil.copy2('{}/wsgi.py'.format(src_template), '{}/wsgi.py'.format(src_target))

    print('COPY modules directory')
    modules_template = '{}/TCMLApiTemplate/templates/src/modules'.format(os.path.dirname(PROJECT_DIRECTORY))
    modules_target = '{}/src/modules'.format(PROJECT_DIRECTORY)
    shutil.copytree(modules_template, modules_target)

    print('COPY routes directory')
    routes_template = '{}/TCMLApiTemplate/templates/src/routes'.format(os.path.dirname(PROJECT_DIRECTORY))
    routes_target = '{}/src/routes'.format(PROJECT_DIRECTORY)
    shutil.copytree(routes_template, routes_target)

    print('COPY libraries directory')
    libraries_template = '{}/TCMLApiTemplate/templates/src/libraries'.format(os.path.dirname(PROJECT_DIRECTORY))
    libraries_target = '{}/src/libraries'.format(PROJECT_DIRECTORY)
    shutil.copytree(libraries_template, libraries_target)

    if '{{ cookiecutter.use_database }}' == 'yes':
        print('COPY db directory')
        db_template = '{}/TCMLApiTemplate/templates/db'.format(os.path.dirname(PROJECT_DIRECTORY))
        db_target = '{}/db'.format(PROJECT_DIRECTORY)
        shutil.copytree(db_template, db_target)

        print('COPY .env')
        shutil.copy2('{}/TCMLApiTemplate/templates/.env.db.dev'.format(os.path.dirname(PROJECT_DIRECTORY)), '{}/.env'.format(PROJECT_DIRECTORY))

        print('COPY docker-compose')
        shutil.copy2('{}/TCMLApiTemplate/templates/docker-compose-db.yml'.format(os.path.dirname(PROJECT_DIRECTORY)), '{}/docker-compose.yml'.format(PROJECT_DIRECTORY))

        print('COPY main file')
        shutil.copy2('{}/main_db.py'.format(src_template), '{}/main.py'.format(src_target))

        print('COPY config file')
        shutil.copy2('{}/config_db.py'.format(src_template), '{}/config.py'.format(src_target))

        print('COPY requirements file')
        shutil.copy2('{}/requirements_db.txt'.format(src_template), '{}/requirements.txt'.format(src_target))

        print('COPY models directory')
        models_template = '{}/TCMLApiTemplate/templates/src/models'.format(os.path.dirname(PROJECT_DIRECTORY))
        models_target = '{}/src/models'.format(PROJECT_DIRECTORY)
        shutil.copytree(models_template, models_target)
    else:
        print('COPY .env')
        shutil.copy2('{}/TCMLApiTemplate/templates/.env.dev'.format(os.path.dirname(PROJECT_DIRECTORY)), '{}/.env'.format(PROJECT_DIRECTORY))

        print('COPY docker-compose')
        shutil.copy2('{}/TCMLApiTemplate/templates/docker-compose.yml'.format(os.path.dirname(PROJECT_DIRECTORY)), '{}/docker-compose.yml'.format(PROJECT_DIRECTORY))

        print('COPY main file')
        shutil.copy2('{}/main.py'.format(src_template), '{}/main.py'.format(src_target))

        print('COPY config file')
        shutil.copy2('{}/config.py'.format(src_template), '{}/config.py'.format(src_target))

        print('COPY requirements file')
        shutil.copy2('{}/requirements.txt'.format(src_template), '{}/requirements.txt'.format(src_target))
