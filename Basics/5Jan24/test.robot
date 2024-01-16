*** Settings ***

Library Selenium2Library

*** Variables ***
${HOMEPAGE} http://www.google.com
${BROWSER} Chrome

*** Test Cases ***

Open Browser
    o