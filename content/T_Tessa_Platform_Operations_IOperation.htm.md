# IOperation - интерфейс
Операция.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Operations](N_Tessa_Platform_Operations.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IOperation : IBinarySerializable, 
    	IStorageSerializable
VB __Копировать
     Public Interface IOperation
    	Inherits IBinarySerializable, IStorageSerializable
C++ __Копировать
     public interface class IOperation : IBinarySerializable, 
    	IStorageSerializable
F# __Копировать
     type IOperation = 
        interface
            interface IBinarySerializable
            interface IStorageSerializable
        end
Implements
    [IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm), [IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm)
##  __Свойства
[Completed](P_Tessa_Platform_Operations_IOperation_Completed.htm)|  Дата и
время окончания операции в UTC или null, если операция ещё не завершена.  
---|---  
[Created](P_Tessa_Platform_Operations_IOperation_Created.htm)| Дата и время
создания операции в UTC.  
[CreatedByID](P_Tessa_Platform_Operations_IOperation_CreatedByID.htm)|
Идентификатор пользователя, создавшего запрос на операцию.  
[CreatedByName](P_Tessa_Platform_Operations_IOperation_CreatedByName.htm)| Имя
пользователя, создавшего запрос на операцию.  
[Digest](P_Tessa_Platform_Operations_IOperation_Digest.htm)| Краткое описание
операции.  
[ID](P_Tessa_Platform_Operations_IOperation_ID.htm)| Идентификатор операции.  
[InProgress](P_Tessa_Platform_Operations_IOperation_InProgress.htm)|  Дата и
время начала выполнения операции в UTC или null, если выполнение операции ещё
не начато.  
[Progress](P_Tessa_Platform_Operations_IOperation_Progress.htm)|  Процент
выполнения операции от 0 до 100 или null, если операция не сообщает процент
своей готовности.  
[ReportsProgress](P_Tessa_Platform_Operations_IOperation_ReportsProgress.htm)|
Признак того, что операция сообщает о проценте своей готовности в свойстве
[Tessa.Platform.Operations.IOperation.Progress].  
[Request](P_Tessa_Platform_Operations_IOperation_Request.htm)|  Запрос на
выполнение операции или null, если для выполнения операции не требуется
запрос.  
[RequestHash](P_Tessa_Platform_Operations_IOperation_RequestHash.htm)|  Хеш,
посчитанный для данных в запросе Request, или null, если для выполнения
операции не требуется запрос. Для расчёта обычно используется функция
хеширования HMAC-SHA256, размер хеша в которой 256 бит или 32 байта. Расчёт
выполняется автоматически в момент создания операции. Заполнять поле вручную
не рекомендуется.  
[Response](P_Tessa_Platform_Operations_IOperation_Response.htm)|  Результат
выполнения операции или null, если операция ещё не завершена или для операции
недоступна информация о результате.  
[State](P_Tessa_Platform_Operations_IOperation_State.htm)| Состояние операции.  
[TypeID](P_Tessa_Platform_Operations_IOperation_TypeID.htm)|  Идентификатор
типа операции. Должен быть добавлен в перечисление OperationTypes.  
## __Методы
[Deserialize(BinaryReader)](M_Tessa_Platform_IBinarySerializable_Deserialize.htm)|
Десериализует объект из бинарной формы.  
(Унаследован от
[IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm))  
---|---  
[Deserialize(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_IStorageSerializable_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm))  
[Serialize(BinaryWriter)](M_Tessa_Platform_IBinarySerializable_Serialize.htm)|
Сериализует объект в бинарной форме.  
(Унаследован от
[IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm))  
[Serialize(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_IStorageSerializable_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Унаследован от
[IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm))  
##  __Методы расширения
[ConvertOperationToStorage](M_Tessa_Web_Client_Helpers_CommonExtensions_ConvertOperationToStorage.htm)|  
(Определяется
[CommonExtensions](T_Tessa_Web_Client_Helpers_CommonExtensions.htm))  
---|---  
[ToSerializedDictionary](M_Tessa_Platform_Storage_StorageExtensions_ToSerializedDictionary.htm)|
Сериализует объект в нетипизированный словарь.  
(Определяется
[StorageExtensions](T_Tessa_Platform_Storage_StorageExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Operations - пространство
имён](N_Tessa_Platform_Operations.htm)
