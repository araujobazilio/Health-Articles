# Correções para Deploy no Streamlit Cloud

## Problemas Encontrados

1. **Problemas de compilação**:
   - `tiktoken` - Falha na compilação
   - `pycairo` (dependência do `xhtml2pdf`) - Requer bibliotecas do sistema

2. **Conflitos de versões**:
   - `pydantic` - Conflito com `crewai`
   - `openai` - Versão incompatível com `crewai`
   - `instructor` - Versão incompatível com `crewai`
   - `numpy` - Versão incompatível com Python 3.9

3. **Ambiente Python**:
   - Versão do Python no Streamlit Cloud incompatível com algumas dependências

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
pkg-config
libjpeg-dev
libpng-dev
libtiff-dev
zlib1g-dev
```

### 2. Arquivo `requirements.txt`
- Removido `tiktoken` (OpenAI funciona sem ele, apenas mais lento na tokenização)
- Substituído `xhtml2pdf` por `WeasyPrint` (melhor compatibilidade com Streamlit Cloud)
- Ajustada versão do `numpy` para 1.24.3 (compatível com Python 3.9)
- Ajustada versão do `openai` para `>=1.7.1,<2.0.0` (compatível com `crewai`)
- Ajustada versão do `pydantic` para `>=2.4.2,<3.0.0` (compatível com `crewai`)
- Ajustada versão do `instructor` para `>=0.5.2,<0.6.0` (compatível com `crewai`)

### 3. Arquivo `setup.py`
- Removido `tiktoken`
- Atualizada versão do `openai`
- Substituído `xhtml2pdf` por `WeasyPrint`
- Atualizada versão do `instructor`

### 4. Arquivo `app.py`
- Substituído import de `xhtml2pdf` por `WeasyPrint`
- Atualizada função `convert_markdown_to_pdf` para usar a API do WeasyPrint

### 5. Arquivo `runtime.txt`
- Alterada versão do Python de 3.10.13 para 3.9.18 para melhor compatibilidade com as dependências

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

3. Se ainda houver problemas:
   - Verificar logs de erro
   - Considerar remover outras dependências que requerem compilação
   - Considerar usar versões pré-compiladas (wheels) quando disponíveis
