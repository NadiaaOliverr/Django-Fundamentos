from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe
from passagens.validation import *
from passagens.models import Passagem, ClasseViagem, Pessoa

class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da Pesquisa', disabled=True, initial=datetime.today)

    class Meta:
        model = Passagem
        fields = '__all__'
        # Caso queira excluir algum campo: exclude = ['origem']
        labels = {
            'data_ida': 'Data de Ida',
            'data_volta': 'Data de Volta',
            'informacoes': 'Informações',
            'classe_viagem': 'Classe do Vôo'
        }
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker()
        }
   
    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_da_ida = self.cleaned_data.get('data_ida')
        data_da_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')


        lista_de_erros = {}
        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        data_ida_maior_que_data_volta(data_da_ida, data_da_volta, lista_de_erros)
        data_de_ida_nao_pode_ser_menor_que_a_data_de_hoje(data_da_ida, data_pesquisa, lista_de_erros)
        if lista_de_erros is not None:
            for error in lista_de_erros:
                mensagem_erro = lista_de_erros[error]
                self.add_error(error, mensagem_erro)
        return self.cleaned_data

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome'] # vai trazer todos, exceto o nome

# # Sem usar um modelo
# class PassagemForms(forms.Form):
#     origem = forms.CharField(label='Origem', max_length=100)
#     destino = forms.CharField(label='Destino', max_length=100)
#     data_da_ida = forms.DateField(label='Ida', widget=DatePicker())
#     data_da_volta = forms.DateField(label='Volta', widget=DatePicker())
#     data_pesquisa = forms.DateField(label='Data da Pesquisa', disabled=True, initial=datetime.today)
#     classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipos_de_classe)
#     informacoes = forms.CharField(
#         label='Informações Extras',
#         max_length=200,
#         widget=forms.Textarea,
#         required=False
#     )
#     email = forms.EmailField(label='E-mail', max_length=150)

#     # Alguns parâmetros para o widget
#     # widget=DatePicker(
#     #         options={
#     #             'minDate': '2009-01-20',
#     #             'maxDate': '2017-01-20',
#     #         },
#     #     ),
#     #     initial='2013-01-01'

#     # Posso usar o clen_ ou o clean, o clean é mais integrador, já que posso 
#     # fazer tudo de uma só vez
#     # def clean_origem(self):
#     #     origem = self.cleaned_data.get('origem')
#     #     if any(char.isdigit() for char in origem):
#     #         raise forms.ValidationError('Origem inválida: Não inclua números')
#     #     else:
#     #         return origem
    
#     # def clean_destino(self):
#     #     destino = self.cleaned_data.get('destino')
#     #     if any(char.isdigit() for char in destino):
#     #         raise forms.ValidationError('Destino inválido: Não inclua números')
#     #     else:
#     #         return destino

#     def clean(self):
#         origem = self.cleaned_data.get('origem')
#         destino = self.cleaned_data.get('destino')
#         data_da_ida = self.cleaned_data.get('data_da_ida')
#         data_da_volta = self.cleaned_data.get('data_da_volta')
#         data_pesquisa = self.cleaned_data.get('data_pesquisa')


#         lista_de_erros = {}
#         campo_tem_algum_numero(origem, 'origem', lista_de_erros)
#         campo_tem_algum_numero(destino, 'destino', lista_de_erros)
#         origem_destino_iguais(origem, destino, lista_de_erros)
#         data_ida_maior_que_data_volta(data_da_ida, data_da_volta, lista_de_erros)
#         data_de_ida_nao_pode_ser_menor_que_a_data_de_hoje(data_da_ida, data_pesquisa, lista_de_erros)
#         if lista_de_erros is not None:
#             for error in lista_de_erros:
#                 mensagem_erro = lista_de_erros[error]
#                 self.add_error(error, mensagem_erro)
#         return self.cleaned_data