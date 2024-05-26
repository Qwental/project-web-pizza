#!/bin/bash

manage_py_path="./manage.py"

apps=$(python $manage_py_path shell -c "from django.apps import apps; print(' '.join([app.label for app in apps.get_app_configs()]))")

for app in $apps; do
    models=$(python $manage_py_path shell -c "from django.apps import apps; app = apps.get_app_config('$app'); print(' '.join([f'{app.label}.{model.__name__}' for model in app.get_models()]))")

    for model in $models; do
        app_name=$(echo $model | cut -d'.' -f1)
        model_name=$(echo $model | cut -d'.' -f2)

        if [ -f fixtures/$app_name/$model_name.json ]; then
            echo "Loading $model fixture";
            python $manage_py_path loaddata fixtures/$app_name/$model_name.json
        fi
    done
done
