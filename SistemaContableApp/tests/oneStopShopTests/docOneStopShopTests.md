## Scenario Configuration

### OneStopSearchTest
| Name                           | Class          | Stage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| create_instances               | SearchTestCase | Creates instances of some objects in the database for testing purposes.<br>Specifically, instances of the following objects are created:<br>- RequestStatus<br>- RequestType<br>- CreationDate<br>- ClosureDate                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| testFilterRequestByStatus      | SearchTestCase | Unit test to verify filtering requests by status.<br>Request instances are created, and a GET request is made with the 'status' parameter, where the status is assumed to be "Approved". Then, a request is made to the 'one_stop_shop' controller. It is verified that the response has a status code of 200 and that the response content contains the first request since its status is "Approved".                                                                                                                                                                                               |
| test_search_request            | SearchTestCase | Tests the search for a request.<br>This test verifies that the `search_` function responds correctly to a GET request with a search parameter and returns a status code of 200 along with the content of the searched request.                                                                                                                                                                                                                                                                                                                                                                             |

### Purpose of the search test

The purpose of the tests in "search" is to test the functionality of the search method in the system. This test verifies if the search method returns the expected results when provided with a specific set of input data, and the purpose of these tests would be to ensure that the search method is implemented correctly and returns the correct results according to the established search criteria.

### Search test cases

| Class                  | Method                        | Stage                                                                                                                                                                                                                                                                                                                                                                                            | Input Values                                                                                                                                                                                                                                                                                                                                                                                                         | Expected Result                                                                                                                                                                                                                                                                                                                          |
|------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SearchTestCase         | create_instances              | Creates instances of some objects in the database for testing purposes. Specifically, instances of the following objects: RequestStatus, RequestType, CreationDate, ClosureDate                                                                                                                                                                                                   | -                                                                                                                                                                                                                                                                                                                                                                                                                        | It is expected that instances of objects in the database for the mentioned objects, such as RequestStatus, RequestType, CreationDate, and ClosureDate, which are necessary for tests related to the search and filtering of requests, are created.                                                                                                                                               |
| SearchTestCase         | testFilterRequestByStatus     | Unit test to verify filtering requests by status. Request instances are created, and a GET request is made with the 'status' parameter, where the status is assumed to be "Approved". Then, a request is made to the 'one_stop_shop' controller. It is verified that the response has a status code of 200 and that the response content contains the first request since its status is "Approved". | -                                                                                                                                                                                                                                                                                                                                                                                                                        | It is expected that by filtering the requests by "Approved" status, the 'one_stop_shop' view responds with a status code of 200, and the response content contains the first request, as its status is "Approved".                                                                                                                                                                                   |
| SearchTestCase         | test_search_request           | Tests the search for a request. This test verifies that the `search_one_stop_shop` function responds correctly to a GET request with a search parameter and returns a status code of 200 along with the content of the searched request.                                                                                                                                                                                                | -                                                                                                                                                                                                                                                                                                                                                                                                                        | It is expected that by performing the search for requests with the "requisition" parameter, the 'search_one_stop_shop' view responds with a status code of 200, and the response content contains the request with type "requisition", ensuring that the search method is implemented correctly and returns the correct results according to the established search criterion.  |

## Scenario Configuration

### ViewTestCase

| Name | Class        | Stage |
| ------ | ------------ | ----- |
| setUp  | ViewTestCase | -     |

### Objective of the Tests

The objective of these tests is to verify the correct functioning of the views in the accounting system, including template rendering, passing required context data, and form processing.

### Test Cases

| Class        | Method                    | Stage                       | Expected Result                                                                                               |
| ------------ | ------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------- |
| ViewTestCase | testSummaryOneStopShopView| -                           | Verify that the 'summaryOneStopShop' view returns a status code of 200, uses the correct template, and passes the required context data.                           |
| ViewTestCase | testFullOneStopShopView   | -                           | Verify that the 'fullOneStopShop' view returns a status code of 200, uses the correct template, and passes the required context data, including 'followingData' and 'files'. |
| ViewTestCase | testOneStopShopFormViewGet| -                           | Verify that the 'OneStopShopForm' view returns a status code of 200, uses the correct template, and passes the required context data, including 'oneStopShopForm' and 'attachedDocumentForm'. |
| ViewTestCase | testOneStopShopFormViewPostValid| -                    | Verify that the 'OneStopShopForm' view redirects after a successful form submission and creates the expected Following and AttachedDocument instances.    |

## Scenario Configuration

### ModelTestCase

| Name | Class        | Stage |
| ------ | ------------ | ----- |
| setUp  | ModelTestCase| -     |

### Objective of the Tests

The objective of these tests is to verify that the models of the applications function correctly, including creating instances with valid data and the expected string representation.

### Test Cases

| Class        | Method                    | Stage   | Expected Result                                                                                                          |
| ------------ | ------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------ |
| ModelTestCase | testFollowingModel       | -       | Verify that the Following model creates instances correctly and returns the expected string representation.           |
| ModelTestCase | testAttachedDocumentModel| -       | Verify that the AttachedDocument model creates instances correctly and returns the expected string representation.   |

## Scenario Configuration

### FormTestCase

| Name | Class       | Stage |
| ------ | ----------- | ----- |
| setUp  | FormTestCase| -     |

### Objective of the Tests

The objective of these tests is to verify that the forms of the application function correctly, both with valid data and with invalid data.

### Test Cases

| Class       | Method                 | Stage | Expected Result                                                                                         |
| ----------- | ---------------------- | ----- | ---------------------------------------------------------------------------------------------------------- |
| FormTestCase| testOneStopShopValidForm   | -     | Verify that the OneStopShopForm form is valid when provided with valid data.                              |
| FormTestCase| testAttachedDocumentValidForm | - | Verify that the AttachedDocumentForm form is valid when provided with valid file data.                        |
| FormTestCase| testOneStopShopInvalidForm  | -     | Verify that the OneStopShopForm form is invalid when provided with incomplete data.                          |
| FormTestCase| testAttachedDocumentInvalidForm| - | Verify that the AttachedDocumentForm form is invalid when provided with incorrect file data.                |

                                                                                                                                                                                               