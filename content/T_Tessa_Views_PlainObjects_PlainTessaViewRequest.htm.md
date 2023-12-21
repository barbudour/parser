# PlainTessaViewRequest - класс
PDO для запроса на просмотр представления. Объект используется для
сериализации в Json или Storage.
## __Definition
 **Пространство имён:**
[Tessa.Views.PlainObjects](N_Tessa_Views_PlainObjects.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public class PlainTessaViewRequest : StorageSerializable
VB __Копировать
    <SerializableAttribute>
    <DataContractAttribute>
    Public Class PlainTessaViewRequest
    	Inherits StorageSerializable
C++ __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public ref class PlainTessaViewRequest : public StorageSerializable
F# __Копировать
     [<SerializableAttribute>]
    [<DataContractAttribute>]
    type PlainTessaViewRequest = 
        class
            inherit StorageSerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm) __ PlainTessaViewRequest
##  __Конструкторы
[PlainTessaViewRequest()](M_Tessa_Views_PlainObjects_PlainTessaViewRequest__ctor.htm)|
Конструктор без параметров.  
---|---  
[PlainTessaViewRequest(ITessaViewRequest)](M_Tessa_Views_PlainObjects_PlainTessaViewRequest__ctor_1.htm)|
Конструктор с передачей запроса на просмотр представления.  
## __Свойства
[CalculateRowCounting](P_Tessa_Views_PlainObjects_PlainTessaViewRequest_CalculateRowCounting.htm)|
Признак необходимости подсчета количества строк.  
---|---  
[ExecutionTimeOut](P_Tessa_Views_PlainObjects_PlainTessaViewRequest_ExecutionTimeOut.htm)|
Тайм-аут выполнения запроса.  
[SkipErrorLogging](P_Tessa_Views_PlainObjects_PlainTessaViewRequest_SkipErrorLogging.htm)|
Возвращает или задаёт значение, показывающее, должны ли логироваться ошибки
выполнения представлений в карточке ошибок.  
[SortingColumns](P_Tessa_Views_PlainObjects_PlainTessaViewRequest_SortingColumns.htm)|
Список колонок сортировки.  
[SubsetName](P_Tessa_Views_PlainObjects_PlainTessaViewRequest_SubsetName.htm)|
Имя вызываемого подмножества представления.  
[Values](P_Tessa_Views_PlainObjects_PlainTessaViewRequest_Values.htm)|  Список
значений параметров.  
[ViewAlias](P_Tessa_Views_PlainObjects_PlainTessaViewRequest_ViewAlias.htm)|
Псевдоним представления  
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
[DeserializeCore](M_Tessa_Views_PlainObjects_PlainTessaViewRequest_DeserializeCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
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
[SerializeCore](M_Tessa_Views_PlainObjects_PlainTessaViewRequest_SerializeCore.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Переопределяет [StorageSerializable.SerializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_SerializeCore.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToTessaViewRequest](M_Tessa_Views_PlainObjects_PlainTessaViewRequest_ToTessaViewRequest.htm)|
Извлечение запроса на просмотр представления.  
## __Методы расширения
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
[Tessa.Views.PlainObjects - пространство имён](N_Tessa_Views_PlainObjects.htm)
