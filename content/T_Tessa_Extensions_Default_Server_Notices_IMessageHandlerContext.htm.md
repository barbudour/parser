# IMessageHandlerContext - интерфейс
Контекст операции обработки сообщения мобильного согласования
[IMessageHandler](T_Tessa_Extensions_Default_Server_Notices_IMessageHandler.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Notices](N_Tessa_Extensions_Default_Server_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IMessageHandlerContext
VB __Копировать
     Public Interface IMessageHandlerContext
C++ __Копировать
     public interface class IMessageHandlerContext
F# __Копировать
     type IMessageHandlerContext = interface end
##  __Свойства
[BuilderFactory](P_Tessa_Extensions_Default_Server_Notices_IMessageHandlerContext_BuilderFactory.htm)|
Объект для генерации запросов к базе данных.  
---|---  
[Cancel](P_Tessa_Extensions_Default_Server_Notices_IMessageHandlerContext_Cancel.htm)|
Признак того, что сохранение карточки
[Card](P_Tessa_Extensions_Default_Server_Notices_IMessageHandlerContext_Card.htm)
будет отменено. По умолчанию false.  
[CancellationToken](P_Tessa_Extensions_Default_Server_Notices_IMessageHandlerContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
[Card](P_Tessa_Extensions_Default_Server_Notices_IMessageHandlerContext_Card.htm)|
Карточка, с которой производятся действия, или null, если карточка недоступна.  
[Db](P_Tessa_Extensions_Default_Server_Notices_IMessageHandlerContext_Db.htm)|
Объект для взаимодействия с базой данных.  
[Info](P_Tessa_Extensions_Default_Server_Notices_IMessageHandlerContext_Info.htm)|
Информация, разобранная из сообщения.  
[Message](P_Tessa_Extensions_Default_Server_Notices_IMessageHandlerContext_Message.htm)|
Обрабатываемое сообщение.  
[Session](P_Tessa_Extensions_Default_Server_Notices_IMessageHandlerContext_Session.htm)|
Сессия текущего пользователя.  
[Task](P_Tessa_Extensions_Default_Server_Notices_IMessageHandlerContext_Task.htm)|
Задания, с которым производятся действия (обычно это завершаемое задание), или
null, если задание недоступно.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Notices - пространство
имён](N_Tessa_Extensions_Default_Server_Notices.htm)
