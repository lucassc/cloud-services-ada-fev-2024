# Mensageiria 

## RabbitMQ 

### Docker

```BASH
docker run --rm -it -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```

Depois que o comando acima tiver sido executado, você poderá acessar o portal do RabbitMQ em http://localhost:15672/ 

Usuário: `guest`
Senha: `guest`

### CLI 

[rabbitmqadmin](http://localhost:15672/cli/rabbitmqadmin)

```BASH
sudo curl -o /usr/local/bin/rabbitmqadmin http://localhost:15672/cli/rabbitmqadmin

sudo chmod +x sudo curl -o /usr/local/bin/rabbitmqadmin

sudo sh -c "rabbitmqadmin --bash-completion > /etc/bash_completion.d/rabbitmqadmin"
```

#### Exemplos de comandos

[Management Command Line Tool - Examples](https://www.rabbitmq.com/docs/management-cli#examples)

```BASH
rabbitmqadmin -V test publish exchange=amq.fanout payload="hello, world" routing_key=""
```