# Correções para Deploy no Streamlit Cloud

## Problemas Encontrados

1. **Problemas de compilação**:
   - `tiktoken` - Falha na compilação
   - `pycairo` (dependência do `xhtml2pdf`) - Requer bibliotecas do sistema
   - `distutils` - Módulo ausente no Python 3.13
   - `WeasyPrint` - Problemas de compilação

2. **Conflitos de versões**:
   - `pydantic` - Conflito com `crewai`
   - `openai` - Versão incompatível com `crewai`
   - `instructor` - Versão incompatível com `crewai`
   - `numpy` - Versão incompatível com Python 3.13

3. **Ambiente Python**:
   - Streamlit Cloud está usando Python 3.13, apesar da configuração no `runtime.txt`

## Alterações Realizadas

### 1. Arquivo `packages.txt`
Adicionadas bibliotecas do sistema necessárias para compilação:
```
libcairo2-dev
libpango1.0-dev
libgdk-pixbuf2.0-dev
libffi-dev
shared-mime-info
libxml2-dev
libxslt-dev
build-essential
python3-dev
python3-distutils
pkg-config
libjpeg-dev
libpng-dev
libtiff-dev
zlib1g-dev
```

### 2. Arquivo `requirements.txt`
- Removido `tiktoken` (OpenAI funciona sem ele, apenas mais lento na tokenização)
- Removido `WeasyPrint` (também causa problemas de compilação)
- Ajustada versão do `numpy` para range `>=1.22.0,<1.25.0` (mais flexível)
- Ajustada versão do `reportlab` para 3.6.13 (mais estável)
- Ajustada versão do `openai` para `>=1.7.1,<2.0.0` (compatível com `crewai`)
- Ajustada versão do `pydantic` para `>=2.4.2,<3.0.0` (compatível com `crewai`)
- Ajustada versão do `instructor` para `>=0.5.2,<0.6.0` (compatível com `crewai`)
- Adicionado `setuptools>=65.5.0` para resolver problema com `distutils`

### 3. Arquivo `setup.py`
- Removido `tiktoken`
- Removido `WeasyPrint`
- Atualizada versão do `numpy`
- Atualizada versão do `reportlab`
- Atualizada versão do `openai`
- Atualizada versão do `pydantic`
- Atualizada versão do `instructor`
- Adicionado `setuptools`

### 4. Arquivo `app.py`
- Substituído import de `WeasyPrint` por imports do `reportlab`
- Reescrita completamente a função `convert_markdown_to_pdf` para usar apenas o ReportLab

### 5. Arquivo `runtime.txt`
- Alterada versão do Python de 3.10.13 para 3.9.18 (embora o Streamlit Cloud possa estar ignorando isso)

## Próximos Passos

1. Fazer commit e push das alterações:
```bash
git add .
git commit -m "Corrigidos problemas de dependências para deploy no Streamlit Cloud"
git push origin main
```

2. No painel do Streamlit Cloud:
   - Verificar se o branch está configurado como `main`
   - O arquivo principal deve ser `streamlit_app.py`
   - Clicar em "Deploy" ou "Redeploy"
   - Se possível, tentar recriar o app para garantir que as configurações sejam aplicadas corretamente

3. Se ainda houver problemas:
   - Verificar logs de erro
   - Considerar usar apenas dependências que não requerem compilação
   - Considerar usar versões pré-compiladas (wheels) quando disponíveis
   - Considerar hospedar em outro serviço como Heroku ou Railway
