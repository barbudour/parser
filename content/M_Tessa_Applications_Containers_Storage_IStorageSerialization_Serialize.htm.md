# IStorageSerialization.Serialize - метод
Осуществяляет сериализацию элемента в хранилище создаваемое с помощью фабрики
storageFactory
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    IStorage Serialize(
    	[NotNullAttribute] IStorageFactory storageFactory
    )
VB __Копировать
    <NotNullAttribute>
    Function Serialize ( 
    	<NotNullAttribute> storageFactory As IStorageFactory
    ) As IStorage
C++ __Копировать
    [NotNullAttribute]
    IStorage^ Serialize(
    	[NotNullAttribute] IStorageFactory^ storageFactory
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract Serialize : 
            [<NotNullAttribute>] storageFactory : IStorageFactory -> IStorage 
#### Параметры
storageFactory
[IStorageFactory](T_Tessa_Applications_Containers_Storage_IStorageFactory.htm)
     Фабрика создания хранилища 
#### Возвращаемое значение
[IStorage](T_Tessa_Applications_Containers_Storage_IStorage.htm)  
Хранилище содержащее сериализованое представление объекта
[IStorage](T_Tessa_Applications_Containers_Storage_IStorage.htm).
## __См. также
#### Ссылки
[IStorageSerialization -
](T_Tessa_Applications_Containers_Storage_IStorageSerialization.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
