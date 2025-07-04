import dagster as dg


def execute_query(query):
    del query


# start_marker_assets
@dg.asset
def sugary_cereals() -> None:
    execute_query(
        "CREATE TABLE sugary_cereals AS SELECT * FROM cereals WHERE sugar_grams > 10"
    )


@dg.asset(deps=[sugary_cereals])
def shopping_list() -> None:
    execute_query("CREATE TABLE shopping_list AS SELECT * FROM sugary_cereals")


# end_marker_assets


# start_marker_jobs
all_assets_job = dg.define_asset_job(name="all_assets_job")

sugary_cereals_job = dg.define_asset_job(
    name="sugary_cereals_job", selection="sugary_cereals"
)

# end_marker_jobs
