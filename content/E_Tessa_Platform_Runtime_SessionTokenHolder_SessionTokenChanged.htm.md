# SessionTokenHolder.SessionTokenChanged - событие
Событие, происходящее при изменении токена для текущей сессии.
##  __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<DeferredEventArgs> SessionTokenChanged
VB __Копировать
     Public Event SessionTokenChanged As EventHandler(Of DeferredEventArgs)
C++ __Копировать
     public:
    virtual  event EventHandler<DeferredEventArgs^>^ SessionTokenChanged {
    	void add (EventHandler<DeferredEventArgs^>^ value);
    	void remove (EventHandler<DeferredEventArgs^>^ value);
    }
F# __Копировать
     abstract SessionTokenChanged : IEvent<EventHandler<DeferredEventArgs>,
        DeferredEventArgs>
    override SessionTokenChanged : IEvent<EventHandler<DeferredEventArgs>,
        DeferredEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[DeferredEventArgs](T_Tessa_Platform_DeferredEventArgs.htm)>
#### Реализации
[ISessionTokenHolder.SessionTokenChanged](E_Tessa_Platform_Runtime_ISessionTokenHolder_SessionTokenChanged.htm)  
##  __См. также
#### Ссылки
[SessionTokenHolder - ](T_Tessa_Platform_Runtime_SessionTokenHolder.htm)
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
