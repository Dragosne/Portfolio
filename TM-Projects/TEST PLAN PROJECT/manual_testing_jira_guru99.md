<h1>TESTING PROJECT</h1>

<h1>for IT Factory Manual Testing Course</h1>

The scope of the final project for the ITFactory Manual Testing Course is to use all gained knowledge through the course and apply it in practice, using a live application

Application under test: [Guru99 Banking WebApp](https://demo.guru99.com/V4/index.php)

Tools used: Jira, Zephyr Squad.

<h1>INTRODUCTION</h1>

This test plan describes the methods and procedures that will be used in the testing process of the project.
The objective of the testing activities is to check the functions and features provided by the guru99 net banking facilities offered to its customers aiming to enhance trust in the quality of the product as much as possible before the application release. 

The purpose of this testing plan is to be used and followed during the testing process and to identify which items and features will be tested, the types of testing that will be performed, the resources and the personnel required for the testing process, the associated risks, and the schedule to complete the testing process.

## FUNCTIONAL SPECIFICATIONS OF PROJECT

The following stories were created in Jira and describe the functional specifications of the "**New Customer, Edit Customer, and Delete Customer**" modules, for which the final project is performed.

![image](https://github.com/Dragosne/Manual-Testing-Portfolio/blob/main/TEST%20PLAN%20PROJECT/ProjectImages/Jira%20specificattions.jpg) <be>


[**Edit Customer Story**](https://github.com/Dragosne/Manual-Testing-Portfolio/blob/main/TEST%20PLAN%20PROJECT/ProjectImages/story%20edit%20customer.png)<br>
[**Delete Customer**](https://github.com/Dragosne/Manual-Testing-Portfolio/blob/main/TEST%20PLAN%20PROJECT/ProjectImages/story%20delete%20customer.png)<br>

### COMPLETE GURU99 BANKING SOFTWARE REQUIREMENTS SPECIFICATIONS

For complete "**Documentation**" please, click here: [**Guru99-SRS_v1.3**](https://github.com/Dragosne/TM-Projects/blob/main/TEST%20PLAN%20PROJECT/ProjectImages/Guru99%20Banking%20SRS_v1.pdf)

## PROJECT RELEASE

Here you can find the release that was created for this project:

![image](https://github.com/Dragosne/Manual-Testing-Portfolio/blob/main/TEST%20PLAN%20PROJECT/ProjectImages/release.png)

<h1>TESTING PROCESS</h1>

The testing process was conducted according to the standard procedures outlined below.

## TEST PLANNING

The Test Plan details the testing procedures for the "New Customer, Edit Customer, and Delete Customer" modules of the Guru99 Banking WebApp.

The plan specifies the items and features to be tested, the types of testing to be performed, the personnel responsible, the resources and schedule needed for completion, and the associated risks.

### ROLES ASSIGNED TO THE PROJECT AND PERSONS ALLOCATED

<ul>
  <li>Project manager: John Smith </li> 
  <li>Product manager: Krishna Rungta</li>
  <li>Software developer: Tom Patrick</li>
  <li>QA Engineer: Dragos Nechifor</li>
</ul>

### TEST CRITERIA

The conditions under which testing is conducted and the expected outcomes during test execution are described below:
- Execute each use case, use-case flow, or function using valid and invalid data.
- Verify that the expected results occur when valid data is used.
- Ensure appropriate error or warning messages are displayed when invalid data is used.
- Confirm that each rule is properly applied.

These criteria ensure comprehensive coverage of the system's functionality and validate that the application behaves as expected under various conditions. We aim to identify and resolve issues before the release, ensuring a robust and reliable application for end-users.

#### ENTRY CRITERIA 

The following conditions must be met before we start testing to ensure everything runs smoothly and effectively:
- The application construction is complete, with all planned features and functionalities.
- The server is functional, and the web banking application is available for testing.
- All necessary devices, instruments, and other equipment are acquired and set up.
- The test environment is prepared, including software and hardware configurations, and the application is deployed to this environment.
- The test specification is created and approved, detailing the test cases, procedures, and scenarios.
- All dependencies, such as third-party services or integrations, are available and functioning correctly.
- The testing team is briefed and understands the scope, objectives, and procedures.
- Required test data is prepared and validated to ensure it represents both typical and edge-case scenarios.
 
Meeting these criteria ensures that we can start testing without any issues.

#### EXIT CRITERIA

To conclude testing, the following conditions must be met:
- all the tests have been executed
- At least 90% of tests have passed successfully.
- Any critical or major bugs identified during testing have been fixed promptly and retested.
- Any remaining open bugs are not critical or major and are acceptable for release.
- Clear documentation of any remaining issues and plans for addressing them in future releases.

Meeting these standards ensures the software is ready for deployment and use, providing confidence in its reliability and functionality.

#### SUSPENSION CRITERIA 

The following criteria have been established to guide the suspension of testing, ensuring that any unexpected issues or changes are addressed promptly and appropriately before proceeding further:
- If the web server hosting the Guru99 application experiences instability or downtime, which could compromise the reliability of test results.
- If a significant portion (e.g., 40%) of test cases fail, indicating potential systemic issues within the Guru99 application that require investigation and resolution by the development team.
- In the event of unexpected critical errors or major issues arising during testing that were not anticipated in the initial test plan.
- If there are significant changes in application requirements or code during testing, necessitating a reassessment of testing procedures and potential suspension to evaluate the impact of these changes.
- If critical testing resources become unavailable, such as access to essential data or specialized equipment, requiring a temporary halt until these resources are accessible again.

These criteria ensure that testing is conducted effectively, allowing for the prompt identification and resolution of any issues or changes that may impact the quality and reliability of the Guru99 banking application.

### TEST SCOPE

#### TESTS IN SCOPE

- To ensure comprehensive coverage, all features of the New Customer, Edit Customer, and Delete Customer modules, as defined in the Guru99 business requirements, will undergo functional and GUI testing.
- The functionality of adding a new customer will be tested to ensure accurate data capture and validation.
- Error handling for duplicate Email IDs will be verified to maintain data integrity.
- Testing will validate the registration process for new customers to ensure seamless access to Guru99 Bank services.
- Compatibility testing will be conducted to ensure the banking site functions correctly on supported browsers.

#### TESTS NOT IN SCOPE

- Non-functional testing, such as stress and performance testing, falls outside the scope of this project and will not be included in the testing efforts.
- Automation testing is not within the scope of this project and will not be implemented.
- QA support for mobile applications is not provided. Testing efforts will focus solely on web applications developed for Guru99 Bank.

#### ADDITIONAL ELEMENTS

- Test Prioritization: Tests will be prioritized based on their impact on critical functionalities and business requirements to focus testing efforts effectively.
- Required Resources: Necessary resources, including equipment, testing environment setup, and personnel, will be identified and allocated for testing activities.
- Testing Schedule: A detailed testing schedule will be established to ensure timely testing activities align with project timelines.
- Reporting and Communication: Protocols for reporting test results and communicating with stakeholders will be established to ensure transparency and accountability in testing activities.

### RISKS DETECTED

#### PROJECT RISKS:

- A tight project schedule may result in rushed testing activities and compromised quality.
- Limited availability of key team members due to other project commitments may impact project progress and continuity.
- Ambiguity or frequent changes in project requirements may lead to scope creep and project delays.
- Dependence on third-party vendors or external services may introduce delays or compatibility issues.

#### PRODUCT RISKS:

- Server stability risks (crashes, disconnects, etc.) may disrupt testing and user experience.
- Usability issues with the Guru99 Bank App may lead to customer dissatisfaction and decreased adoption.
- Limited computer knowledge among some Guru99 Bank users may result in usability challenges and support issues.
- Stringent validation constraints on fields may lead to user frustration and abandonment.
- Data validation errors could compromise the integrity and accuracy of user data.
- Compatibility issues with new browser versions may affect the accessibility and functionality of the application.
- Security vulnerabilities could compromise the confidentiality and integrity of user information.

#### EVALUATING ENTRY CRITERIA

The entry criteria defined in the Test Planning phase have been achieved and the test process can continue.

*********************

### TEST MONITORING AND CONTROL

The monitoring and control phase was initiated to ensure effective oversight of the testing process and project progress. 
Weekly reports were intended to be generated to provide insight into the following aspects:
- Progress of the testing process
- Adherence to schedule
- Project costs
- Allocation of necessary resources
- Quality level achieved

Additionally, this phase aimed to provide reasoning for the monitoring and control activities undertaken and how they were executed. 
The test status report from Zephyr - Test Metrics, specifically the first report reflecting testing activity, and evolution.

![image](https://github.com/Dragosne/Manual-Testing-Portfolio/blob/main/TEST%20PLAN%20PROJECT/ProjectImages/daily_execution_final.png)

[interim Report](https://github.com/Dragosne/Manual-Testing-Portfolio/blob/main/TEST%20PLAN%20PROJECT/ProjectImages/daily_execution_intermediary.png)

### TEST ANALYSIS

The testing process will be executed based on the application requirements.

Test conditions were defined for the following functionalities:


For each field of New Customer, Edit Customer Modules:
- Technical requirements for each field are met
- Fields functions with valid and invalid data (characters, special characters, blank, space)
- The error messages are displayed correctly
- The inserted data (valid or invalid) will be validated
- Fields length

For the entire modules:
- UI test
- The technical requirements are met
- The functional validation is met
- A new customer can be created and saved in the database
- Technical requirements for the module are met

The following test conditions were found: <br>
![image](https://github.com/Dragosne/Manual-Testing-Portfolio/blob/main/TEST%20PLAN%20PROJECT/ProjectImages/testCasesTitles.png)

### TEST DESIGN
Functional test cases were created in Zephyr Squad based on the analysis of the specifications. 
The test cases can be accessed here:<br> 
[**TEST CASES .csv**](https://github.com/Dragosne/Manual-Testing-Portfolio/blob/main/TEST%20PLAN%20PROJECT/ProjectImages/ZFJ-Cycles-02-27-2024.csv); 

### TEST IMPLEMENTATION

The following elements are needed to be ready before the test execution phase begins:

- The test cases are written for the application module to be tested
- The environment is ready to start the testing process:
   - Internet connection (good and stable; at list 5mbs specified, 15mbs at a minimum recommended),
   - Desktop or laptop computer, minimum requirements: Windows 7 or MacOS Sierra or above; 4GB RAM; CPU 3.4Ghz,
   - Google Chrome ver27 or above installed,
- The Guru99 web app server and database server are installed, available, and online,
- The credentials for app login are provided.

### TEST EXECUTION

Test cases are executed on the created test Cycle summary: **Release 3.0/Guru99 Bank Web App Testing**

Bugs have been created based on the failed tests. The complete bug reports can be found here: [**BUG REPORTS .csv**](https://github.com/Dragosne/Manual-Testing-Portfolio/blob/main/TEST%20PLAN%20PROJECT/ProjectImages/BugsDetails.csv)

The following is a summary of the bugs that have been found
![**Jira Bug List**](https://github.com/Dragosne/Manual-Testing-Portfolio/blob/main/TEST%20PLAN%20PROJECT/ProjectImages/bugList.png)

Full regression testing is needed on the impacted areas after the bugs are fixed and retesting will be done for every functionality that was previously failed.

### TEST COMPLETION

As the Exit criteria were met and satisfied as mentioned in the appropriate section, this feature is suggested to ‘Go Live’ by the Testing team

The traceability matrix was generated and can be found here: 
[**Traceability Matrix Excel file**](https://github.com/Dragosne/Manual-Testing-Portfolio/blob/main/TEST%20PLAN%20PROJECT/ProjectImages/Forward%20Traceability_27_2_2024.xlsx)
![image](https://github.com/Dragosne/Manual-Testing-Portfolio/blob/main/TEST%20PLAN%20PROJECT/ProjectImages/TraceMartrix.png)

A test execution chart was generated and can be found below. 

![image](https://github.com/Dragosne/Manual-Testing-Portfolio/blob/main/TEST%20PLAN%20PROJECT/ProjectImages/ExecutionReport.png)

The final report shows that a number of **4** tests have failed from a total of **19** tests which means a pass rate of 78.95%

A number of **10** total bugs were found, from which the priority is: **3** are high and **2** are medium.

Within the testing project, a total of 19 tests were executed, out of which 15 tests passed successfully, and 4 tests failed to meet the expected criteria. These tests covered a wide range of scenarios and functionalities defined in the project's specific requirements, achieving a pass rate of approximately 79%.

Regarding the test results, we observe that 79% of the conducted tests have passed successfully, while 21% have been deemed unsuccessful. This figure falls below the initial threshold of 90% set for test success. A detailed analysis of these results reveals that the majority of failed tests were associated with minor bugs, while a limited number of tests failed due to high-severity bugs.

Given the nature of the identified bugs and their impact on the application's functionality and quality, the development and testing team has agreed that most minor bugs can be addressed in a manner that allows the product launch under acceptable conditions. However, efforts are now focused on addressing and retesting high-severity bugs to minimize any significant risks to the application's functionality and performance.

While the current situation does not fully align with the initial thresholds set for test success, we are confident that our ongoing efforts in bug resolution and retesting will lead to adequate product quality and a successful launch.
