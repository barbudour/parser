# PluginSyncLauncher.PluginLaunching - событие
Событие, возникающее перед запуском плагина.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<PluginLaunchingEventArgs> PluginLaunching
VB __Копировать
     Public Event PluginLaunching As EventHandler(Of PluginLaunchingEventArgs)
C++ __Копировать
     public:
     event EventHandler<PluginLaunchingEventArgs^>^ PluginLaunching {
    	void add (EventHandler<PluginLaunchingEventArgs^>^ value);
    	void remove (EventHandler<PluginLaunchingEventArgs^>^ value);
    }
F# __Копировать
     member PluginLaunching : IEvent<EventHandler<PluginLaunchingEventArgs>,
        PluginLaunchingEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[PluginLaunchingEventArgs](T_Chronos_Platform_Scheduling_PluginLaunchingEventArgs.htm)>
##  __См. также
#### Ссылки
[PluginSyncLauncher - ](T_Chronos_Platform_Scheduling_PluginSyncLauncher.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
