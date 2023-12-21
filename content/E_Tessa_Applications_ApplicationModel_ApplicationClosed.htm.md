# ApplicationModel.ApplicationClosed - событие
Событие закрытия приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler ApplicationClosed
VB __Копировать
     Public Event ApplicationClosed As EventHandler
C++ __Копировать
     public:
    virtual  event EventHandler^ ApplicationClosed {
    	void add (EventHandler^ value);
    	void remove (EventHandler^ value);
    }
F# __Копировать
     abstract ApplicationClosed : IEvent<EventHandler,
        EventArgs>
    override ApplicationClosed : IEvent<EventHandler,
        EventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler)
#### Реализации
[IApplicationModel.ApplicationClosed](E_Tessa_Applications_IApplicationModel_ApplicationClosed.htm)  
##  __См. также
#### Ссылки
[ApplicationModel - ](T_Tessa_Applications_ApplicationModel.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
