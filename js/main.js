let tentativas = 3
let senha = prompt("Digite a sua senha: ")
console.log(`A sua senha e essa ${senha}`)

let entrar = prompt("Coloque a sua senha: ")

while (tentativas > 0) {
    if (entrar !== senha) {
        tentativas = tentativas - 1
        alert("Senha incorreta! Você tem " + tentativas + " tentativas restantes.")
        console.log(`Você tem ${tentativas} se erra mais senha sua senha vai ser bloqueada`)
        entrar = prompt("Coloque a sua senha: ")
    } else if (tentativas === 0) {
        alert("Você não tem mais tentativas restantes. Acesso negado.")
        console.log("Acesso negado.")
        break
    } else {
        alert("Senha correta! Bem-vindo!")
        console.log("Acesso permitido.")
        break }
    }