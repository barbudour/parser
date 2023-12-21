# MetadataExportItem<TMetadata> \- класс
Объект, описывающий экспортированные из сборки метаданные.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public class MetadataExportItem<TMetadata> : IMetadataExportItem<TMetadata>
VB __Копировать
    <SerializableAttribute>
    Public Class MetadataExportItem(Of TMetadata)
    	Implements IMetadataExportItem(Of TMetadata)
C++ __Копировать
    [SerializableAttribute]
    generic<typename TMetadata>
    public ref class MetadataExportItem : IMetadataExportItem<TMetadata>
F# __Копировать
     [<SerializableAttribute>]
    type MetadataExportItem<'TMetadata> = 
        class
            interface IMetadataExportItem<'TMetadata>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ MetadataExportItem<TMetadata>
Implements
    [IMetadataExportItem](T_Chronos_Platform_Composition_IMetadataExportItem_1.htm)<TMetadata>
#### Параметры типа
TMetadata
     Тип экспортируемых метаданных. Может реализовывать интерфейс [ISerializableMetadata<TMetadata>](T_Chronos_Contracts_ISerializableMetadata_1.htm) для сериализации. 
## __Заметки
Наследники класса могут добавлять свойства.
## __Конструкторы
[MetadataExportItem<TMetadata>](M_Chronos_Platform_Composition_MetadataExportItem_1__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[AssemblyFilePath](P_Chronos_Platform_Composition_MetadataExportItem_1_AssemblyFilePath.htm)|
Путь к файлу со сборкой.  
---|---  
[AssemblyFullName](P_Chronos_Platform_Composition_MetadataExportItem_1_AssemblyFullName.htm)|
Полное имя сборки.  
[AssemblyQualifiedTypeName](P_Chronos_Platform_Composition_MetadataExportItem_1_AssemblyQualifiedTypeName.htm)|
Квалифицированное имя типа, которое включает имя сборки.  
[ImplementedInterfaceTypes](P_Chronos_Platform_Composition_MetadataExportItem_1_ImplementedInterfaceTypes.htm)|
Типы интерфейсов, которые реализует экспортированный тип. Типы всех
проверяемых интерфейсов должны быть указаны при экспорте.  
[Metadata](P_Chronos_Platform_Composition_MetadataExportItem_1_Metadata.htm)|
Экспортированная метаинформация.  
[ResolveAssemblyFunc](P_Chronos_Platform_Composition_MetadataExportItem_1_ResolveAssemblyFunc.htm)|
Функция, выполняющая загрузку сборки, в которой размещается тип, или null,
если загруженная сборка недоступна.  
[TypeFullName](P_Chronos_Platform_Composition_MetadataExportItem_1_TypeFullName.htm)|
Полное имя типа без указания сборки.  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TypeImplements<T>](M_Chronos_Platform_Composition_MetadataExportItem_1_TypeImplements__1.htm)|
Возвращает признак того, что экспортированный тип реализует указанный
интерфейс.  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
