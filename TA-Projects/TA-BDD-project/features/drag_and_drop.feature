Feature: Drag and Drop action on the horokuapp webpage
@drag_and_drop
  Scenario: Testing the drag and drop functionality
    Given Navigate to the Drag&Drop webpage
    Then Initial state is: the source object is "A" and the target object is "B"
    When First Action: Drag the source object A and drop it to the target object B
    Then Check status after first action: First object is "B" and second object is "A"
    When Second action: Drag the source object B and drop it to the target object A
    Then Check status after second action: First object is "A" and second object is "B"

