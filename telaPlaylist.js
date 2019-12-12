const axios = require('axios');
var info;

criarPlaylist = async (nome) => {
    var user = '';
    var token = '';
    

    await axios({
      url: `https://api.spotify.com/v1/users/${user}/playlists`,
      method: 'get',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      }
    }).then(     
      function(response){ 
      info = response; 
      var idPlaylists = [];
      response.data.items.forEach(element => {
          idPlaylists.push(element.id);
          console.log(idPlaylists[idPlaylists.length-1]);
      });
      /*
      for(let i = 0; i < response.data.items.length; i++){
        idPlaylists[i] = response.data.items[i].id;
        // Salva o id de 20 playlists que foram solicitadas
        console.log(idPlaylists[i]);
      }
      */
    }
    ).catch(function (err){
        console.log(err);
    })
    //console.log(info.data.items);
}
    
criarPlaylist('');

// Lembrar de pegar o user id
// Lembrar de pegar o token id (em: https://developer.spotify.com/console/get-playlist-tracks/, por exemplo, para pegar as musicas de uma playlist)
