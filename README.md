# Configuração do Projeto #

Será necessário ter instalado o python 3.6
<br />
Ter o pipenv para instalado para instalação das depêndencias do projeto.
<br />
<br />
**Apis sobre Tipos de caminhões**

**127.0.0.1:8080/alltypesoftrucks**
<br />
Lista todos os tipos de caminhoões cadastrados

**127.0.0.1:8080//typeoftruck/add**
<br />
Adiciona um novo tipo de caminhão é apenas necessário passar truck_name = nome do caminhão**

**127.0.0.1:8080//typeoftruck/update**
<br />
Altera registro do caminhão é apenas necessário passar truck_name = nome do caminhão

**127.0.0.1:8080//typeoftruck/del/:id**
<br />
Deleta o registro, necessário passar o id do tipo de caminhão que será deletado
<br />
<br />
**Apis sobre Motoristas**
**127.0.0.1:8080/driver/list/:id**
<br />
Exibi sobre o motorista -> Id, nome, origem e destino
**127.0.0.1:8080/driver/listalldrivers**
<br />
Exibi sobre os motoristas -> Id, nome, origem e destino
**127.0.0.1:8080/driver/vehiclenotloaded**
<br />
Exibi os motoristas que não estão com o caminhão carregado
**127.0.0.1:8080/driver/ownvehicle**
<br />
Exibi os motoristas que tem veículo próprio
**127.0.0.1:8080/driver/ownvehicle**
<br />
Exibi os motoristas que tem veículo próprio
**127.0.0.1:8080/driver/notownvehicle**
<br />
Exibi os motoristas que não tem veículo próprio
