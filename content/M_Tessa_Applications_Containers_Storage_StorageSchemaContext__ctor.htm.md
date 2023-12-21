# StorageSchemaContext - конструктор
Initializes a new instance of the
[StorageSchemaContext](T_Tessa_Applications_Containers_Storage_StorageSchemaContext.htm)
class. Initializes a new instance of the
[StorageSchemaContext](T_Tessa_Applications_Containers_Storage_StorageSchemaContext.htm)
struct. Initializes a new instance of the
[StorageSchemaContext](T_Tessa_Applications_Containers_Storage_StorageSchemaContext.htm)
class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public StorageSchemaContext(
    	[NotNullAttribute] string schemaName,
    	[NotNullAttribute] string schemaId,
    	[NotNullAttribute] string rootElement,
    	[CanBeNullAttribute] Type schemaFactoryType = null
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> schemaName As String,
    	<NotNullAttribute> schemaId As String,
    	<NotNullAttribute> rootElement As String,
    	<CanBeNullAttribute> Optional schemaFactoryType As Type = Nothing
    )
C++ __Копировать
     public:
    StorageSchemaContext(
    	[NotNullAttribute] String^ schemaName, 
    	[NotNullAttribute] String^ schemaId, 
    	[NotNullAttribute] String^ rootElement, 
    	[CanBeNullAttribute] Type^ schemaFactoryType = nullptr
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] schemaName : string * 
            [<NotNullAttribute>] schemaId : string * 
            [<NotNullAttribute>] rootElement : string * 
            [<CanBeNullAttribute>] ?schemaFactoryType : Type 
    (* Defaults:
            let _schemaFactoryType = defaultArg schemaFactoryType null
    *)
    -> StorageSchemaContext
#### Параметры
schemaName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Пространство имен 
schemaId [String](https://learn.microsoft.com/dotnet/api/system.string)
     Идентификато схемы 
rootElement [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя корневого элемента 
schemaFactoryType [Type](https://learn.microsoft.com/dotnet/api/system.type)
(Optional)
     Тип фабрики схемы. 
## __См. также
#### Ссылки
[StorageSchemaContext -
](T_Tessa_Applications_Containers_Storage_StorageSchemaContext.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
