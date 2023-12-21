# PlainTessaViewResult - класс
PDO результата выполнения запроса к представлению. Объект используется для
сериализации в Json или Storage.
## __Definition
 **Пространство имён:**
[Tessa.Views.PlainObjects](N_Tessa_Views_PlainObjects.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public class PlainTessaViewResult : StorageSerializable
VB __Копировать
    <SerializableAttribute>
    <DataContractAttribute>
    Public Class PlainTessaViewResult
    	Inherits StorageSerializable
C++ __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public ref class PlainTessaViewResult : public StorageSerializable
F# __Копировать
     [<SerializableAttribute>]
    [<DataContractAttribute>]
    type PlainTessaViewResult = 
        class
            inherit StorageSerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm) __ PlainTessaViewResult
##  __Конструкторы
[PlainTessaViewResult()](M_Tessa_Views_PlainObjects_PlainTessaViewResult__ctor.htm)|
Конструктор без параметров.  
---|---  
[PlainTessaViewResult(ITessaViewResult)](M_Tessa_Views_PlainObjects_PlainTessaViewResult__ctor_1.htm)|
Конструктор с передачей результата выполнения запроса к представлению.  
## __Свойства
[Columns](P_Tessa_Views_PlainObjects_PlainTessaViewResult_Columns.htm)|
Список колонок.  
---|---  
[DataTypes](P_Tessa_Views_PlainObjects_PlainTessaViewResult_DataTypes.htm)|
Список типов данных SQL. Рекомендуется использовать
[SchemeTypes](P_Tessa_Views_PlainObjects_PlainTessaViewResult_SchemeTypes.htm)
для обработки типов данных, не связанных с конкретной СУБД.  
Устарело.  
[RowCount](P_Tessa_Views_PlainObjects_PlainTessaViewResult_RowCount.htm)|
Количество строк, которое доступно в запросе. Данное количество, строк
является расчетным и не всегда равно количеству строк в
[Rows](P_Tessa_Views_PlainObjects_PlainTessaViewResult_Rows.htm).  
[Rows](P_Tessa_Views_PlainObjects_PlainTessaViewResult_Rows.htm)|  Строки
таблицы.  
[SchemeTypes](P_Tessa_Views_PlainObjects_PlainTessaViewResult_SchemeTypes.htm)|
Список типов данных.  
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
[DeserializeCore](M_Tessa_Views_PlainObjects_PlainTessaViewResult_DeserializeCore.htm)|
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
[SerializeCore](M_Tessa_Views_PlainObjects_PlainTessaViewResult_SerializeCore.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Переопределяет [StorageSerializable.SerializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_SerializeCore.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToTessaViewResult](M_Tessa_Views_PlainObjects_PlainTessaViewResult_ToTessaViewResult.htm)|
Извлечение результата выполнения запроса к представлению.  
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
