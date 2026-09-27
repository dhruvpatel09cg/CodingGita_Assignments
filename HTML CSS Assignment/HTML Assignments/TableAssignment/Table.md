## Answers:
---
```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Table Assignment</title>
</head>
<body>
    <h2 align="center">Table Assignment</h2>
    <h3>Date: 16 August, 2026</h3>
    <h3>Q: 01</h3>
        <table border="1">
            <tr>
                <th>Course Name</th>
                <th>Duration</th>
            </tr>
            <tr>
                <td>Web Development</td>
                <td>4 months</td>
            </tr>
            <tr>
                <td>Data Analytics</td>
                <td>5 months</td>
            </tr>
        </table>
    <br>
    <h3>Q: 02</h3>
        <table border="1">
            <caption>Monthly Workshop Schedule</caption>
            <tr>
                <th>Workshop</th>
                <th>Month</th>
            </tr>
            <tr>
                <td>UI/UX design</td>
                <td>September</td>
            </tr>
            <tr>
                <td>DSA</td>
                <td>November</td>
            </tr>
        </table>
    <br>
    <h3>Q: 03</h3>
        <table border="1">
            <tr>
                <th colspan="2">Institute programs</th>
            </tr>
            <tr>
                <td>MERN stack development</td>
                <td>Full stack development</td>
            </tr>
        </table>
    <br>
    <h3>Q: 04</h3>
        <table border="1">
            <tr>
                <td rowspan="2">Programming track</td>
                <td>Semester 1</td>
            </tr>
            <tr>
                <td>Semester 2</td>
            </tr>
        </table>
    <br>
    <h3>Q: 05</h3>
        <table border="1">
            <caption>Student Performance Report</caption>
            <thead>
                <tr>
                    <th>Student name</th>
                    <th>Grade</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Dhruv Patel</td>
                    <td>10.0 CGPA</td>
                </tr>
                <tr>
                    <td>Parv Patel</td>
                    <td>10.0 CGPA</td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <td colspan="2">End of report</td>
                </tr>
            </tfoot>
        </table>
    <br>
    <h3>Q: 06</h3>
        <table border="1">
            <tr>
                <th scope="col">Name</th>
                <th scope="col">Age</th>
                <th scope="col">City</th>
            </tr>
            <tr>
                <td>Dhruv</td>
                <td>17</td>
                <td>Visnagar</td>
            </tr>
            <tr>
                <td>Rudra</td>
                <td>18</td>
                <td>Mehsana</td>
            </tr>
        </table>
     <br>
    <h3>Q: 07</h3>
        <table border="1">
            <tr>
                <th scope="row">Course</th>
                <td>Communication skills</td>
            </tr>
            <tr>
                <th scope="row">Duration</th>
                <td>6 Months</td>
            </tr>
            <tr>
                <th scope="row">Mode</th>
                <td>Online</td>
            </tr>
        </table>
     <br>
    <h3>Q: 08</h3>
        <table border="1">
            <tr>
                <th id="subject">Subject</th>
                <th id="marks">Marks</th>
                <th id="result">Result</th>
            </tr>
            <tr>
                <td headers="subject">Git</td>
                <td headers="marks">97</td>
                <td headers="result">Pass</td>
            </tr>
            <tr>
                <td headers="subject">Figma</td>
                <td headers="marks">98</td>
                <td headers="result">Pass</td>
            </tr>
        </table>
     <br>
    <h3>Q: 09</h3>
        <table border="1">
            <caption>Department Summary</caption>
            <thead>
                <tr>
                    <th scope="col">Buildings</th>
                    <th scope="col">Apps</th>
                    <th scope="col">Machine</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Civil Dep.</td>
                    <td>Computer Dep.</td>
                    <td>Mechanical Dep.</td>
                </tr>
                <tr>
                    <td>Closed</td>
                    <td>Open</td>
                    <td>Closed</td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <td colspan="3">End of Summary</td>
                </tr>
            </tfoot>
        </table>
     <br>
    <h3>Q: 10</h3>
        <table border="1">
            <caption>Availble Cars</caption>
            <thead>
                <tr>
                    <th scope="col" id="name">Car Name</th>
                    <th scope="col" id="brand">Brand</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td headers="name">Amaze</td>
                    <td headers="brand" rowspan="2">Honda</td>
                </tr>
                <tr>
                    <td headers="name">City</td>
                </tr>
                <tr>
                    <td headers="name">Verna</td>
                    <td headers="brand">Hyundai</td>
                </tr>
                <tr>
                    <td headers="name">Slavia</td>
                    <td headers="brand" rowspan="2">Skoda</td>
                </tr>
                <tr>
                    <td headers="name">Kushaq</td>
                </tr>
            </tbody>
            <tfoot>
                <td colspan="2">Take on Rent</td>
            </tfoot>
        </table>
     <br>
    <h3>Q: 11</h3>
        <table border="1">
            <caption>Weekly Class Schedule</caption>
            <tr>
                <th>Day</th>
                <th>Subjects</th>
            </tr>
            <tr>
                <th rowspan="3">Monday</th>
                <td>JavaScript</td>
            </tr>
            <tr>
                <td>HTML</td>
            </tr>
            <tr>
                <td>CSS</td>
            </tr>
        </table>
     <br>
    <h3>Q: 12</h3>
        <table border="1">
            <tr>
                <th colspan="3">Course Comparision</th>
            </tr>
            <tr>
                <th>Category</th>
                <th>Course</th>
                <th>Value</th>
            </tr>
            <tr>
                <th rowspan="2">Duration</th>
                <td>HTML</td>
                <td>2 months</td>
            </tr>
            <tr>
                <td>Figma</td>
                <td>3 months</td>
            </tr>
            <tr>
                <th rowspan="2">fees</th>
                <td>HTML</td>
                <td>₹10,000</td>
            </tr>
            <tr>
                <td>Figma</td>
                <td>₹15,000</td>
            </tr>
        </table>
     <br>
    <h3>Q: 13</h3>
        <table border="1">
            <caption>Internal Assesment Marks</caption>
            <thead>
               <tr>
                    <th scope="col">Name of Student</th>
                    <th scope="col">Marks</th>
               </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Raj</td>
                    <td>20</td>
                </tr>
                <tr>
                    <td>Zeel</td>
                    <td>20</td>
                </tr>
                <tr>
                    <td>Jeel</td>
                    <td>20</td>
                </tr>
            </tbody>
            <tfoot>
                <td colspan="2">Avg = 20</td>
            </tfoot>
        </table>
     <br>
    <h3>Q: 14</h3>
        <table border="1">
            <tr>
                <th scope="col">Sport</th>
                <th scope="col" id="cap">Captain</th>
                <th scope="col" id="vc">Vice Captain</th>
            </tr>
            <tr>
                <th scope="row" id="cricket">Cricket</th>
                <td headers="cap cricket">Dhruv</td>
                <td headers="vc cricket">Zeel</td>
            </tr>
            <tr>
                <th scope="row" id="volley">Volleyball</th>
                <td headers="cap volley">Rudra</td>
                <td headers="vc volley">Jeel</td>
            </tr>
        </table>
     <br>
    <h3>Q: 15</h3>
        <table border="1">
            <caption>Short Summary</caption>
            <thead>
                <tr>
                    <th colspan="2" scope="col">Name</th>
                    <th scope="col">Marks</th>
                    <th>Institute</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Dhruv</td>
                    <td>Om</td>
                    <td>98</td>
                    <th rowspan="2">CodingGita</th>
                </tr>
                <tr>
                    <td>xyz</td>
                    <td>pqr</td>
                    <td>94</td>
                </tr>
            </tbody>
            <tfoot>
                <th colspan="4">Toppers</th>
            </tfoot>
        </table>
</body>
</html>
```
