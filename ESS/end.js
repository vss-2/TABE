var canvas = document.getElementById("meuCanvas");
canvas.onmousedown = myDown;
canvas.onmouseup = myUp;
var ctx = canvas.getContext("2d");
var rect = canvas.getBoundingClientRect();
var checkPoint = document.getElementsByName("PoCo");
var matriz = [];
var matrizaux = [];
var comecoBool;
var retaSelect = 0;
var avaliat = 15;
var dragok = false;
var lastX;
var lastY;
var pontoNovos = [];

var rmPonto = false;
var mkPonto = false;

var actualCurve;
var actualPoint;

function moverCurva(e) {
    if (dragok) {
        matriz[actualCurve][actualPoint * 2] = e.pageX - canvas.offsetLeft;
        matriz[actualCurve][(actualPoint * 2) + 1] = e.pageY - canvas.offsetTop;
        redesenharTudo();
    }
}

function myDown(e) {
    if (mkPonto) inserirPonto();
    if (rmPonto) removerPonto();
    for (var j = 0; j < matriz.length; j++) {
        var arraux = matriz[j];
        for (var i = 0; ((i * 2) + 1) < arraux.length; i++) {
            let x = arraux[i * 2];
            let y = arraux[(i * 2) + 1];
            
            if (e.pageX < x + 5 + canvas.offsetLeft && e.pageX > x - 5 +
                canvas.offsetLeft && e.pageY < y + 5 + canvas.offsetTop &&
                e.pageY > y - 5 + canvas.offsetTop) {
                actualCurve = j
                actualPoint = i;
                arraux[i * 2] = e.pageX - canvas.offsetLeft;
                arraux[(i * 2) + 1] = e.pageY - canvas.offsetTop;
                dragok = true;
                canvas.onmousemove = moverCurva;
            }
        } 
    }
}

function myUp() {
    dragok = false;
    canvas.onmousemove = null;
}

function mudou(){
    avaliat = document.getElementById("numAvaliacao").value;
    redesenharTudo();
}

function criandoReta(){
	if (document.getElementById("inserirP").checked == true){
        matriz[retaSelect].push(event.clientX-rect.left);
        matriz[retaSelect].push(event.clientY-rect.top);
        console.log("Entrei aqui");
        //document.getElementById("inserirP").checked = false;
		mkPonto = false;
		return;
	}
    if(comecoBool){
        matrizaux.push(event.clientX-rect.left);
        matrizaux.push(event.clientY-rect.top);
        drawPointAoVivo();
    }
}

function comeco(){
    // Vemos se devemos inserir na curva ou parar a inserção
    if(!comecoBool){    
        document.getElementById("criar").innerHTML = "Parar Curva";
        comecoBool = true;
    } else {
        document.getElementById("criar").innerHTML = "Nova Curva"; 
        comecoBool = false;
        if(matrizaux.length > 0){
            matriz.push(matrizaux);
        }
        matrizaux = [];
        redesenharTudo();
    }
}

function apagarReta(){
    // Apagamos a reta
    matriz.splice(retaSelect, 1);
    if(retaSelect > matriz.length-1){
        retaSelect--;
    }
    if(retaSelect < 0){
        retaSelect = 0;
    }
    redesenharTudo();
}

function anteriorReta(){
    // Função de voltar a reta selecionada
    if(retaSelect > 0){
        retaSelect--;
        redesenharTudo();
    }
}

function proximaReta(){
    // Função de avançar a reta selecionada
    if(retaSelect < matriz.length - 1){
        retaSelect++;
        redesenharTudo();
    }
}

function drawPointAoVivo(){
    // Desenha ponto "ao vivo", ou seja, no momento que você clica
    var checkPoint = document.getElementsByName("PoCo");
    if(checkPoint[0].checked){
        var arraux = matrizaux;
        for(var i = 0; ((i*2)+1)<arraux.length;i++){
            ctx.beginPath();
            ctx.arc(arraux[i*2],arraux[(i*2)+1],5, 0, 2 * Math.PI);
            ctx.fillStyle = '#000000';
            // Ponto desenhado na cor preta
            ctx.fill();
            ctx.stroke();
        }
    }
}

