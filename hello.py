const prompt = require("prompt-sync")(); //Importing the prompt-sync module

// Asking the user to enter an operator (+, -, *, or /)
const operator = prompt('Enter operator (either +,-,* or /): ');

// Asking the user to enter two numbers
let num1 = parseFloat(prompt("Enter number 1: "));
let num2 = parseFloat(prompt("Enter number 2: "));
let result;

//Using a switch statement to perform the operation
switch (operator) 
{
    case '+':
        result = num1 + num2;
        break;
    case '-':
        result = num1 - num2;
        break;
    case '*':
        result = num1 * num2;
        break;
    case '/':
        if (num2 === 0){
            console.log("Division by zero is not allowed. ");
            Process.exit(1);
        }
        result = num1 / num2;
            break;
        default:
                console.log("Invalid operator. Please enter a valid operator (+,-,* or /).");
                Process.exit(1);
            }

    if (result !== undefined)
    {
        console.log('Result:${result} ');

    }

