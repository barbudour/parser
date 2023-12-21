# CardMergeOptions - класс
Реализация параметров слияния для объектов Card
## __Definition
 **Пространство имён:** [Tessa.Cards.SmartMerge](N_Tessa_Cards_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public class CardMergeOptions : MergeOptions, 
    	ICardMergeOptions, IMergeOptions, IStorageSerializable
VB __Копировать
    <SerializableAttribute>
    <DataContractAttribute>
    Public Class CardMergeOptions
    	Inherits MergeOptions
    	Implements ICardMergeOptions, IMergeOptions, IStorageSerializable
C++ __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public ref class CardMergeOptions : public MergeOptions, 
    	ICardMergeOptions, IMergeOptions, IStorageSerializable
F# __Копировать
     [<SerializableAttribute>]
    [<DataContractAttribute>]
    type CardMergeOptions = 
        class
            inherit MergeOptions
            interface ICardMergeOptions
            interface IMergeOptions
            interface IStorageSerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm) __[MergeOptions](T_Tessa_SmartMerge_MergeOptions.htm) __ CardMergeOptions
Implements
    [ICardMergeOptions](T_Tessa_Cards_SmartMerge_ICardMergeOptions.htm), [IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm), [IMergeOptions](T_Tessa_SmartMerge_IMergeOptions.htm)
##  __Конструкторы
[CardMergeOptions()](M_Tessa_Cards_SmartMerge_CardMergeOptions__ctor.htm)|
Инициализирует новый экземпляр класса CardMergeOptions  
---|---  
[CardMergeOptions(IEnumerable<SectionSettings>, FileSettings, Boolean,
Boolean)](M_Tessa_Cards_SmartMerge_CardMergeOptions__ctor_1.htm)|
Инициализирует новый экземпляр класса CardMergeOptions  
##  __Свойства
[FileSettings](P_Tessa_Cards_SmartMerge_CardMergeOptions_FileSettings.htm)|
Параметры слияния для прикрепленных файлов  
---|---  
[IgnoreDuplicateRows](P_Tessa_SmartMerge_MergeOptions_IgnoreDuplicateRows.htm)|
Отвечает за логику в случае более одного совпадения по ключевым полям на одном
"тир-уровне", true - игнорировать дубликаты, false - инсертить дубликаты с
занесением в WarningValidationResult  
(Унаследован от [MergeOptions](T_Tessa_SmartMerge_MergeOptions.htm))  
[SectionsSettings](P_Tessa_Cards_SmartMerge_CardMergeOptions_SectionsSettings.htm)|
Список параметров слияния для секций  
[SkipIfCardExists](P_Tessa_Cards_SmartMerge_CardMergeOptions_SkipIfCardExists.htm)|
Пропустить импорт, если карточка уже существует в БД.  
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
[DeserializeCore](M_Tessa_Cards_SmartMerge_CardMergeOptions_DeserializeCore.htm)|  
(Переопределяет [MergeOptions.DeserializeCore(Dictionary<String,
Object>)](M_Tessa_SmartMerge_MergeOptions_DeserializeCore.htm))  
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
[SerializeCore](M_Tessa_Cards_SmartMerge_CardMergeOptions_SerializeCore.htm)|  
(Переопределяет [MergeOptions.SerializeCore(Dictionary<String,
Object>)](M_Tessa_SmartMerge_MergeOptions_SerializeCore.htm))  
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
[ToSerializedDictionary](M_Tessa_Platform_Storage_StorageExtensions_ToSerializedDictionary.htm)|
Сериализует объект в нетипизированный словарь.  
(Определяется
[StorageExtensions](T_Tessa_Platform_Storage_StorageExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.SmartMerge - пространство имён](N_Tessa_Cards_SmartMerge.htm)
