# ApplicationModel.OnMessage - метод
Вызывает обработку сообщения message
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void OnMessage(
    	ApplicationMessage message
    )
VB __Копировать
     Public Sub OnMessage ( 
    	message As ApplicationMessage
    )
C++ __Копировать
     public:
    virtual void OnMessage(
    	ApplicationMessage^ message
    ) sealed
F# __Копировать
     abstract OnMessage : 
            message : ApplicationMessage -> unit 
    override OnMessage : 
            message : ApplicationMessage -> unit 
#### Параметры
message
[ApplicationMessage](T_Tessa_Applications_Messages_ApplicationMessage.htm)
     Обрабатываемое сообщение 
#### Реализации
[IApplicationMessageObserver.OnMessage(ApplicationMessage)](M_Tessa_Applications_Services_ApplicationManager_IApplicationMessageObserver_OnMessage.htm)  
##  __Исключения
[NullReferenceException](https://learn.microsoft.com/dotnet/api/system.nullreferenceexception)|
The address is a null pointer.  
---|---  
## __См. также
#### Ссылки
[ApplicationModel - ](T_Tessa_Applications_ApplicationModel.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
