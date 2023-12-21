# IAssemblyLoaderResult<TMetadata> \- интерфейс
Результат загрузки метаданных из сборок.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Composition](N_Tessa_Platform_Composition.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
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
     Тип экспортируемых метаданных. Может реализовывать интерфейс [ISerializableMetadata<TMetadata>](T_Tessa_Platform_Composition_ISerializableMetadata_1.htm) для сериализации. 
## __Свойства
[AssemblyResolvers](P_Tessa_Platform_Composition_IAssemblyLoaderResult_1_AssemblyResolvers.htm)|
Объекты, выполнявшие загрузку сборок в процессе экспорта метаинформации.  
---|---  
[Items](P_Tessa_Platform_Composition_IAssemblyLoaderResult_1_Items.htm)| Вся
экспортированная метаинформация.  
[Options](P_Tessa_Platform_Composition_IAssemblyLoaderResult_1_Options.htm)|
Настройки, использованные при экспорте метаинформации.  
##  __См. также
#### Ссылки
[Tessa.Platform.Composition - пространство
имён](N_Tessa_Platform_Composition.htm)
