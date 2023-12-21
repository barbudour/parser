# AssemblyLoader<TMetadata>.Export(IReadOnlyCollection<Type>,
IAssemblyLoaderOptions) - метод
Экспортирует метаинформацию по заданному списку атрибутов.
##  __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public IAssemblyLoaderResult<TMetadata> Export(
    	IReadOnlyCollection<Type> attributes,
    	IAssemblyLoaderOptions options = null
    )
VB __Копировать
     Public Function Export ( 
    	attributes As IReadOnlyCollection(Of Type),
    	Optional options As IAssemblyLoaderOptions = Nothing
    ) As IAssemblyLoaderResult(Of TMetadata)
C++ __Копировать
     public:
    virtual IAssemblyLoaderResult<TMetadata>^ Export(
    	IReadOnlyCollection<Type^>^ attributes, 
    	IAssemblyLoaderOptions^ options = nullptr
    ) sealed
F# __Копировать
     abstract Export : 
            attributes : IReadOnlyCollection<Type> * 
            ?options : IAssemblyLoaderOptions 
    (* Defaults:
            let _options = defaultArg options null
    *)
    -> IAssemblyLoaderResult<'TMetadata> 
    override Export : 
            attributes : IReadOnlyCollection<Type> * 
            ?options : IAssemblyLoaderOptions 
    (* Defaults:
            let _options = defaultArg options null
    *)
    -> IAssemblyLoaderResult<'TMetadata> 
#### Параметры
attributes
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[Type](https://learn.microsoft.com/dotnet/api/system.type)>
     Список типов атрибутов с метаинформацией, которые будут экспортированы. Каждый тип должен наследоваться от класса [Attribute] и реализовывать интерфейс метаинформации TMetadata. 
options
[IAssemblyLoaderOptions](T_Chronos_Platform_Composition_IAssemblyLoaderOptions.htm)
(Optional)
     Настройки, связанные с экспортом метаданных из сборки, или null, если используются настройки по умолчанию. 
#### Возвращаемое значение
[IAssemblyLoaderResult](T_Chronos_Platform_Composition_IAssemblyLoaderResult_1.htm)<[TMetadata](T_Chronos_Platform_Composition_AssemblyLoader_1.htm)>  
Результат экспорта метаданных из сборок.
#### Реализации
[IAssemblyLoader<TMetadata>.Export(IReadOnlyCollection<Type>,
IAssemblyLoaderOptions)](M_Chronos_Platform_Composition_IAssemblyLoader_1_Export.htm)  
##  __См. также
#### Ссылки
[AssemblyLoader<TMetadata> \-
](T_Chronos_Platform_Composition_AssemblyLoader_1.htm)
[Export -
перегрузка](Overload_Chronos_Platform_Composition_AssemblyLoader_1_Export.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
