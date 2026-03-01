# Nome do Projeto: 
Sistema de Reservas de Hotel com Git e Github

# Autores: 
Paula Modesto

# Descrição geral: 
O Sistema de Gestão de Reservas de Hotel é uma aplicação desenvolvida em Python. O objetivo principal é facilitar as operações básicas de receção de um hotel, para isso criei código para os clientes, os quartos e as reservas, e no final uma aplicação com um menu juntando tudo num só, permitindo o controlo de fluxos de hóspedes, inventário de quartos e o registo de ocupação de forma organizada e intuitiva. E com a ajuda do Git e Github, permitiu com que pudesse organizar o meu código de melhor forma.

# Funções principais do sistema: 
O sistema está dividido em três módulos centrais acessíveis: Os clientes; Os quartos e as reservas. Depois foi criado uma aplicação (app.py) que é basicamente um menu em que se juntam os códigos dos clientes, quartos e reservas.

Gestão de Clientes (clientes.py): Permite o registo nominal de novos clientes numa base de dados local (lista) e a listagem completa de todos os hóspedes registados no sistema.

Gestão de Quartos (quartos.py): Possibilita o registo de quartos por numeração ou nome, incluindo uma validação de duplicados para garantir que o mesmo quarto não seja registado duas vezes, além de listar todos os quartos disponíveis para reserva.

Gestão de Reservas (reservas.py): É o módulo de integração que permite criar novas reservas, associando um cliente específico a um número de quarto através de dicionários Python, e consultar a lista de reservas ativas.

Menu da aplicação (app.py): É basicamente o centro da aplicação, oferecendo uma navegação fluida entre todas as áreas do sistema com opções para entrar nos módulos, voltar ao menu anterior ou encerrar o programa de forma segura. Permite gerir as reservas, os quartos e os clientes.