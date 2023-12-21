# PluginLaunchingEventArgs - конструктор
Создаёт аргументы события с указаанием ссылки на экземпляр плагина.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public PluginLaunchingEventArgs(
    	IPlugin plugin,
    	CancellationTokenSource cancellationTokenSource
    )
VB __Копировать
     Public Sub New ( 
    	plugin As IPlugin,
    	cancellationTokenSource As CancellationTokenSource
    )
C++ __Копировать
     public:
    PluginLaunchingEventArgs(
    	IPlugin^ plugin, 
    	CancellationTokenSource^ cancellationTokenSource
    )
F# __Копировать
     new : 
            plugin : IPlugin * 
            cancellationTokenSource : CancellationTokenSource -> PluginLaunchingEventArgs
#### Параметры
plugin [IPlugin](T_Chronos_Contracts_IPlugin.htm)
    Ссылка на экземпляр плагина.
cancellationTokenSource
[CancellationTokenSource](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtokensource)
     Объект, посредством которого можно отменить выполнение метода [EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm). 
## __См. также
#### Ссылки
[PluginLaunchingEventArgs -
](T_Chronos_Platform_Scheduling_PluginLaunchingEventArgs.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
