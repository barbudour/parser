# XmlStorageFactory.Create - метод
Осщуествляет создание хранилища
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IStorage Create(
    	IStorageSchemaContext schemaContext
    )
VB __Копировать
     Public Function Create ( 
    	schemaContext As IStorageSchemaContext
    ) As IStorage
C++ __Копировать
     public:
    virtual IStorage^ Create(
    	IStorageSchemaContext^ schemaContext
    ) sealed
F# __Копировать
     abstract Create : 
            schemaContext : IStorageSchemaContext -> IStorage 
    override Create : 
            schemaContext : IStorageSchemaContext -> IStorage 
#### Параметры
schemaContext
[IStorageSchemaContext](T_Tessa_Applications_Containers_Storage_IStorageSchemaContext.htm)
     Контекст хранилища 
#### Возвращаемое значение
[IStorage](T_Tessa_Applications_Containers_Storage_IStorage.htm)  
Созданное хранилище
#### Реализации
[IStorageFactory.Create(IStorageSchemaContext)](M_Tessa_Applications_Containers_Storage_IStorageFactory_Create.htm)  
##  __См. также
#### Ссылки
[XmlStorageFactory -
](T_Tessa_Applications_Containers_Storage_XmlStorageFactory.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
