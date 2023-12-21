# PluginFacade.PluginImported - событие
Событие, происходящее после импортирования плагина.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<PluginImportEventArgs> PluginImported
VB __Копировать
     Public Event PluginImported As EventHandler(Of PluginImportEventArgs)
C++ __Копировать
     public:
     event EventHandler<PluginImportEventArgs^>^ PluginImported {
    	void add (EventHandler<PluginImportEventArgs^>^ value);
    	void remove (EventHandler<PluginImportEventArgs^>^ value);
    }
F# __Копировать
     member PluginImported : IEvent<EventHandler<PluginImportEventArgs>,
        PluginImportEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[PluginImportEventArgs](T_Chronos_Platform_Scheduling_PluginImportEventArgs.htm)>
##  __См. также
#### Ссылки
[PluginFacade - ](T_Chronos_Platform_Scheduling_PluginFacade.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
