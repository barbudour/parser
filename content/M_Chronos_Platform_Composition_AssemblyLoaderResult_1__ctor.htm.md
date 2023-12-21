# AssemblyLoaderResult<TMetadata> \- конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public AssemblyLoaderResult(
    	IReadOnlyList<IMetadataExportItem<TMetadata>> items,
    	IReadOnlyList<IAssemblyResolver> assemblyResolvers,
    	IAssemblyLoaderOptions options
    )
VB __Копировать
     Public Sub New ( 
    	items As IReadOnlyList(Of IMetadataExportItem(Of TMetadata)),
    	assemblyResolvers As IReadOnlyList(Of IAssemblyResolver),
    	options As IAssemblyLoaderOptions
    )
C++ __Копировать
     public:
    AssemblyLoaderResult(
    	IReadOnlyList<IMetadataExportItem<TMetadata>^>^ items, 
    	IReadOnlyList<IAssemblyResolver^>^ assemblyResolvers, 
    	IAssemblyLoaderOptions^ options
    )
F# __Копировать
     new : 
            items : IReadOnlyList<IMetadataExportItem<'TMetadata>> * 
            assemblyResolvers : IReadOnlyList<IAssemblyResolver> * 
            options : IAssemblyLoaderOptions -> AssemblyLoaderResult
#### Параметры
items
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[IMetadataExportItem](T_Chronos_Platform_Composition_IMetadataExportItem_1.htm)<[TMetadata](T_Chronos_Platform_Composition_AssemblyLoaderResult_1.htm)>>
     Вся экспортированная метаинформация. Параметр не равен null. 
assemblyResolvers
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[IAssemblyResolver](T_Chronos_Platform_Composition_IAssemblyResolver.htm)>
     Объекты, выполнявшие загрузку сборок в процессе экспорта метаинформации. Параметр не равен null. 
options
[IAssemblyLoaderOptions](T_Chronos_Platform_Composition_IAssemblyLoaderOptions.htm)
     Настройки, использованные при экспорте метаинформации. Параметр не равен null. 
## __См. также
#### Ссылки
[AssemblyLoaderResult<TMetadata> \-
](T_Chronos_Platform_Composition_AssemblyLoaderResult_1.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
