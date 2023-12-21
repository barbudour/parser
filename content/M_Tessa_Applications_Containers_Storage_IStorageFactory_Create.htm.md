# IStorageFactory.Create - метод
Осщуествляет создание хранилища
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    IStorage Create(
    	[NotNullAttribute] IStorageSchemaContext schemaContext
    )
VB __Копировать
    <NotNullAttribute>
    Function Create ( 
    	<NotNullAttribute> schemaContext As IStorageSchemaContext
    ) As IStorage
C++ __Копировать
    [NotNullAttribute]
    IStorage^ Create(
    	[NotNullAttribute] IStorageSchemaContext^ schemaContext
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract Create : 
            [<NotNullAttribute>] schemaContext : IStorageSchemaContext -> IStorage 
#### Параметры
schemaContext
[IStorageSchemaContext](T_Tessa_Applications_Containers_Storage_IStorageSchemaContext.htm)
     Контекст хранилища 
#### Возвращаемое значение
[IStorage](T_Tessa_Applications_Containers_Storage_IStorage.htm)  
Созданное хранилище
## __См. также
#### Ссылки
[IStorageFactory -
](T_Tessa_Applications_Containers_Storage_IStorageFactory.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
