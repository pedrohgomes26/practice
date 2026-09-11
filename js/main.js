let idade = Number(prompt("Qual a sua idade?"));

if (idade >= 18) {
    alert("Você é maior de idade.");
} else if (idade < 18) {
    alert("Você é menor de idade.");
}

let temperatura = Number(prompt("Qual a temperatura esta agora?"));

if (temperatura <= 19) {
    alert("Ta frio");
} else if (temperatura >= 20) {
    alert("Ta normal");
} else if (temperatura >= 27) {
    alert("Ta calor");
} else if (temperatura >= 30) {
    alert("ta muito calor");
} else {
    alert("calor do cão");
}