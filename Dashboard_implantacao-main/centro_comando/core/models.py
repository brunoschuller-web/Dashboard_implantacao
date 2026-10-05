from django.db import models

class Loja(models.Model):
    FASES = [
        ('piloto', 'Piloto'),
        ('em_migracao', 'Em Migração'),
        ('migrada', 'Migrada'),
        ('pendente', 'Pendente'),
    ]
    codigo = models.CharField(max_length=10, unique=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    fase = models.CharField(max_length=20, choices=FASES, default='pendente')

    def __str__(self):
        return f"Loja {self.codigo} - {self.cidade}/{self.estado}"

class Computador(models.Model):
    STATUS_MIG = [
        ('pendente', 'Pendente'),
        ('andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
    ]
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='computadores')
    hostname = models.CharField(max_length=50)
    ip = models.GenericIPAddressField()
    mac = models.CharField(max_length=17)
    processador = models.CharField(max_length=50)
    ram = models.IntegerField()
    so = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_MIG, default='pendente')
    data_migracao = models.DateTimeField(null=True, blank=True)
    online = models.BooleanField(default=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.hostname