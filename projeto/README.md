# Projeto Serviços Cloud

## Problema
Desenvolva um sistema que detecte possíveis transações bancárias fraudulentas de forma assíncrona, usando análise de dados de transações e armazenamento em cache para acesso rápido a dados usados com frequência. Se uma transação for definida como fraudulenta, deverá ser possível fazer o download de um relatório. O link deve estar disponível em um sistema de cache.

- Não é necessária uma implementação persistente.
- A implementação do Dead Dead-Letter Queue (DLQ) não é obrigatória.
- Toda implementação deve funcionar se você precisar recriar o RabbitMQ (ou qualquer outra ferramenta), por exemplo. Vou executar o aplicativo em uma máquina virtual "zerada".
- Não é obrigatório implementar nada depois que uma transação for considerada normal (não fraudulenta).

## Definição de fraude
- Você pode definir qualquer regra que desejar
- Sugestão: Transações realizadas em locais distantes em um curto período de tempo, no qual não seria fisicamente possível que o cliente viajasse. Exemplo: Compra em São Paulo e minutos depois em Pernambuco

## Relatório  
 - Deve ser um arquivo (txt, pdf, ...)
 - Contém dados da última transação
 - Deve conter o número da conta
 - Opcional (dados de transações anteriores)
 - Você pode usar outras ferramentas semelhantes de mensagens, cache e armazenamento, não é obrigatório que eles sejam exatamente as estudadas neste módulo
 