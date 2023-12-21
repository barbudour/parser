# ApplicationModel.ApplicationLaunchFailed - событие
Событие сбоя при запуске приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler ApplicationLaunchFailed
VB __Копировать
     Public Event ApplicationLaunchFailed As EventHandler
C++ __Копировать
     public:
    virtual  event EventHandler^ ApplicationLaunchFailed {
    	void add (EventHandler^ value);
    	void remove (EventHandler^ value);
    }
F# __Копировать
     abstract ApplicationLaunchFailed : IEvent<EventHandler,
        EventArgs>
    override ApplicationLaunchFailed : IEvent<EventHandler,
        EventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler)
#### Реализации
[IApplicationModel.ApplicationLaunchFailed](E_Tessa_Applications_IApplicationModel_ApplicationLaunchFailed.htm)  
##  __См. также
#### Ссылки
[ApplicationModel - ](T_Tessa_Applications_ApplicationModel.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
