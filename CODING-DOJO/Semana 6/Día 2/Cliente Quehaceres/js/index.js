
async function eliminaQuehacer( event, idQuehacer ){
    const URL = `http://127.0.0.1:5001/api/eliminar/quehacer/${idQuehacer}`;
    const config = {
        method : 'DELETE'
    }

    const respuesta = await fetch( URL, config );
    document.querySelector( `#id_quehacer_${idQuehacer}` ).closest('li').remove();
}

async function obtenerQuehaceres( event ){
    const URL = "http://127.0.0.1:5001/api/quehaceres";
    const config = {
        method : 'GET'
    }

    const respuesta = await fetch( URL, config );
    const data = await respuesta.json();
    
    let lista = document.querySelector( '.quehaceres' );
    lista.innerHTML = "";
    for( let i = 0; i < data.length; i ++ ){
        lista.innerHTML += `<li> 
                                ${data[i].descripcion} - ${data[i].estatus} - 
                                <button onclick="eliminaQuehacer(event, ${data[i].id})" class="eliminaQuehacer" id="id_quehacer_${data[i].id}"> Eliminar </button>
                            </li>`;    
    }
}

async function agregarQuehacer( event ){
    event.preventDefault();
    const URL = "http://127.0.0.1:5001/api/quehacer/nuevo";
    const datos = {
        "descripcion" : document.querySelector( '#descripcion' ).value,
        "estatus" : document.querySelector( '#estatus' ).value,
        "id_usuario" : document.querySelector( '#id_usuario' ).value, 
    }
    const config = {
        method : "POST",
        body : JSON.stringify( datos ),
        headers : {
            'Content-type' : 'application/json'
        }
    };

    const respuesta = await fetch( URL, config );
    const data = await respuesta.json();
    console.log( data );

}