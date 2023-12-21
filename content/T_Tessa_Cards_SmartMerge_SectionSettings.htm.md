# SectionSettings - класс
Параметры слияния для конкретной секции
## __Definition
 **Пространство имён:** [Tessa.Cards.SmartMerge](N_Tessa_Cards_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public class SectionSettings : StorageSerializable
VB __Копировать
    <SerializableAttribute>
    <DataContractAttribute>
    Public Class SectionSettings
    	Inherits StorageSerializable
C++ __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public ref class SectionSettings : public StorageSerializable
F# __Копировать
     [<SerializableAttribute>]
    [<DataContractAttribute>]
    type SectionSettings = 
        class
            inherit StorageSerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm) __ SectionSettings
##  __Конструкторы
[SectionSettings()](M_Tessa_Cards_SmartMerge_SectionSettings__ctor.htm)|
Инициализирует новый экземпляр класса SectionSettings  
---|---  
[SectionSettings(String, IReadOnlyList<String>, IReadOnlyList<String>,
IReadOnlyList<String>, IReadOnlyList<String>, Boolean,
Nullable<Boolean>)](M_Tessa_Cards_SmartMerge_SectionSettings__ctor_1.htm)|
Инициализирует новый экземпляр класса SectionSettings  
##  __Свойства
[ExcludedColumns](P_Tessa_Cards_SmartMerge_SectionSettings_ExcludedColumns.htm)|
Исключенные колонки. Если заполнены, то значения узлов слияния, относящихся к
данной секции, будут сравниваться исключая эти колонки. Имеют приоритет перед
IncludedColumns. Если ExcludedColumns и IncludedColumns заполнены
одновременно, выдается Warning в ValidationResult.  
---|---  
[Ignored](P_Tessa_Cards_SmartMerge_SectionSettings_Ignored.htm)|  Указывает на
то что секция игнорируется при слиянии  
[IgnoredColumns](P_Tessa_Cards_SmartMerge_SectionSettings_IgnoredColumns.htm)|
Игнорируемые колонки. Поведение такое же как и у параметра ExcludedColumns
(дополняют друг друга), но в дополнение к логике параметра ExcludedColumns,
колонки, указанные в этом параметре, будут проигнорированы при апдейте узлов.  
[IgnoreDuplicateRows](P_Tessa_Cards_SmartMerge_SectionSettings_IgnoreDuplicateRows.htm)|
Отвечает за логику в случае более одного совпадения по ключевым полям на одном
"тир-уровне", имеет приоритет над общим одноименным флагом, установленным для
опций.  
[IncludedColumns](P_Tessa_Cards_SmartMerge_SectionSettings_IncludedColumns.htm)|
Включенные колонки. Если заполнены, то значения узлов слияния, относящихся к
данной секции, будут сравниваться только с учетом этих колонок.  
[KeyColumns](P_Tessa_Cards_SmartMerge_SectionSettings_KeyColumns.htm)|
Ключевые колонки. Если заполнены, то помимо RowID на первом уровне
сопоставления, на втором уровне объекты будут сопоставляться по этим ключевым
колонкам.  
[Name](P_Tessa_Cards_SmartMerge_SectionSettings_Name.htm)|  Наименование
секции  
## __Методы
[Deserialize](M_Tessa_Platform_Storage_StorageSerializable_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
---|---  
[DeserializeAndGetCore](M_Tessa_Platform_Storage_StorageSerializable_DeserializeAndGetCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeCore](M_Tessa_Cards_SmartMerge_SectionSettings_DeserializeCore.htm)|  
(Переопределяет [StorageSerializable.DeserializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_DeserializeCore.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Serialize](M_Tessa_Platform_Storage_StorageSerializable_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[SerializeCore](M_Tessa_Cards_SmartMerge_SectionSettings_SerializeCore.htm)|  
(Переопределяет [StorageSerializable.SerializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_SerializeCore.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Cards.SmartMerge - пространство имён](N_Tessa_Cards_SmartMerge.htm)
