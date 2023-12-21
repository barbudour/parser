# IAssemblyLoaderResult<TMetadata> \- интерфейс
Результат загрузки метаданных из сборок.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAssemblyLoaderResult<out TMetadata>
VB __Копировать
     Public Interface IAssemblyLoaderResult(Of Out TMetadata)
C++ __Копировать
    generic<typename TMetadata>
    public interface class IAssemblyLoaderResult
F# __Копировать
     type IAssemblyLoaderResult<'TMetadata> = interface end
#### Параметры типа
TMetadata
     Тип экспортируемых метаданных. Может реализовывать интерфейс [ISerializableMetadata<TMetadata>](T_Chronos_Contracts_ISerializableMetadata_1.htm) для сериализации. 
## __Свойства
[AssemblyResolvers](P_Chronos_Platform_Composition_IAssemblyLoaderResult_1_AssemblyResolvers.htm)|
Объекты, выполнявшие загрузку сборок в процессе экспорта метаинформации.  
---|---  
[Items](P_Chronos_Platform_Composition_IAssemblyLoaderResult_1_Items.htm)| Вся
экспортированная метаинформация.  
[Options](P_Chronos_Platform_Composition_IAssemblyLoaderResult_1_Options.htm)|
Настройки, использованные при экспорте метаинформации.  
##  __См. также
#### Ссылки
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
