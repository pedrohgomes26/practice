let tentativas = 3
let senha = prompt("Digite a sua senha: ")
console.log(senha)

let entrar = prompt("Coloque a sua senha: ")

while (tentativas > 0) {
    if (entrar !== senha) {
        tentativas = tentativas - 1
        alert("Senha incorreta! Você tem " + tentativas + " tentativas restantes.")
        entrar = prompt("Coloque a sua senha: ")
    } else {
        alert("Senha correta! Bem-vindo!")
        break
    }
}