# IPipeBinaryMessage - интерфейс
Сообщение, содержащее массив байт, который записывается после основного
сообщения отдельным сообщением.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeBinaryMessage : IPipeMessage, 
    	ISealable
VB __Копировать
     Public Interface IPipeBinaryMessage
    	Inherits IPipeMessage, ISealable
C++ __Копировать
     public interface class IPipeBinaryMessage : IPipeMessage, 
    	ISealable
F# __Копировать
     type IPipeBinaryMessage = 
        interface
            interface IPipeMessage
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [IPipeMessage](T_Tessa_Platform_Pipes_IPipeMessage.htm)
##  __Свойства
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm)|
Массив байт, который записывается после основного сообщения отдельным
сообщением. Для такого сообщения содержимое не кодируется в виде строки и
передаётся в исходном виде.  
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
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Item](P_Tessa_Platform_Pipes_IPipeMessage_Item.htm)|  Возвращает или
устанавливает параметр сообщения по заданному ключу. Если параметр
отсутствует, то возвращает null.  
(Унаследован от [IPipeMessage](T_Tessa_Platform_Pipes_IPipeMessage.htm))  
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
для сообщения IPipeBinaryMessage на основании текущего значения свойства
[BinaryData](P_Tessa_Platform_Pipes_IPipeBinaryMessage_BinaryData.htm). Этот
метод автоматически вызывается перед отправкой сообщения по каналу, вызывать
его вручную не требуется.  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
