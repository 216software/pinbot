# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

from setuptools import find_packages, setup

setup(

    name="pystreamliner",

    version="0.0.1",

    packages=find_packages(),

    include_package_data=True,

    package_dir={"pystreamliner": "pystreamliner"},

    scripts=[
        "pystreamliner/scripts/pystreamliner-run-webapp",
        "pystreamliner/scripts/pystreamliner-upgrade-database",
        "pystreamliner/scripts/pystreamliner-rebuild-database",
        "pystreamliner/scripts/pystreamliner-config",
        "pystreamliner/scripts/pystreamliner-yaml-example",
        "pystreamliner/scripts/load_v2_weekly_manifest.py",
        "pystreamliner/scripts/pystreamliner-load-dump",
        "pystreamliner/scripts/load_all_weekly_manifests.py",
        "pystreamliner/scripts/look_up_amazon_prices.py",
        "pystreamliner/scripts/fast_look_up_amazon_prices.py",
        "pystreamliner/scripts/mp_look_up_amazon_prices.py",
        "pystreamliner/scripts/wm_asin_lookup.py",
        "pystreamliner/scripts/ms2ascii.py",
        "pystreamliner/scripts/search_by_item_description.py",
        "pystreamliner/scripts/look-up-all-prices.sh",
        "pystreamliner/scripts/rebuild-materialized-views-and-csv-files",
        "pystreamliner/scripts/grab-amazon-files.sh",
        "pystreamliner/scripts/load_all_truck_level_manifests.py",
        "pystreamliner/scripts/pystreamliner-load-from-db-template",
        "pystreamliner/scripts/rebuild-snapshot-db",
        "pystreamliner/scripts/rewrite-container-contents-csv-files",
        "pystreamliner/scripts/rewrite-container-barcodes",
        "pystreamliner/scripts/load_one_truck_level_manifest.py",
        "pystreamliner/scripts/rewrite-scan-reports",
        "pystreamliner/scripts/load-ebay-categories",
        "pystreamliner/scripts/update_csv_listener.py",
        "pystreamliner/scripts/inmar_listener.py",
        "pystreamliner/scripts/cvs_listener.py",
        "pystreamliner/scripts/load_mcr_manifest.py",
        "pystreamliner/scripts/input-uploaded-inmar-files",
        "pystreamliner/scripts/mcr_listener.py",
        "pystreamliner/scripts/rewrite_mcr_csv_files.py",
        "pystreamliner/scripts/rewrite_cvs_asset_reports.py",
        "pystreamliner/scripts/repair-cvs-scans",
    ],

)
