Documentação: https://kubernetes.io/docs/concepts/storage/persistent-volumes/

Um PersistentVolume (PV) é uma parte do armazenamento no cluster que foi provisionado por um administrador ou provisionado dinamicamente Storage Classes. Os PVs tem um ciclo de vida independente de qualquer pod associado a ele.

#### Tipos de Volumes:

awsElasticBlockStore - AWS Elastic Block Store (EBS)
azureDisk - Azure Disk
azureFile - Azure File
cephfs - CephFS volume
cinder - Cinder (OpenStack block storage)
csi - Container Storage Interface (CSI)
fc - Fibre Channel (FC) storage
flexVolume - FlexVolume
flocker - Flocker storage
gcePersistentDisk - GCE Persistent Disk
glusterfs - Glusterfs volume
*hostPath - HostPath volume*
iscsi - iSCSI (SCSI over IP) storage
local
nfs - Network File System (NFS) storage
photonPersistentDisk - Photon controller persistent disk.
portworxVolume - Portworx volume
quobyte - Quobyte volume
rbd - Rados Block Device (RBD) volume
scaleIO - ScaleIO volume
storageos - StorageOS volume
vsphereVolume - vSphere VMDK volume

#### Capacidade:

Especificação de tamanho do PV ( Gi Mi)

    capacity: 
      storage: 1Gi

#### VolumeMode:

    volumeMode: [Filesystem | Block]

#### accessModes:

ReadWriteOnce -- O volume pode ser montado com leitura e escrita(read-write) por um único node.
ReadOnlyMany -- O volume pode ser montado como somente leitura(read-only) por vários node.
ReadWriteMany -- O volume pode ser montado como leitura e escrita(read-write) por vários nodes.

    accessModes:
    - [ReadWriteOnce | ReadOnlyMany | ReadWriteMany]

#### Reclaim Policy:

Essa opção tem como objetivo a ação que o cluster irá fazer após que o PVC for excluído.

Retain -- Precisa de uma ação manual
Recycle -- Basico (rm -rf /thevolume/*)
Delete -- utilizando AWS EBS, GCE PD, Azure Disk, ou OpenStack Cinder o volume é deletado

    persistentVolumeReclaimPolicy: [Retain | Recycle | Delete]

#### Class:

Determina qual será o storageClass que o PV irá utilizar.

    storageClassName: ""

#### hostPath:

Um volume hostPath monta um arquivo ou diretório do filesystem do nó do host em seu pod.

    hostPath:
      path:
      type: [ FileOrCreate | DirectoryOrCreate ]

DirectoryOrCreate = Se nada existir no caminho fornecido, um diretório vazio será criado lá conforme necessário com a permissão definida como 0755, tendo o mesmo grupo e propriedade do Kubelet.

FileOrCreate = Se nada existir no caminho fornecido, um arquivo vazio será criado lá conforme necessário com a permissão definida como 0644, tendo o mesmo grupo e propriedade do Kubelet.