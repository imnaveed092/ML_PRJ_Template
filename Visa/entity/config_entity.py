from collections import namedtuple



DataIngestionConfig: namedtuple("DataIngestionConfig",
                                ['dataset_download_url','raw_data_dir','ingested_dir','ingetsted_train_dir','ingested_test_dir'])


DataValidationCongif: namedtuple('DataValidationCongif',['schema_file_dir'])