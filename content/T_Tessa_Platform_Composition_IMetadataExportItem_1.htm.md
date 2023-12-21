# IMetadataExportItem<TMetadata> \- интерфейс
Объект, описывающий экспортированные из сборки метаданные.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Composition](N_Tessa_Platform_Composition.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
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
     Тип экспортируемых метаданных. Может реализовывать интерфейс [ISerializableMetadata<TMetadata>](T_Tessa_Platform_Composition_ISerializableMetadata_1.htm) для сериализации. 
## __Свойства
[Assembly](P_Tessa_Platform_Composition_IMetadataExportItem_1_Assembly.htm)|
Сборка, в которой размещается тип, или null, если загруженная сборка
недоступна.  
---|---  
[AssemblyFilePath](P_Tessa_Platform_Composition_IMetadataExportItem_1_AssemblyFilePath.htm)|
Путь к файлу со сборкой.  
[AssemblyFullName](P_Tessa_Platform_Composition_IMetadataExportItem_1_AssemblyFullName.htm)|
Полное имя сборки.  
[AssemblyQualifiedTypeName](P_Tessa_Platform_Composition_IMetadataExportItem_1_AssemblyQualifiedTypeName.htm)|
Квалифицированное имя типа, которое включает имя сборки.  
[ImplementedInterfaceTypes](P_Tessa_Platform_Composition_IMetadataExportItem_1_ImplementedInterfaceTypes.htm)|
Типы интерфейсов, которые реализует экспортированный тип. Типы всех
проверяемых интерфейсов должны быть указаны при экспорте.  
[Metadata](P_Tessa_Platform_Composition_IMetadataExportItem_1_Metadata.htm)|
Экспортированная метаинформация.  
[TypeFullName](P_Tessa_Platform_Composition_IMetadataExportItem_1_TypeFullName.htm)|
Полное имя типа без указания сборки.  
##  __Методы
[TypeImplements<T>](M_Tessa_Platform_Composition_IMetadataExportItem_1_TypeImplements__1.htm)|
Возвращает признак того, что экспортированный тип реализует указанный
интерфейс.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Composition - пространство
имён](N_Tessa_Platform_Composition.htm)
