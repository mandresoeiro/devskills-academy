# DevSkills Academy

Biblioteca profissional de skills reutilizáveis para agentes de IA e desenvolvimento de software, com documentação em português brasileiro.

## Estado do projeto

Catálogo inicial com **160 skills planejadas em 40 categorias**: 40 P1, 80 P2 e 40 P3. Nenhuma skill está implementada ou testada. A primeira selecionada é **DSA-057 — Preparar commits sem segredos**.

## Documentação

- [Proposta e requisitos do projeto](docs/PROJETO.md)
- [Catálogo e indicadores](catalog/README.md)
- [Inventário completo em JSON](catalog/skills.json)
- [Escopo e primeiro passo da skill inicial](docs/PRIMEIRA-SKILL.md)

## Validação local

Requer Python 3.10 ou superior, sem dependências externas.

```sh
python scripts/validate_catalog.py
python -m unittest discover -s tests -v
```

O validador confere campos, datas, prioridades, status, duplicações, caminhos e correspondência com a tabela do catálogo. Os testes verificam rejeição de dados inválidos; não representam testes das skills planejadas.

## Arquitetura planejada

| Pasta | Finalidade |
| --- | --- |
| `skills/` | Skills organizadas por tecnologia e especialidade |
| `catalog/` | Inventário, prioridades e acompanhamento |
| `templates/` | Modelos reutilizáveis |
| `scripts/` | Validação e manutenção |
| `tests/` | Testes de skills e do catálogo |
| `docs/` | Documentação do projeto e futuro site MkDocs |
| `examples/` | Exemplos práticos |
| `.github/workflows/` | Validações automáticas futuras |

## Método de trabalho

Uma skill por vez: definir requisitos, implementar, validar, testar, documentar e registrar no catálogo antes de iniciar a próxima com autorização.

A compatibilidade com cada agente será verificada individualmente. Nenhuma compatibilidade é declarada nesta etapa.

## Licença

A definir pelo responsável pelo projeto.


