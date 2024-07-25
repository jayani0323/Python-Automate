Feature: search_for_course

  Scenario Outline: search_python_course
     Given we go to elearning.lk site
      When we search for "<search_text>" in serach bar and click search
      Then we should redirect to the python course results page
      Examples:
        | search_text|
        | Python Course|