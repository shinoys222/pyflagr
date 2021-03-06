# flagr
Flagr is a feature flagging, A/B testing and dynamic configuration microservice. The base path for all the APIs is \"/api/v1\". 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1.0
- Package version: 1.1.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import flagr 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import flagr
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = flagr.ConstraintApi()
flag_id = 789 # int | numeric ID of the flag
segment_id = 789 # int | numeric ID of the segment
body = flagr.CreateConstraintRequest() # CreateConstraintRequest | create a constraint

try:
    api_response = api_instance.create_constraint(flag_id, segment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConstraintApi->create_constraint: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConstraintApi* | [**create_constraint**](docs/ConstraintApi.md#create_constraint) | **POST** /flags/{flagID}/segments/{segmentID}/constraints | 
*ConstraintApi* | [**delete_constraint**](docs/ConstraintApi.md#delete_constraint) | **DELETE** /flags/{flagID}/segments/{segmentID}/constraints/{constraintID} | 
*ConstraintApi* | [**find_constraints**](docs/ConstraintApi.md#find_constraints) | **GET** /flags/{flagID}/segments/{segmentID}/constraints | 
*ConstraintApi* | [**put_constraint**](docs/ConstraintApi.md#put_constraint) | **PUT** /flags/{flagID}/segments/{segmentID}/constraints/{constraintID} | 
*DistributionApi* | [**find_distributions**](docs/DistributionApi.md#find_distributions) | **GET** /flags/{flagID}/segments/{segmentID}/distributions | 
*DistributionApi* | [**put_distributions**](docs/DistributionApi.md#put_distributions) | **PUT** /flags/{flagID}/segments/{segmentID}/distributions | 
*EvaluationApi* | [**post_evaluation**](docs/EvaluationApi.md#post_evaluation) | **POST** /evaluation | 
*EvaluationApi* | [**post_evaluation_batch**](docs/EvaluationApi.md#post_evaluation_batch) | **POST** /evaluation/batch | 
*ExportApi* | [**get_export_sq_lite**](docs/ExportApi.md#get_export_sq_lite) | **GET** /export/sqlite | 
*FlagApi* | [**create_flag**](docs/FlagApi.md#create_flag) | **POST** /flags | 
*FlagApi* | [**delete_flag**](docs/FlagApi.md#delete_flag) | **DELETE** /flags/{flagID} | 
*FlagApi* | [**find_flags**](docs/FlagApi.md#find_flags) | **GET** /flags | 
*FlagApi* | [**get_flag**](docs/FlagApi.md#get_flag) | **GET** /flags/{flagID} | 
*FlagApi* | [**get_flag_entity_types**](docs/FlagApi.md#get_flag_entity_types) | **GET** /flags/entity_types | 
*FlagApi* | [**get_flag_snapshots**](docs/FlagApi.md#get_flag_snapshots) | **GET** /flags/{flagID}/snapshots | 
*FlagApi* | [**put_flag**](docs/FlagApi.md#put_flag) | **PUT** /flags/{flagID} | 
*FlagApi* | [**set_flag_enabled**](docs/FlagApi.md#set_flag_enabled) | **PUT** /flags/{flagID}/enabled | 
*HealthApi* | [**get_health**](docs/HealthApi.md#get_health) | **GET** /health | 
*SegmentApi* | [**create_segment**](docs/SegmentApi.md#create_segment) | **POST** /flags/{flagID}/segments | 
*SegmentApi* | [**delete_segment**](docs/SegmentApi.md#delete_segment) | **DELETE** /flags/{flagID}/segments/{segmentID} | 
*SegmentApi* | [**find_segments**](docs/SegmentApi.md#find_segments) | **GET** /flags/{flagID}/segments | 
*SegmentApi* | [**put_segment**](docs/SegmentApi.md#put_segment) | **PUT** /flags/{flagID}/segments/{segmentID} | 
*SegmentApi* | [**put_segments_reorder**](docs/SegmentApi.md#put_segments_reorder) | **PUT** /flags/{flagID}/segments/reorder | 
*VariantApi* | [**create_variant**](docs/VariantApi.md#create_variant) | **POST** /flags/{flagID}/variants | 
*VariantApi* | [**delete_variant**](docs/VariantApi.md#delete_variant) | **DELETE** /flags/{flagID}/variants/{variantID} | 
*VariantApi* | [**find_variants**](docs/VariantApi.md#find_variants) | **GET** /flags/{flagID}/variants | 
*VariantApi* | [**put_variant**](docs/VariantApi.md#put_variant) | **PUT** /flags/{flagID}/variants/{variantID} | 


## Documentation For Models

 - [Constraint](docs/Constraint.md)
 - [CreateConstraintRequest](docs/CreateConstraintRequest.md)
 - [CreateFlagRequest](docs/CreateFlagRequest.md)
 - [CreateSegmentRequest](docs/CreateSegmentRequest.md)
 - [CreateVariantRequest](docs/CreateVariantRequest.md)
 - [Distribution](docs/Distribution.md)
 - [Error](docs/Error.md)
 - [EvalContext](docs/EvalContext.md)
 - [EvalDebugLog](docs/EvalDebugLog.md)
 - [EvalResult](docs/EvalResult.md)
 - [EvaluationBatchRequest](docs/EvaluationBatchRequest.md)
 - [EvaluationBatchResponse](docs/EvaluationBatchResponse.md)
 - [EvaluationEntity](docs/EvaluationEntity.md)
 - [Flag](docs/Flag.md)
 - [FlagSnapshot](docs/FlagSnapshot.md)
 - [PutDistributionsRequest](docs/PutDistributionsRequest.md)
 - [PutFlagRequest](docs/PutFlagRequest.md)
 - [PutSegmentReorderRequest](docs/PutSegmentReorderRequest.md)
 - [PutSegmentRequest](docs/PutSegmentRequest.md)
 - [PutVariantRequest](docs/PutVariantRequest.md)
 - [Segment](docs/Segment.md)
 - [SegmentDebugLog](docs/SegmentDebugLog.md)
 - [SetFlagEnabledRequest](docs/SetFlagEnabledRequest.md)
 - [Variant](docs/Variant.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



