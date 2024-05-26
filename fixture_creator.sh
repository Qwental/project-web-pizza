#!/bin/bash

manage_py_path="./manage.py"

mkdir -p fixtures

apps=$(python $manage_py_path shell -c "from django.apps import apps; print(' '.join([app.label for app in apps.get_app_configs()]))")

for app in $apps; do
    models=$(python $manage_py_path shell -c "from django.apps import apps; app = apps.get_app_config('$app'); print(' '.join([f'{app.label}.{model.__name__}' for model in app.get_models()]))")

    for model in $models; do
        echo "$model fixture created";

        app_name=$(echo $model | cut -d'.' -f1)
        model_name=$(echo $model | cut -d'.' -f2)

        mkdir -p fixtures/$app_name

        python $manage_py_path dumpdata $model > fixtures/$app_name/$model_name.json
    done
done
