import yaml


def dbt_schema_yml_splitter():
    """
    Splits the schema.yml file of DBT schema to multiple schema YML files by models
    """
    try:
        with open("schema.yml", "r", encoding="utf-8") as stream:
            data = yaml.load(stream, yaml.FullLoader)
            for model in data["models"]:
                with open(model["name"] + ".yml", "a", encoding="utf-8") as outfile:
                    outfile.write(f"version: {data['version']}\n\nmodels:\n")
                    yaml.dump(
                        data=[model],
                        stream=outfile,
                        default_flow_style=False,
                        sort_keys=False,
                        allow_unicode=True,
                        encoding="utf-8",
                    )
    except yaml.YAMLError as e:
        print(e)


if __name__ == "__main__":
    dbt_schema_yml_splitter()
