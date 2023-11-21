#### Configurando versionamento:

Habilitar o versionamento em buckets: https://docs.aws.amazon.com/pt_br/AmazonS3/latest/userguide/manage-versioning-examples.html

Ativando:

    aws s3api put-bucket-versioning --bucket DOC-EXAMPLE-BUCKET1 --versioning-configuration Status=Enabled
			
    aws s3api get-bucket-versioning --bucket my-bucket

Imprimindo as versões do objeto (arquivo):

    aws s3api list-object-versions --bucket my-bucket | grep - A1 teste.txt

Recuperando a versão:

    rm -rf teste.txt

    aws s3api get-object --bucket my-bucket --key teste.txt --version-id pd4G_9sqBj9NHmV7oPjA teste.txt