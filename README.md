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
1. config.yaml
2. schema.yaml
3. params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components in src components
7. Update the pipeline in src pipeline
8. Update the main.py

### Workflow Details
* We update the below files in that order to achieve the ML pipeline:
1. config.yaml
   1. Needed for Data Ingestion, Data Validation
   2. Data Ingestion: Fill this first config_data_ingestion.py
   3. Data Validation: Fill this first config_data_validation.py
2. schema.yaml
   1. Not needed for Data Ingestion 
3. params.yaml
   1. Not needed for Data Ingestion 
4. Update the entity
   1. Needed for Data Ingestion
   2. Data Ingestion: Fill this first config_entity.py
5. Update the configuration manager in src config
   1. Needed for Data Ingestion
   2. Data Ingestion: Fill this first configuration.py
6. Update the components in src components
   1. Needed for Data Ingestion
   2. Data Ingestion: Fill this first data_ingestion.py
7. Update the pipeline in src pipeline
8. Update the main.py