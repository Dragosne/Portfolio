<h1>API Testing Project</h1>

The purpose of this project is to apply the API testing knowledge gained throughout the Software Testing course in practical scenarios, using a real-life application. The chosen platform for testing is Trello, a popular project management and organization application that offers a robust API for interacting with its functionalities.

Through this project, we aim to explore various aspects of API testing, including basic functionality, data verification, and performance management. We utilized the acquired knowledge to create and execute tests covering the most significant actions available in Trello, such as board creation, list management, and card manipulation.

Each test and API request was designed to properly evaluate the behavior and functionality of the Trello platform in different usage scenarios. Thus, this project represents a valuable opportunity to apply theory into practice and solidify our understanding of the API testing process in a real-world environment.

The application under test: **Trello**

Tools used: Postman, Newman

[**API Collection link:**](https://www.postman.com/gold-rocket-762536/workspace/trello/request/31285083-e24bfdb3-2dc8-4e2f-9980-9d60f8122e4e)

The Trello REST API documentation: [**link**](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/#api-group-actions)

### Tests performed:

********

<h3>1. CREATE A BOARD </h3>
  
**HTTP method for request: POST**<br>

**Request description:**
This request creates a new board in Trello. According to the API documentation, you must provide a **name** for the new board, your APItoken and APIkey (provided by Trello by following the authorization steps).<be>

**Test types/techniques used:** <br>
Functional testing. Verify that the API endpoint correctly creates a new Trello board.<br>
Positive testing: Ensure the API returns the correct response when valid data is provided.<br>
Data validation: Ensure the response contains each field's expected data types and values.<br>
Status Code Verification: Confirm that the API returns appropriate status codes (200 OK for successful requests)<br>
Response Time Testing: Measure the API's response time and ensure it meets performance criteria.<br>

**Response status code:** 200 (OK)<br>

Below you can find a picture of the API request from Postman:<be>
![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/1st%20request_create_board.png)<br>

**JavaScript Tests:** [create a board tests](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/create%20a%20board%20tests.txt)

**Test Results**

![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/create%20a%20board%20test%20results.png)<br>

********

<h3>2. GET A BOARD </h3>
  
**HTTP method for request: GET**<br>

**Request Description:**
This request retrieves the details of a specific board in Trello. According to the API documentation, you need to provide the board ID to get the information. The response includes details such as the board's name, description, organization ID, and other metadata..<be>

**Test types/techniques used:** <br>
Functional testing: verify that the API endpoint returns the correct details for a given board ID.<br>
Positive Testing: Ensure the API returns the correct response when valid data is provided<br>
Data validation: Ensure the response contains each field's expected data types and values.<br>
Status Code Verification: Confirm that the API returns appropriate status codes (200 OK for successful requests)<br>

**Response status code:** 200 (OK)<br>

Below you can find a picture of the API request from Postman:<be>
![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/get%20a%20board%20requrest.png)<br>

**JavaScript Tests:** [get a board tests](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/get%20a%20board%20tests.txt)

**Test Results**

![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/get%20a%20board%20test%20results.png)<br>

*******

<h3>3. UPDATE A BOARD </h3>
  
**HTTP method for request: PUT**<br>

**Request Description:**
This request updates the details of a specific board in Trello. According to the API documentation, you need to provide the board ID and the new details you want to update. For example, you can update the board's name. The response should confirm that the board's details have been successfully updated.<br>
We will use the "Postman Board June3" board created in a previous session. It will be renamed: "Updated Postman Board"

**Body:** 
```
{
    "name": "{{new_board_name}}"
}
```
**Pre-request Script (create a variable with the desired new board name):** 
```
var newBoardName = "Updated Board Name";
pm.environment.set("new_board_name", newBoardName);
```

**Test types/techniques used:** <br>
Functional Testing: Verify that the API endpoint correctly updates the specified board details.<br>
Positive Testing: Ensure the API returns the correct response when valid data is provided.<br>
Data validation: Ensure the response contains each field's expected data types and values.<br>
Status Code Verification: Confirm that the API returns appropriate status codes (200 OK for successful requests)<br>
Response Time Testing: Measure the API's response time and ensure it meets performance criteria.<br>

**Response status code:** 200 (OK)<br>

Below you can find a picture of the API request from Postman:<be>
![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/update%20a%20board.png)<br>

**JavaScript Tests:** [update a board tests](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/update%20a%20board%20tests%20list.txt)

**Test Results**

![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/update%20a%20board%20tests.png)<br>

*******

<h3>4. CREATE LISTS: TO DO, DOING, DONE </h3>
  
**HTTP method for request: POST**<be>

**Request Description:**
These requests create three lists on a specific board in Trello. According to the API documentation, you need to provide the board ID and the list's name. The response should confirm that each list has been successfully created with the specified name.

**Body:** <br>
```
{
    "name": "{{list_name}}",
    "idBoard": "{{postmanBoardID}}"
}
```
**Pre-request Script (to set the list name for each request):**
```
for "TO DO":
var listName = "TO DO";
pm.environment.set("list_name", listName);
```
```
for "DOING":
var listName = "DOING";
pm.environment.set("list_name", listName);
```
```
for "DONE":
var listName = "DONE";
pm.environment.set("list_name", listName);
```
**Test types/techniques used:** <br>
Functional Testing: Verify that the API endpoint correctly creates a new list with the specified name on the given board.<br>
Positive Testing: Ensure the API returns the correct response when valid data is provided.<br>
Data Validation: Ensure the response contains each field's expected data types and values.<br>
Status Code Verification: Confirm that the API returns appropriate status codes (200 OK for successful creations).<br>
Response Time Testing: Measure the API's response time and ensure it meets performance criteria.<br>

**Response status code:** 200 (OK)<br>

Below you can find a picture of the API request from Postman:<be>
![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/create%20a%20list%20request.png)<br>

**JavaScript Tests:** [create a list tests](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/create%20a%20list%20tests.txt)

**Test Results**

![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/create%20a%20list%20response%20status.png)<br>

********

<h3>5. ADD A CARD</h3>
  
**HTTP method for request: POST**<be>

**Request Description:**
This request adds a new card to a specific list. The card information is sent in the body of the request.

**Body:** <br>
```
{
    "name": "PAY TAXES",
    "desc": "property tax",
    "due": "2024-06-06",
    "dueComplete": false,
    "idList": "{{listID}}"
}
```

**Test types/techniques used:** <br>
Functional Testing: Verify that the card details are created correctly.<br>
Positive Testing: Ensure that valid inputs result in a successful format.<br>
Status Code Verification: Confirm that the API returns appropriate status codes (200 OK for successful requests)<br>
Response Time Testing: Measure the API's response time and ensure it meets performance criteria.<br>


**Response status code:** 200 (OK)<br>

Below you can find a picture of the API request from Postman:<be>
![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/add%20a%20card%20request.png)<br>

**JavaScript Tests:** [add a card tests](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/add%20a%20card.txt)

**Test Results**

![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/add%20a%20card%20tests%20result.png)<br>

********

<h3>6. UPDATE A LISTS</h3>
  
**HTTP method for request: PUT**<be>

**Request Description:**
This request enables the user to update the details of a specified list in Trello. According to the API documentation, the user can update properties such as the list name or other attributes by making a PUT request and providing the ID. We will change the name of a list from "DOING" to "PROGRESS".

**Body:** <br>
```
{
    "name": "PROGRESS",
}
```

**Test types/techniques used:** <br>
Functional Testing: Verify that the list name is updated correctly.<br>
Positive Testing: Ensure that valid inputs result in successful updates.<br>
Status Code Verification: Confirm that the API returns appropriate status codes (200 OK for successful requests)<br>
Response Time Testing: Measure the API's response time and ensure it meets performance criteria.<br>

**Response status code:** 200 (OK)<br>

Below you can find a picture of the API request from Postman:<be>
![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/update%20a%20list%20request.png)<br>

**JavaScript Tests:** [update a list tests](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/delete%20a%20board%20tests%20list.txt)

**Test Results**

![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/update%20a%20list%20test%20results.png)<br>

********

<h3>7. DELETE A BOARD </h3>
  
**HTTP method for request: DELETE**<br>

**Request description:**
This request deletes a specific board in Trello. According to the API documentation, you need to provide the board ID to delete the board. The response should confirm that the board has been successfully deleted.<br>
We will delete the board: "Updated Postman Board"

**Test types/techniques used:** <br>
Functional Testing: Verify that the API endpoint correctly deletes the specified board details.<br>
Positive Testing: Ensure the API returns the correct response when a valid board ID is provided.<br>
Status Code Verification: Confirm that the API returns appropriate status codes (200 OK for successful requests)<br>

**Response status code:** 200 (OK)<br>

Below you can find a picture of the API request from Postman:<be>
![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/delete%20a%20board%20request.png)<br>

**JavaScript Tests:** [delete a board tests](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/delete%20a%20board%20tests%20list.txt)

**Test Results**

![image]([https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/update%20a%20board%20tests.png](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/delete%20a%20board%20tests.png))<br>

********

<h2>Execution report for the created API collection</h2>

Below you can find the execution report generated through the Postman collection runner. <br>

**POSTMAN Execution Report**<be>

![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/postman_report1.png)
![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/postman_report2.png)
![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/postman_report3.png)

The collection was also run through Newman directly from the terminal, and the results can be found below:<br>

**Newman Execution report**<be>

![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/raport_newman1.png)
![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/raport_newman2.png)
![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/raport_newman3.png)
![image](https://github.com/Dragosne/TM-Projects/blob/main/API%20Postman/Project_files/raport_newman4.png)

<h2> No Defects found</h2>

Fortunately, during the execution of our tests using Postman, we did not encounter any defects or issues. The application appears to be stable, and all the requests we made functioned as expected. It's reassuring to see that the API endpoints we tested are robust and reliable.

<h2>Conclusions</h2>

In conclusion, our testing endeavors have traversed a substantial array of scenarios, encapsulating a significant portion of the application's pivotal functionalities. Nearly all proposed tests were meticulously crafted and executed with precision, culminating in an expansive coverage of our initial testing objectives.

Throughout our testing journey, we observed occasional fluctuations in server response times, albeit within manageable bounds. Importantly, these fluctuations did not manifest into critical errors that could imperil the application's readiness for production deployment. Any lingering concerns regarding performance can be diligently addressed and rectified in subsequent iterations, ensuring an unwavering commitment to delivering a seamless and expeditious user experience.

While we have diligently covered the majority of critical application actions, the quest for comprehensive testing is an ongoing endeavor. As such, there remains an ever-present opportunity to explore and scrutinize additional facets of the application, a prospect that we shall ardently embrace in future testing endeavors.


