/*Program to get data types of all in JavaScript
var inputname = "Alex";
var inputnumber = 9;
var inputcheck = true;
var inputarr = [5 ,4, 6, 8];
var inputobj = {
    name : "fox",
    type: "animal"
}
var inputvar = undefined;
var inputempty = null;


function checkTypes(){
    console.log("Type of " + inputname + " is: " + typeof(inputname));
    console.log("Type of " + inputnumber + " is: " + typeof(inputnumber));
    console.log("Type of " + inputcheck + " is: " + typeof(inputcheck));
    console.log("Type of " + inputarr + " is: " + typeof(inputarr));
    console.log("Type of " + inputobj.name + " is: " + typeof(inputobj));
    console.log("Type of " + inputvar + " is: " + typeof(inputvar));
    console.log("Type of " + inputempty + " is: " + typeof(inputempty));
}
checkTypes();
*/

//Json Interpretation
/*var library = [
    {
        title: "JavaScript",
        price: 500,
        readers: [
            {
                name: "Person 1",
                count: 300
            },
            {
                name: "Person 2",
                count: 400
            }
        ],
        authorDetails: {
            name: "Raj",
            age: 40
        }
    },
    {
        title: "Nodejs",
        price: 600,
        readers: [],
        authorDetails: {
            name: "Raj",
            age: 40
        }
    }
]
/3a
console.log(library[0].price);
/3b
console.log(library[1].authorDetails.age)
/3c
console.log(library[0].readers.length)
/3d
console.log(library[0].readers[1].count)
*/
//JSON Representation
{
    "Dimensions" = 
    {
        "Overall length(mm)": 3500,
        "Overall Width(mm)" : 1600,
        "Overall height(mm)" : 1490,
        "WheelBase(mm)" : 2360,
        "Track width(mm)" : {
            "Front(mm)" : 1405,
            "Rear(mm)" : 1400
        }
        ,"Minimum turning radius(m)": 4.5,
        "Minimum ground clearance(mm)" : 170
    }
    "Capacities" = 
    {
        "Seating capacity(persons)" : 5,
        "Fuel tank capacity(litres)" : 35
    }
    "Engine" = 
    {
        "Type" : "KB - Series",
        "Number of cylinders" : 3,
        "Number of valves" : 12,
        "Capacity(cc/cm3)" : 998,
        "Bore * Stroke(mm)" : 73.0*79.5,
        "Compression ratio": "10:1",
        "Maximum power(PS/RPM)" : "67/6200",
        "Maximum torque(Nm/rpm)" : "30/3500",
        "Fuel distribution" : "Multipoint injection",
    }
    "Transmission" = 
    {
        "Type" : "5-speed-MT"
    }
    "Chassis" = 
    {
        "Steering" : "Rack & Pinion, Power assisted",
        "Brakes":
        {
            "Front" : "Ventilated Discs",
            "Rear" : "Drums"
        }
        ,"Suspension" : 
        {
            "Front" : "MacPherson strut & coil spring",
            "Rear" : "Isolated trailing link & coil spring"
        }
        ,"Shock absorbers" : "Gas Filled",
        "Tyre(tubeless)" : "155/BOR13"
    }
    "Weights" = 
    {
        "Kerb weight (min. with full options)(kg)" : "860-880",
        "Gross vehicle weight(kg)" : 1320 
    }
}
