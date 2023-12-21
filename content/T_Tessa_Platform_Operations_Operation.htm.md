# Operation - класс
Операция.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Operations](N_Tessa_Platform_Operations.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class Operation : StorageSerializable, 
    	IOperation, IBinarySerializable, IStorageSerializable
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class Operation
    	Inherits StorageSerializable
    	Implements IOperation, IBinarySerializable, IStorageSerializable
C++ __Копировать
    [SerializableAttribute]
    public ref class Operation sealed : public StorageSerializable, 
    	IOperation, IBinarySerializable, IStorageSerializable
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type Operation = 
        class
            inherit StorageSerializable
            interface IOperation
            interface IBinarySerializable
            interface IStorageSerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm) __ Operation
Implements
    [IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm), [IOperation](T_Tessa_Platform_Operations_IOperation.htm), [IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm)
##  __Конструкторы
[Operation()](M_Tessa_Platform_Operations_Operation__ctor.htm)| Создаёт
экземпляр класса с параметрами по умолчанию.  
---|---  
[Operation(IOperation)](M_Tessa_Platform_Operations_Operation__ctor_1.htm)|
Создаёт экземпляр класса с указанием операции, свойства которой используются
для инициализации создаваемого объекта.  
## __Свойства
[Completed](P_Tessa_Platform_Operations_Operation_Completed.htm)|  Дата и
время окончания операции в UTC или null, если операция ещё не завершена.  
---|---  
[Created](P_Tessa_Platform_Operations_Operation_Created.htm)| Дата и время
создания операции в UTC.  
[CreatedByID](P_Tessa_Platform_Operations_Operation_CreatedByID.htm)|
Идентификатор пользователя, создавшего запрос на операцию.  
[CreatedByName](P_Tessa_Platform_Operations_Operation_CreatedByName.htm)| Имя
пользователя, создавшего запрос на операцию.  
[Digest](P_Tessa_Platform_Operations_Operation_Digest.htm)| Краткое описание
операции.  
[ID](P_Tessa_Platform_Operations_Operation_ID.htm)| Идентификатор операции.  
[InProgress](P_Tessa_Platform_Operations_Operation_InProgress.htm)|  Дата и
время начала выполнения операции в UTC или null, если выполнение операции ещё
не начато.  
[Progress](P_Tessa_Platform_Operations_Operation_Progress.htm)|  Процент
выполнения операции от 0 до 100 или null, если операция не сообщает процент
своей готовности.  
[ReportsProgress](P_Tessa_Platform_Operations_Operation_ReportsProgress.htm)|
Признак того, что операция сообщает о проценте своей готовности в свойстве
[Tessa.Platform.Operations.IOperation.Progress].  
[Request](P_Tessa_Platform_Operations_Operation_Request.htm)|  Запрос на
выполнение операции или null, если для выполнения операции не требуется
запрос.  
[RequestHash](P_Tessa_Platform_Operations_Operation_RequestHash.htm)|  Хеш,
посчитанный для данных в запросе Request, или null, если для выполнения
операции не требуется запрос. Для расчёта обычно используется функция
хеширования HMAC-SHA256, размер хеша в которой 256 бит или 32 байта. Расчёт
выполняется автоматически в момент создания операции. Заполнять поле вручную
не рекомендуется.  
[Response](P_Tessa_Platform_Operations_Operation_Response.htm)|  Результат
выполнения операции или null, если операция ещё не завершена или для операции
недоступна информация о результате.  
[State](P_Tessa_Platform_Operations_Operation_State.htm)| Состояние операции.  
[TypeID](P_Tessa_Platform_Operations_Operation_TypeID.htm)|  Идентификатор
типа операции. Должен быть добавлен в перечисление OperationTypes.  
## __Методы
[Deserialize(BinaryReader)](M_Tessa_Platform_Operations_Operation_Deserialize.htm)|
Десериализует объект из бинарной формы.  
---|---  
[Deserialize(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeAndGetCore](M_Tessa_Platform_Storage_StorageSerializable_DeserializeAndGetCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeCore](M_Tessa_Platform_Operations_Operation_DeserializeCore.htm)|
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
[Serialize(BinaryWriter)](M_Tessa_Platform_Operations_Operation_Serialize.htm)|
Сериализует объект в бинарной форме.  
[Serialize(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[SerializeCore](M_Tessa_Platform_Operations_Operation_SerializeCore.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Переопределяет [StorageSerializable.SerializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_SerializeCore.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[ConvertOperationToStorage](M_Tessa_Web_Client_Helpers_CommonExtensions_ConvertOperationToStorage.htm)|  
(Определяется
[CommonExtensions](T_Tessa_Web_Client_Helpers_CommonExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[Tessa.Platform.Operations - пространство
имён](N_Tessa_Platform_Operations.htm)
