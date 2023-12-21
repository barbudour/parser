# ApplicationModel.ApplicationLaunched - событие
Событие успешного запуска приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler ApplicationLaunched
VB __Копировать
     Public Event ApplicationLaunched As EventHandler
C++ __Копировать
     public:
    virtual  event EventHandler^ ApplicationLaunched {
    	void add (EventHandler^ value);
    	void remove (EventHandler^ value);
    }
F# __Копировать
     abstract ApplicationLaunched : IEvent<EventHandler,
        EventArgs>
    override ApplicationLaunched : IEvent<EventHandler,
        EventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler)
#### Реализации
[IApplicationModel.ApplicationLaunched](E_Tessa_Applications_IApplicationModel_ApplicationLaunched.htm)  
##  __См. также
#### Ссылки
[ApplicationModel - ](T_Tessa_Applications_ApplicationModel.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
