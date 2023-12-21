# IPipeBinaryResponse - интерфейс
Сообщение-ответ, полученное по каналу, для которого дополнительно загружается
массив байт отдельным сообщением
[IPipeBinaryMessage](T_Tessa_Platform_Pipes_IPipeBinaryMessage.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeBinaryResponse : IPipeResponse, 
    	IPipeMessage, ISealable, IPipeBinaryMessage
VB __Копировать
     Public Interface IPipeBinaryResponse
    	Inherits IPipeResponse, IPipeMessage, ISealable, IPipeBinaryMessage
C++ __Копировать
     public interface class IPipeBinaryResponse : IPipeResponse, 
    	IPipeMessage, ISealable, IPipeBinaryMessage
F# __Копировать
     type IPipeBinaryResponse = 
        interface
            interface IPipeResponse
            interface IPipeMessage
            interface ISealable
            interface IPipeBinaryMessage
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [IPipeBinaryMessage](T_Tessa_Platform_Pipes_IPipeBinaryMessage.htm), [IPipeMessage](T_Tessa_Platform_Pipes_IPipeMessage.htm), [IPipeResponse](T_Tessa_Platform_Pipes_IPipeResponse.htm)
##  __Свойства
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm)|
Массив байт, который записывается после основного сообщения отдельным
сообщением. Для такого сообщения содержимое не кодируется в виде строки и
передаётся в исходном виде.  
(Унаследован от
[IPipeBinaryMessage](T_Tessa_Platform_Pipes_IPipeBinaryMessage.htm))  
---|---  
[HasBinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_HasBinaryData.htm)|
Признак того, что в массиве
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm)
содержатся данные. При чтении сообщения возвращает null, если
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm) равен
null, false, если
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm) равен
пустому массиву, или true, если
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm)
содержит действительные данные. При отправке сообщения это значение
устанавливается автоматически, поэтому устанавливать его вручную
необязательно.  
(Унаследован от
[IPipeBinaryMessage](T_Tessa_Platform_Pipes_IPipeBinaryMessage.htm))  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Item](P_Tessa_Platform_Pipes_IPipeMessage_Item.htm)|  Возвращает или
устанавливает параметр сообщения по заданному ключу. Если параметр
отсутствует, то возвращает null.  
(Унаследован от [IPipeMessage](T_Tessa_Platform_Pipes_IPipeMessage.htm))  
[Value](P_Tessa_Platform_Pipes_IPipeResponse_Value.htm)|  Основное значение,
полученное в ответе на запрос. Это аналог значения, возвращаемого методом в
выражении return.  
(Унаследован от [IPipeResponse](T_Tessa_Platform_Pipes_IPipeResponse.htm))  
##  __Методы
[ClearValues](M_Tessa_Platform_Pipes_IPipeMessage_ClearValues.htm)|  Удаляет
все параметры сообщения, установленные ранее.  
(Унаследован от [IPipeMessage](T_Tessa_Platform_Pipes_IPipeMessage.htm))  
---|---  
[ContainsValue](M_Tessa_Platform_Pipes_IPipeMessage_ContainsValue.htm)|
Возвращает признак того, что заданный параметр присутствует в сообщении.  
(Унаследован от [IPipeMessage](T_Tessa_Platform_Pipes_IPipeMessage.htm))  
[Deserialize](M_Tessa_Platform_Pipes_IPipeMessage_Deserialize.htm)|
Десериализует сообщение из строковой формы.  
(Унаследован от [IPipeMessage](T_Tessa_Platform_Pipes_IPipeMessage.htm))  
[GetValues](M_Tessa_Platform_Pipes_IPipeMessage_GetValues.htm)|  Возвращает
список параметров в сообщении с указанием имени параметра и его значения.  
(Унаследован от [IPipeMessage](T_Tessa_Platform_Pipes_IPipeMessage.htm))  
[RemoveValue](M_Tessa_Platform_Pipes_IPipeMessage_RemoveValue.htm)|  Удаляет
параметр из сообщения. Возвращает признак того, что он присутствовал и был
удалён.  
(Унаследован от [IPipeMessage](T_Tessa_Platform_Pipes_IPipeMessage.htm))  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Serialize](M_Tessa_Platform_Pipes_IPipeMessage_Serialize.htm)|  Сериализует
сообщение в строковой форме.  
(Унаследован от [IPipeMessage](T_Tessa_Platform_Pipes_IPipeMessage.htm))  
##  __Методы расширения
[UpdateHasBinaryData](M_Tessa_Platform_Pipes_PipesExtensions_UpdateHasBinaryData.htm)|
Обновляет свойство
[HasBinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_HasBinaryData.htm)
для сообщения
[IPipeBinaryMessage](T_Tessa_Platform_Pipes_IPipeBinaryMessage.htm) на
основании текущего значения свойства
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm). Этот
метод автоматически вызывается перед отправкой сообщения по каналу, вызывать
его вручную не требуется.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
