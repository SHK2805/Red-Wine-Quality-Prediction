# End to end ML project
* This is a template for an end to end ML project.

### ML Pipeline
* The ML pipeline is a sequence of steps that are executed in order to build, train, evaluate, and deploy a machine learning model.
* Below are the steps in the ML pipeline:
1. Data Collection
2. Data Ingestion
3. Data Transformation
4. Model Training
5. Model Evaluation
6. Model Deployment
7. Model Monitoring
8. Model Retraining

### Workflow
* We update the below files in that order to achieve the ML pipeline:
1. config > config.yaml
   1. data_ingestion
   2. data_validation
   3. data_transformation
   4. model_training
2. schema.yaml
   1. The schema of the data i.e. the column headers and the data types
   2. data_validation
3. params.yaml
   1. The parameters for the model training
   2. model_training
4. Update the entity
   1. In src > entity > config_entity.py
5. Update the configuration manager 
   1. In src > config > configuration.py
6. Update the components 
   1. In src > components 
      1. data_ingestion.py
      2. data_validation.py
      3. data_transformation.py
      4. model_trainer.py
7. Update the pipeline
    1. In src > pipeline
        1. data_ingestion.py
        2. data_validation.py
        3. data_transformation.py 
8. Update the main.py

### Workflow Details
* We update the below files in that order to achieve the ML pipeline:
1. config.yaml
   1. Needed for Data Ingestion, Data Validation
   2. Data Ingestion: Fill this first data_ingestion
   3. Data Validation: Fill this first data_validation
   4. Data Transformation: Fill this first data_transformation
2. schema.yaml
   1. Not needed for Data Ingestion
   2. Needed for Data Validation
      1. Data Validation: Fill this second schema.yaml
         1. Add the key value pairs for the data schema the name of the column and the type of the column
3. params.yaml
   1. Not needed for Data Ingestion 
4. Update the entity
   1. Needed for Data Ingestion, Data Validation
   2. Data Ingestion: Fill this second config_entity.py
      1. Add the key value pairs for the data schema the name of the column, and the type of the column should match the ones in config.yaml
   3. Data Validation: Fill this third config_entity.py
      1. Add the key value pairs for the data schema the name of the column, and the type of the column should match the ones in config.yaml
5. Update the configuration manager in src config
   1. Needed for Data Ingestion
   2. Data Ingestion: Fill this third configuration.py get_data_ingestion_config
   3. Data Validation: Fill this fourth configuration.py
6. Update the components in src components
   1. Needed for Data Ingestion
   2. Data Ingestion: Fill this forth data_ingestion.py
   3. Data Validation: Fill this fifth data_validation.py
7. Update the pipeline in src pipeline
   1. Needed for Data Ingestion, Data Validation
   2. Data Ingestion: Fill this fifth data_ingestion.py
   3. Data Validation: Fill this sixth data_validation.py
8. Update the main.py
    1. Needed for Data Ingestion, Data Validation
    2. Data Ingestion: Fill this sixth main.py
    3. Data Validation: Fill this seventh main.py