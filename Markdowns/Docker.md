# Docker

## Instalação
```shell 
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo docker version
```

## Repositório de Imagens Docker 
[Docker Images Hub](https://hub.docker.com)

## Comandos
Executar container (*1):```docker run (nome_do_container)``` <br>
Listar container (ativos): ```docker ps``` <br>
Listar container (todos): ```docker ps -a``` <br>
Parar container: ```docker stop (nome_do_container) ou docker stop (container_id)``` <br>
Deletar container: ```docker rm (nome_do_container)``` <br>
Listar imagens baixadas: ```docker images``` <br>
Remover imagens baixadas: ```docker rmi (nome_da_imagem):(tag, opcional)``` <br>
Dar apenas pull (sem exec): ```docker pull (nome_da_imagem)```
Manter container atrelado ao terminal: ```docker attach (container_id)``` <br>
Destacar container atrelado ao terminal (rodar no background): ```docker run -d (nome_do_container)``` <br>
Atrelar execução ao terminal do container: ```docker run -t (nome_do_container)``` <br>
Atribuir uma porta do host para comunicação com container Docker: ```docker run -p (porta_host):(porta_container) (nome_do_container)``` <br>
Atribuir uma pasta do host para comunicação com pasta do Docker: ```docker run -v (caminho_pasta_host):(caminho_pasta_container) (nome_do_container)```
Ver detalhes avançados do container (em JSON): ```docker inspect (nome_do_container)```
Ver registros (logs) de um container em background-mode: ```docker logs (nome_do_container)```
#### Obs:
(1) Docker vai dar pull do hub caso container não seja encontrado.

## Port-mapping / Port-publishing

### É a alternativa que usamos para acessar containeres através de portas. Vamos supor que ao executar um container, você obteve a seguinte mensagem: <br>
```Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)``` <br>
### Para você acessar a sua aplicação, é bastante simples, basta acessar o endereço fornecido. Porém, para um usuário acessá-la (através de um navegador, por exemplo) precisamos que exista um endereçamento para essa porta específica (caso contrário, ao tentar abrir este endereço, o usuário estará acessando seu próprio endereço local e não o container). O usuário pode acessar o endereço que é atribuído automaticamente pelo docker (IP interno), por exemplo: ```http://170.12.0.1:5000```, ainda assim, um usuário externo estará impossibilitado de acessar o endereço. Para solucionar o problema, suponha o IP da máquina que executa o Docker seja ```192.168.0.3```, podemos então mapear a porta ```6969``` para usuário que estejam na rede acessar o container, da seguinte forma:
```docker run -p 6969:5000 (nome_do_container)```
### Isso permite que o host possa executar várias instâncias de distintos containers para que eles se comuniquem, desde que cada porta seja atribuída a apenas um container de cada vez.

## Volume mapping
### É a alternativa que usamos para que o docker use o armazenamento real (do host) para salvar arquivos, facilitando o acesso do mesmo. Por exemplo, se quisermos que banco de dados de um container de mysql (que por padrão são salvos em: ```/var/lib/mysql```) sejam salvos na pasta ```~/Documents/db/``` podemos fazer:
```docker run -v ~/Documents/db:```