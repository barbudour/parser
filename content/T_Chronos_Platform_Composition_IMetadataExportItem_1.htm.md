# IMetadataExportItem<TMetadata> \- интерфейс
Объект, описывающий экспортированные из сборки метаданные.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IMetadataExportItem<out TMetadata>
VB __Копировать
     Public Interface IMetadataExportItem(Of Out TMetadata)
C++ __Копировать
    generic<typename TMetadata>
    public interface class IMetadataExportItem
F# __Копировать
     type IMetadataExportItem<'TMetadata> = interface end
#### Параметры типа
TMetadata
     Тип экспортируемых метаданных. Может реализовывать интерфейс [ISerializableMetadata<TMetadata>](T_Chronos_Contracts_ISerializableMetadata_1.htm) для сериализации. 
## __Свойства
[AssemblyFilePath](P_Chronos_Platform_Composition_IMetadataExportItem_1_AssemblyFilePath.htm)|
Путь к файлу со сборкой.  
---|---  
[AssemblyFullName](P_Chronos_Platform_Composition_IMetadataExportItem_1_AssemblyFullName.htm)|
Полное имя сборки.  
[AssemblyQualifiedTypeName](P_Chronos_Platform_Composition_IMetadataExportItem_1_AssemblyQualifiedTypeName.htm)|
Квалифицированное имя типа, которое включает имя сборки.  
[ImplementedInterfaceTypes](P_Chronos_Platform_Composition_IMetadataExportItem_1_ImplementedInterfaceTypes.htm)|
Типы интерфейсов, которые реализует экспортированный тип. Типы всех
проверяемых интерфейсов должны быть указаны при экспорте.  
[Metadata](P_Chronos_Platform_Composition_IMetadataExportItem_1_Metadata.htm)|
Экспортированная метаинформация.  
[ResolveAssemblyFunc](P_Chronos_Platform_Composition_IMetadataExportItem_1_ResolveAssemblyFunc.htm)|
Функция, выполняющая загрузку сборки, в которой размещается тип, или null,
если загруженная сборка недоступна.  
[TypeFullName](P_Chronos_Platform_Composition_IMetadataExportItem_1_TypeFullName.htm)|
Полное имя типа без указания сборки.  
##  __Методы
[TypeImplements<T>](M_Chronos_Platform_Composition_IMetadataExportItem_1_TypeImplements__1.htm)|
Возвращает признак того, что экспортированный тип реализует указанный
интерфейс.  
---|---  
##  __См. также
#### Ссылки
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
