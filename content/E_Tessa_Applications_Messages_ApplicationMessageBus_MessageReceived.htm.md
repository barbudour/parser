# ApplicationMessageBus.MessageReceived - событие
Событие, возникающее при получении сообщения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Messages](N_Tessa_Applications_Messages.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<MessageReceivedEventArgs> MessageReceived
VB __Копировать
     Public Event MessageReceived As EventHandler(Of MessageReceivedEventArgs)
C++ __Копировать
     public:
    virtual  event EventHandler<MessageReceivedEventArgs^>^ MessageReceived {
    	void add (EventHandler<MessageReceivedEventArgs^>^ value);
    	void remove (EventHandler<MessageReceivedEventArgs^>^ value);
    }
F# __Копировать
     abstract MessageReceived : IEvent<EventHandler<MessageReceivedEventArgs>,
        MessageReceivedEventArgs>
    override MessageReceived : IEvent<EventHandler<MessageReceivedEventArgs>,
        MessageReceivedEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[MessageReceivedEventArgs](T_Tessa_Applications_Services_PlatformApplication_MessageReceivedEventArgs.htm)>
#### Реализации
[IApplicationMessageBus.MessageReceived](E_Tessa_Applications_Messages_IApplicationMessageBus_MessageReceived.htm)  
##  __См. также
#### Ссылки
[ApplicationMessageBus -
](T_Tessa_Applications_Messages_ApplicationMessageBus.htm)
[Tessa.Applications.Messages - пространство
имён](N_Tessa_Applications_Messages.htm)
