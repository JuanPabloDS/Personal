from django.db import models
import uuid
from django.db.models import signals
from stdimage.models import StdImageField
from django.core.validators import RegexValidator

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)


def get_file_path(_instance, filename):
    """ Função para gerar nomes aleátorios quando for salvar um
    arquivo de imagem"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Apresentacao(Base):
    titulo = models.CharField(max_length=100)
    icon = StdImageField('icon',upload_to=get_file_path, help_text='Icone da página')
    imagem_back = StdImageField('fundo',upload_to=get_file_path, help_text='Imagem de fundo da tela inicial')
    instagram = models.CharField(max_length=100, help_text='Usuario do seu instagram')
    instagram_link = models.CharField(max_length=100, help_text='Link do seu instagram')
    descricao = models.CharField(max_length=100)


    def register(self):
        self.save()

    class Meta:
        verbose_name = 'Apresentacao'
        verbose_name_plural = 'Apresentacao'


    def __str__(self) -> str:
        """Retorna o str"""
        return f'{self.titulo}'


class Sobre(Base):
    titulo = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Sobre'
        verbose_name_plural = 'Sobre'

    def __str__(self) -> str:
        """Retorna o str"""
        return f'{self.titulo}'


class SobreDados(Base):
    titulo = models.CharField(max_length=100)
    textos = models.TextField()

    class Meta:
        verbose_name = 'Sobre texto'
        verbose_name_plural = 'Sobre textos'

    def __str__(self) -> str:
        """Retorna o str"""
        return f'{self.titulo}'

class Detalhes(Base):
    cor_validator = RegexValidator(
        regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
        message='Insira uma cor válida no formato hexadecimal, começando com #.'
    )

    titulo = models.CharField(max_length=100)
    img = StdImageField('detalhes',upload_to=get_file_path)
    texto1 = models.TextField()
    texto2 = models.TextField()
    cor_titulo = models.CharField(max_length=7, validators=[cor_validator], default='')
    cor_fundo = models.CharField(max_length=7, validators=[cor_validator], default='')
    cor_texto = models.CharField(max_length=7, validators=[cor_validator], default='')

    class Meta:
        verbose_name = 'Detalhe'
        verbose_name_plural = 'Detalhes'


    def __str__(self) -> str:
        """Retorna o str"""
        return f'{self.titulo}'

class Precos(Base):
    titulo = models.CharField(max_length=100)
    aviso = models.CharField(max_length=100)


    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'


    def __str__(self) -> str:
        """Retorna o str"""
        return f'{self.titulo}'


class PrecosPlano1(Base):
    titulo = models.CharField(max_length=100)
    dias = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    img = StdImageField('imagem',upload_to=get_file_path, default='')

    class Meta:
        verbose_name = 'Preço Plano 1'
        verbose_name_plural = 'Preços Plano 1'


    def __str__(self) -> str:
        """Retorna o str"""
        return f'{self.titulo}'

class PrecosPlano1Dados(Base):
    destaque = models.TextField(blank=True)
    texto = models.TextField()

    class Meta:
        verbose_name = 'Preço plano 1 texto'
        verbose_name_plural = 'Preço plano 1 texto'

    def __str__(self) -> str:
        """Retorna o str"""
        return f'item'


class PrecosPlano2(Base):
    titulo = models.CharField(max_length=100)
    dias = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    img = StdImageField('imagem',upload_to=get_file_path, default='')

    class Meta:
        verbose_name = 'Preço plano 2'
        verbose_name_plural = 'Preço plano 2'

    def __str__(self) -> str:
        """Retorna o str"""
        return f'{self.titulo}'

class PrecosPlano2Dados(Base):
    destaque = models.TextField(blank=True)
    texto = models.TextField()

    class Meta:
        verbose_name = 'Preço plano 2 texto'
        verbose_name_plural = 'Preço plano 2 texto'

    def __str__(self) -> str:
        """Retorna o str"""
        return f'item'


class Imagem(Base):
    titulo = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Imagem Titulo'
        verbose_name_plural = 'Imagem Titulo'


    def __str__(self) -> str:
        """Retorna o str"""
        return f'{self.titulo}'

class ImagensLista(Base):
    img = StdImageField('imagem',upload_to=get_file_path)

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'


class Duvidas(Base):
    titulo = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Duvida Titulo'
        verbose_name_plural = 'Duvidas Titulo'


    def __str__(self) -> str:
        """Retorna o str"""
        return f'{self.titulo}'

class DuvidasRespostas(Base):
    titulo = models.CharField(max_length=100)
    resposta = models.TextField()

    class Meta:
        verbose_name = 'Duvida e resposta'
        verbose_name_plural = 'Duvidas e respostas'


    def __str__(self) -> str:
        """Retorna o str"""
        return f'{self.titulo}'

class Contato(Base):
    titulo = models.CharField(max_length=100)
    destaque = models.CharField(max_length=100)
    botao = models.CharField(max_length=50)
    link = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'


    def __str__(self) -> str:
        """Retorna o str"""
        return f'{self.titulo}'

class Cores(Base):
    cor_validator = RegexValidator(
        regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
        message='Insira uma cor válida no formato hexadecimal, começando com #.'
    )
    cor_titulo = models.CharField(max_length=7, validators=[cor_validator])
    cor_titulo_dois = models.CharField(max_length=7, validators=[cor_validator])
    cor_fundo_pagina = models.CharField(max_length=7, validators=[cor_validator])
    cor_menu = models.CharField(max_length=7, validators=[cor_validator])
    cor_paragrafo = models.CharField(max_length=7, validators=[cor_validator])
    cor_sublinhado_titulo = models.CharField(max_length=7, validators=[cor_validator])
    cor_box = models.CharField(max_length=7, validators=[cor_validator])
    cor_sobre = models.CharField(max_length=7, validators=[cor_validator])
    cor_back_text = models.CharField(max_length=7, validators=[cor_validator])
    cor_sobre_fundo = models.CharField(max_length=7, validators=[cor_validator])
    cor_sobre_titulo = models.CharField(max_length=7, validators=[cor_validator])
    cor_price_fundo = models.CharField(max_length=7, validators=[cor_validator])
    cor_price_titulo = models.CharField(max_length=7, validators=[cor_validator])
    cor_price_texto = models.CharField(max_length=7, validators=[cor_validator])
    cor_price_money = models.CharField(max_length=7, validators=[cor_validator])
    cor_price_box = models.CharField(max_length=7, validators=[cor_validator])
    cor_price_value = models.CharField(max_length=7, validators=[cor_validator])
    cor_price_span = models.CharField(max_length=7, validators=[cor_validator])
    cor_price_pg = models.CharField(max_length=7, validators=[cor_validator])
    cor_imagem_fundo = models.CharField(max_length=7, validators=[cor_validator])
    cor_imagem_titulo = models.CharField(max_length=7, validators=[cor_validator])
    cor_question_fundo = models.CharField(max_length=7, validators=[cor_validator])
    cor_question_titulo = models.CharField(max_length=7, validators=[cor_validator])
    cor_question_texto = models.CharField(max_length=7, validators=[cor_validator])
    cor_question_box = models.CharField(max_length=7, validators=[cor_validator])
    cor_question_span = models.CharField(max_length=7, validators=[cor_validator])
    cor_contact_fundo = models.CharField(max_length=7, validators=[cor_validator])
    cor_contact_titulo = models.CharField(max_length=7, validators=[cor_validator])
    cor_contact_texto = models.CharField(max_length=7, validators=[cor_validator])
    cor_contact_box = models.CharField(max_length=7, validators=[cor_validator])
    cor_contact_span = models.CharField(max_length=7, validators=[cor_validator])


    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

    def __str__(self) -> str:
        """Retorna o str"""
        return f'Todas as cores'
