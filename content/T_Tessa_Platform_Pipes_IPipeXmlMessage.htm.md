# IPipeXmlMessage - интерфейс
Сообщение, передаваемое по каналу с возможностью XML-сериализации.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeXmlMessage : IPipeMessage, 
    	ISealable
VB __Копировать
     Public Interface IPipeXmlMessage
    	Inherits IPipeMessage, ISealable
C++ __Копировать
     public interface class IPipeXmlMessage : IPipeMessage, 
    	ISealable
F# __Копировать
     type IPipeXmlMessage = 
        interface
            interface IPipeMessage
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [IPipeMessage](T_Tessa_Platform_Pipes_IPipeMessage.htm)
##  __Свойства
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
---|---  
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
[DeserializeFromXml](M_Tessa_Platform_Pipes_IPipeXmlMessage_DeserializeFromXml.htm)|
Десериализует сообщение из формы XML.  
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
[SerializeToXml](M_Tessa_Platform_Pipes_IPipeXmlMessage_SerializeToXml.htm)|
Сериализует сообщение в форме XML.  
## __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