function drawPoint(){
    var checkPoint = document.getElementsByName("PoCo");
    if(checkPoint[0].checked){
        for(var j = 0; j<matriz.length;j++){
            var arraux = matriz[j];
            if(retaSelect == j){
                for(var i = 0; ((i*2)+1)<arraux.length;i++){
                    ctx.strokeStyle = '#900C3E';
                    ctx.beginPath();
                    ctx.arc(arraux[i*2],arraux[(i*2)+1],5, 0, 2 * Math.PI);
                    ctx.fillStyle = '#900C3E';
                    ctx.fill();
                    ctx.stroke();
                    // Pintar o ponto na cor vinho
                }
            } else {
                for(var i = 0; ((i*2)+1)<arraux.length;i++){
                    ctx.strokeStyle = '#000000';
                    ctx.beginPath();
                    ctx.arc(arraux[i*2],arraux[(i*2)+1],5, 0, 2 * Math.PI);
                    ctx.fillStyle = '#000000';
                    ctx.fill();
                    ctx.stroke();
                    // Pintar ponto não selecionado na cor preta
                } 
            }
        }
    }
}

function drawLine(){
    var checkPCtrl = document.getElementsByName("PoCu"); 
    if(checkPCtrl[0].checked){
        for(var j = 0; j<matriz.length;j++){
            var arraux = matriz[j];
            ctx.moveTo(arraux[0],arraux[1]);
            if(retaSelect === j){
                ctx.strokeStyle = '#FFC300';
                ctx.beginPath();
                for(var i = 0; ((i*2)+1) < arraux.length;i++){
                    ctx.lineTo(arraux[i*2],arraux[(i*2)+1]);
                    ctx.stroke();
                }
                // Reta selecionada na cor amarela
            } else {
                ctx.strokeStyle = '#000000';
                ctx.beginPath();
                for(var i = 0; ((i*2)+1) < arraux.length;i++){
                    ctx.lineTo(arraux[i*2],arraux[(i*2)+1]);
                    ctx.stroke();
                }
                // Reta não-selecionada na cor preta 
            }
        }
    }
}

function bezier(t,arr){
    var n = arr.length/2;   
    // Tamanho da reta
    var aupx = [];
    var bezierPontos = [];

    for(var k = 0; (k*2) < arr.length;k++){
        aupx.push(Math.floor(arr[k*2]));
    }

    var aupy = [];
    for(var k = 0; ((k*2)+1) < arr.length; k++){
        aupy.push(Math.floor(arr[(k*2)+1]));
    }

    for(var k = 1; k <= n; k++){
        for(var p = 0; p <= (n-k)-1; p++){
            aupx[p] = (1-t)*aupx[p] + t*aupx[p+1];
            aupy[p] = (1-t)*aupy[p] + t*aupy[p+1];
        }
    }
    bezierPontos.push(aupx[0]);
    bezierPontos.push(aupy[0]);
    return bezierPontos;
}

function deCasteljau(){
    var checkCurve = document.getElementsByName("Cur");
    var pointes = [];
    if(checkCurve[0].checked){
        for(var j = 0; j < matriz.length; j++){
            var c = document.getElementById("meuCanvas");
            var ctx = c.getContext("2d");
            var arraux = matriz[j];
            ctx.beginPath();
            ctx.moveTo(arraux[0],arraux[1]);
            for(var i = 0; i <= 1; i+=(1/avaliat)){
                pointes = bezier(i,arraux);
                if(retaSelect === j){
                    ctx.strokeStyle = '#FF5733';
                    ctx.lineTo(pointes[0],pointes[1]);
                    ctx.stroke();
                } else {
                    ctx.strokeStyle = '#000000';
                    ctx.lineTo(pointes[0],pointes[1]);
                    ctx.stroke();
                }
            }
            if(retaSelect === j){
                ctx.strokeStyle = '#FF5733';

                ctx.lineTo(arraux[arraux.length-2],arraux[arraux.length-1]);
                ctx.stroke();
            } else {
                ctx.strokeStyle = '#000000';
                ctx.lineTo(arraux[arraux.length-2],arraux[arraux.length-1]);
                ctx.stroke();
            }
        } 
    }
}

