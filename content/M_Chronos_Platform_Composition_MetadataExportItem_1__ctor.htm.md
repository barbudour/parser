# MetadataExportItem<TMetadata> \- конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public MetadataExportItem(
    	TMetadata metadata,
    	string assemblyFilePath,
    	string assemblyFullName,
    	string typeFullName,
    	string assemblyQualifiedTypeName,
    	Func<AssemblyLoadContext, Assembly> resolveAssemblyFunc = null,
    	Type[] implementedInterfaceTypes = null
    )
VB __Копировать
     Public Sub New ( 
    	metadata As TMetadata,
    	assemblyFilePath As String,
    	assemblyFullName As String,
    	typeFullName As String,
    	assemblyQualifiedTypeName As String,
    	Optional resolveAssemblyFunc As Func(Of AssemblyLoadContext, Assembly) = Nothing,
    	Optional implementedInterfaceTypes As Type() = Nothing
    )
C++ __Копировать
     public:
    MetadataExportItem(
    	TMetadata metadata, 
    	String^ assemblyFilePath, 
    	String^ assemblyFullName, 
    	String^ typeFullName, 
    	String^ assemblyQualifiedTypeName, 
    	Func<AssemblyLoadContext^, Assembly^>^ resolveAssemblyFunc = nullptr, 
    	array<Type^>^ implementedInterfaceTypes = nullptr
    )
F# __Копировать
     new : 
            metadata : 'TMetadata * 
            assemblyFilePath : string * 
            assemblyFullName : string * 
            typeFullName : string * 
            assemblyQualifiedTypeName : string * 
            ?resolveAssemblyFunc : Func<AssemblyLoadContext, Assembly> * 
            ?implementedInterfaceTypes : Type[] 
    (* Defaults:
            let _resolveAssemblyFunc = defaultArg resolveAssemblyFunc null
            let _implementedInterfaceTypes = defaultArg implementedInterfaceTypes null
    *)
    -> MetadataExportItem
#### Параметры
metadata [TMetadata](T_Chronos_Platform_Composition_MetadataExportItem_1.htm)
    Экспортированная метаинформация.
assemblyFilePath
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Путь к файлу со сборкой.
assemblyFullName
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Полное имя сборки.
typeFullName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Полное имя типа без указания сборки.
assemblyQualifiedTypeName
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Квалифицированное имя типа, которое включает имя сборки.
resolveAssemblyFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[AssemblyLoadContext](https://learn.microsoft.com/dotnet/api/system.runtime.loader.assemblyloadcontext),
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)>
(Optional)
     Функция, выполняющая загрузку сборки, в которой размещается тип, или null, если загруженная сборка недоступна. 
implementedInterfaceTypes
[Type](https://learn.microsoft.com/dotnet/api/system.type)[] (Optional)
     Типы интерфейсов, которые реализует экспортированный тип. Типы всех проверяемых интерфейсов должны быть указаны при экспорте. Равен null, если таких интерфейсов нет. 
## __См. также
#### Ссылки
[MetadataExportItem<TMetadata> \-
](T_Chronos_Platform_Composition_MetadataExportItem_1.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
