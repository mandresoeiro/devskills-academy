# Primeira skill: preparar commits sem segredos

- ID: DSA-057
- Categoria: Git e GitHub
- Prioridade: P1
- Estado: planejada; implementação ainda não iniciada.
- Destino previsto: `skills/git/01/SKILL.md`.

## Objetivo

Orientar a inspeção de alterações antes de um commit, identificando credenciais, arquivos locais e dados que não devem entrar no histórico. A revisão reduz riscos, mas não garante ausência de segredos.

## Por que começar aqui

Todas as próximas skills passarão pelo GitHub. Um procedimento de revisão de publicação será reutilizado desde o início da biblioteca.

## Requisitos propostos

1. Ler as instruções do repositório e identificar o escopo autorizado.
2. Inspecionar arquivos preparados para commit, incluindo arquivos novos e ignorados relevantes, sem imprimir valores sensíveis.
3. Identificar arquivos de ambiente, chaves privadas, tokens e dados pessoais indevidos.
4. Sugerir exclusões específicas no .gitignore e exemplos com valores fictícios.
5. Se um segredo já tiver sido publicado, orientar revogação ou rotação; apagar o texto não elimina a exposição.
6. Preservar alterações do usuário e não reescrever histórico nem publicar sem autorização aplicável.
7. Exigir revisão humana e registrar os limites da análise automatizada.

## Critérios de aceite para a futura implementação

- Um exemplo com token inteiramente fictício é sinalizado sem expor seu valor na saída.
- Um exemplo de configuração sem credenciais pode ser versionado.
- Arquivos legítimos não são removidos ou ignorados indiscriminadamente.
- A skill distingue segredo novo de segredo já presente no histórico.
- Referências oficiais e compatibilidade de agentes são verificadas antes de declarar a skill concluída.

## Primeiro passo prático

Revisar este escopo e os critérios de aceite. Na próxima etapa, criar somente o `SKILL.md` desta skill e suas evidências de validação. Nenhuma outra skill deve ser iniciada junto com ela.