function redesenharTudo(){
    if(!comecoBool){
        ctx.fillStyle = "#FFFFFF";
        ctx.beginPath();
        ctx.fillRect(0,0,1000,400);
        ctx.stroke();
        drawLine();
        drawPoint();
        deCasteljau();
        ctx.strokeStyle = '#000000';
        // A cada mexida que dá no código,
        // temos que refazer todos os elementos
    }
}

function alteraPonto(){
    if(rmPonto || mkPonto){                                         		 // Se um dos dois tiver apertado 
        if(rmPonto ^ mkPonto){                                      		 // XOR: Mas nao os dois apertados ao mesmo tempo
            if(rmPonto){                                           			 // Se for o remover que estiver apertado   
				let rmvString = document.getElementById("removerV").value;   // Pega o valor do textfield remover ponto
                //document.getElementById("removerP").innerHTML = rmv;
                console.log(matriz[retaSelect]);
                console.log("Tentando remover o ponto (x,y):", matriz[retaSelect][rmvString-1],matriz[retaSelect][rmvString]);
                if(rmvString > -1 && rmvString < matriz[retaSelect].length/2){
                    matriz[retaSelect].splice(rmvString*2, 2);                 // dada a rmPosicao, removo 2 itens a partir dela = remove x e depois y
                    console.log(matriz[retaSelect]);
                    redesenharTudo();
                    let rmv = "Removido ponto " + rmvString + "!";
                    alert(rmv);
                    console.log(rmv);
                    document.getElementById("removerV").value = -1;
                    //document.getElementById("removerP").innerHTML = "Remover Ponto";
                } else {
                    alert("Erro: tu deve ter tentado remover onde não existe nada!");
                }
                
                rmPonto = false;
            }
            else{
                let insString = document.getElementById("inserirV").value;
                
                let xClick = pontoNovos[0];		// Pega o posição X
				let yClick = pontoNovos[1];		// Pega o posição Y
                
                console.log(xClick, yClick);
                
				if(insString == -1){
					matrizaux.push(xClick);					// Se for posição -1, como dito na Obs, coloco no fim
					matrizaux.push(yClick);
				} else {
					var matrizTemp = matrizaux;									// Copio a matrizaux usada em drawPointAoVivo
					var matrizTempFim = matrizTemp.slice(insString);			// Corto a matrizaux de onde o cara quer botar o ponto até o fim
					if(insString != 0){											// Caso ele não queira colocar no lugar do primeiro
						matrizTempInicio = matrizTemp.slice(0, insString-1);	// Corto do começo 0 até n-1: onde o cara quer inserir
						matrizTempInicio.push(xClick);							// Insiro no lugar N do array o ponto clicado na tela
						matrizTempInicio.push(yClick);							
						matrizTemp = matrizTemp.concat(matrizTempInicio, matrizTempFim); // Concateno os arrays
					} 
					matrizaux = matrizTemp;
				}
                let ins = "Inserido ponto " + insString + "!";
                alert(ins);
                redesenharTudo();
                document.getElementById("inserirP").innerHTML = "Inserir Ponto";
                //mkPonto = false;
            }
        } return;
    }
    return;
}

function inserirPonto(){
    mkPonto = true; 
    // Altera temporariamente para 
    // continuar adicionando ponto
}

function removerPonto(){
    rmPonto = true;
    alteraPonto();
    rmPonto = false;
    // Altera temporariamente para
    // remover um ponto selecionado
}
