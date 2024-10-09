from rest_framework import serializers

"""
    Serializador para validar lo que el usuario ingrese y para regresar la respuesta
    con el número que falta.
"""
class NumberSetSerializer(serializers.Serializer):
    number = serializers.IntegerField(min_value = 1, max_value = 100)