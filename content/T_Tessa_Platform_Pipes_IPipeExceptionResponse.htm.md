# IPipeExceptionResponse - интерфейс
Ответ на запрос по каналу, используемый при возникновении исключения на
сервере.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeExceptionResponse : IPipeResponse, 
    	IPipeMessage, ISealable
VB __Копировать
     Public Interface IPipeExceptionResponse
    	Inherits IPipeResponse, IPipeMessage, ISealable
C++ __Копировать
     public interface class IPipeExceptionResponse : IPipeResponse, 
    	IPipeMessage, ISealable
F# __Копировать
     type IPipeExceptionResponse = 
        interface
            interface IPipeResponse
            interface IPipeMessage
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [IPipeMessage](T_Tessa_Platform_Pipes_IPipeMessage.htm), [IPipeResponse](T_Tessa_Platform_Pipes_IPipeResponse.htm)
##  __Свойства
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
---|---  
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
[SetException](M_Tessa_Platform_Pipes_IPipeExceptionResponse_SetException.htm)|
Устанавливает исключение для отправки по каналу в ответе на запрос.  
[TryGetException](M_Tessa_Platform_Pipes_IPipeExceptionResponse_TryGetException.htm)|
Возвращает исключение, установленное или полученное по каналу в ответе на
запрос, или null, если исключение не задано.  
## __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
