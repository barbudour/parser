# IApplicationMessageObserver.OnMessage - метод
Вызывает обработку сообщения message
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Services.ApplicationManager](N_Tessa_Applications_Services_ApplicationManager.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void OnMessage(
    	[NotNullAttribute] ApplicationMessage message
    )
VB __Копировать
     Sub OnMessage ( 
    	<NotNullAttribute> message As ApplicationMessage
    )
C++ __Копировать
     void OnMessage(
    	[NotNullAttribute] ApplicationMessage^ message
    )
F# __Копировать
     abstract OnMessage : 
            [<NotNullAttribute>] message : ApplicationMessage -> unit 
#### Параметры
message
[ApplicationMessage](T_Tessa_Applications_Messages_ApplicationMessage.htm)
     Обрабатываемое сообщение 
## __См. также
#### Ссылки
[IApplicationMessageObserver -
](T_Tessa_Applications_Services_ApplicationManager_IApplicationMessageObserver.htm)
[Tessa.Applications.Services.ApplicationManager - пространство
имён](N_Tessa_Applications_Services_ApplicationManager.htm)
