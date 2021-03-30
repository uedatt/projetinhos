function criaToken(){
    const cep = document.getElementById('cep').value
    const token = `https://viacep.com.br/ws/${cep}/json/`
    teste(token)

}


function teste(cep){ 
    fetch(cep).then((res)=> res.json()).then((oi)=>{
        document.getElementById('info').innerHTML = `A rua correspondente ao CEP é: ${oi.logradouro} e o estado é: ${oi.uf}`
        //document.getElementById('rua').value = oi.logradouro
    //var result = JSON.stringify(oi)
    })
    }


document.getElementById('but').addEventListener('click', criaToken)