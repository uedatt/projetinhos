function mostraPoke(){
    const nome = document.getElementById('pokename').value
    var token = `https://pokeapi.co/api/v2/pokemon/${nome}`
    request(token)
}

function request(token){
    fetch(token).then((res)=> res.json()).then((dados)=>{
        const id = dados.id
        var atk1 = dados.moves['0']['move']['name']
        var atk2 = dados.moves['1']['move']['name']
        var tipo1 = dados.types['0']['type']['name']
        pokeimage(id)
        document.getElementById('idpoke').innerHTML = `O numero na pokedex é: ${id}`
        document.getElementById('atks').innerHTML = `O primeiro ataque é : ${atk1} e o segundo é : ${atk2} e os tipos são:`
        document.getElementById('tipo1').innerHTML = tipo1

        

    })}

function pokeimage(id){
    var image = `https://pokeapi.co/api/v2/pokemon-form/${id}/`
    fetch(image).then((resposta)=> resposta.json()).then((anws)=>{
        var sprite = anws.sprites['front_default']
        document.getElementById("imgapi").src = sprite

    })

    
    }




document.getElementById('consulta').addEventListener('click',mostraPoke)

//https://pokeapi.co/api/v2/pokemon-form/94/