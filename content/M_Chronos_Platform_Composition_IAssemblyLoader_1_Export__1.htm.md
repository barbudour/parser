# IAssemblyLoader<TMetadata>.Export<TAttribute>(IAssemblyLoaderOptions) -
метод
Экспортирует метаинформацию по заданному атрибуту.
##  __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     IAssemblyLoaderResult<TMetadata> Export<TAttribute>(
    	IAssemblyLoaderOptions options = null
    )
    where TAttribute : Attribute, TMetadata
VB __Копировать
     Function Export(Of TAttribute As {Attribute, TMetadata}) ( 
    	Optional options As IAssemblyLoaderOptions = Nothing
    ) As IAssemblyLoaderResult(Of TMetadata)
C++ __Копировать
    generic<typename TAttribute>
    where TAttribute : Attribute, TMetadata
    IAssemblyLoaderResult<TMetadata>^ Export(
    	IAssemblyLoaderOptions^ options = nullptr
    )
F# __Копировать
     abstract Export : 
            ?options : IAssemblyLoaderOptions 
    (* Defaults:
            let _options = defaultArg options null
    *)
    -> IAssemblyLoaderResult<'TMetadata>  when 'TAttribute : Attribute and 'TMetadata
#### Параметры
options
[IAssemblyLoaderOptions](T_Chronos_Platform_Composition_IAssemblyLoaderOptions.htm)
(Optional)
     Настройки, связанные с экспортом метаданных из сборки, или null, если используются настройки по умолчанию. 
#### Параметры типа
TAttribute
     Тип атрибута с метаинформацией. Должен наследоваться от класса [Attribute] и реализовывать интерфейс метаинформации TMetadata. 
#### Возвращаемое значение
[IAssemblyLoaderResult](T_Chronos_Platform_Composition_IAssemblyLoaderResult_1.htm)<[TMetadata](T_Chronos_Platform_Composition_IAssemblyLoader_1.htm)>  
Результат экспорта метаданных из сборок.
##  __См. также
#### Ссылки
[IAssemblyLoader<TMetadata> \-
](T_Chronos_Platform_Composition_IAssemblyLoader_1.htm)
[Export -
перегрузка](Overload_Chronos_Platform_Composition_IAssemblyLoader_1_Export.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
