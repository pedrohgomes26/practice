import promptSync from "prompt-sync";
const prompt = promptSync();

let num1 = Number(prompt("coloque um numero: "));
let num2 = Number(prompt("coloque outro numero: "));

let op = prompt("coloque qual conta quer fazer: ")
let resultado = 0

if (op == "+") {
    resultado = num1 + num2
} else if (op == "-") {
    resultado = num1 - num2
} else if (op == "*") {
    resultado = num1 * num2
} else if (op == "/") {
    resultado =num1 / num2
}

console.log("O resultado da sua conta é: " + resultado)