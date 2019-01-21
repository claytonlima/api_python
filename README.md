# Configuração do Projeto #
<ol>
    <li>Necessário ter instalado o python 3.6</li>
    <li>Necessário ter instalado o pip</li>
    <li>Instalar o pipenv utilizando o pip ( pip install pipenv )</li>
    <li>No diretório do projeto, instalar as denpedências do projeto ( pipenv install )</li>
    <li>Ativar o ambiente virtual necessário estar na pasta do projeto( pipenv shell )</li>
    <li>Ativar a api no diretório do projeto ( python api )</li>
</ol>

**Recomendações:**
<ol>
    <li>Se possivel utilize a IDE PyCharm</li>
    <li>Se possivel utilize o PostMan para as requisiçoes</li>
 </ol>
<br />

**Apis sobre Tipos de caminhões:**

**http://127.0.0.1:8080/alltypesoftrucks**
<br />
Lista todos os tipos de caminhões cadastrados

**http://127.0.0.1:8080/typeoftruck/add**
<br />
Adiciona um novo tipo de caminhão é apenas necessário passar truck_name = nome do caminhão**

**http://127.0.0.1:8080/typeoftruck/update**
<br />
Altera registro do caminhão é apenas necessário passar truck_name = nome do caminhão

**http://127.0.0.1:8080/typeoftruck/del/:id**
<br />
Deleta o registro, necessário passar o id do tipo de caminhão que será deletado
<br />
<br />
**Apis sobre Motoristas:**
<br />
<br />
**http://127.0.0.1:8080/driver/list/:id**
<br />
Exibi sobre o motorista -> Id, nome, origem e destino
<br />
<br />
**http://127.0.0.1:8080/driver/listalldrivers**
<br />
Exibi sobre os motoristas -> Id, nome, origem e destino
<br />
<br />
**http://127.0.0.1:8080/driver/vehiclenotloaded**
<br />
Exibi os motoristas que não estão com o caminhão carregado
<br />
<br />
**http://127.0.0.1:8080/driver/ownvehicle**
<br />
Exibi os motoristas que tem veículo próprio
<br />
<br />
**http://127.0.0.1:8080/driver/notownvehicle**
<br />
Exibi os motoristas que não tem veículo próprio

**Observação:**
No projeto já tem uma cópia do banco, utilizado para desenvolvimento e testes da api
<br />
Caso queira deletar o banco da pasta database e inserir os dados novamenete nas tabelas, temos dois métodos para auxilia-lo
<br />
**http://127.0.0.1:8080/typeoftruck/addMock**
<br />
Tabela de tipos de caminhões, insere cincos tipos de caminhões na tabela -> trucks_types
<br />
**http://127.0.0.1:8080//driver/addMock**
<br />
Tabela de motoristas, insere cincos motoristas na tabela -> drivers
