# PluginFacade.StartChildInfo.AwaitCancellationDeltaSeconds - свойство
Количество секунд до завершения интервала
[AwaitGracefulStopSeconds](P_Chronos_Platform_Scheduling_PluginFacade_StartChildInfo_AwaitGracefulStopSeconds.htm),
когда дочерний процесс пытается принудительно завершить
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm)
через
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public double AwaitCancellationDeltaSeconds { get; }
VB __Копировать
     Public ReadOnly Property AwaitCancellationDeltaSeconds As Double
    	Get
C++ __Копировать
     public:
    property double AwaitCancellationDeltaSeconds {
    	double get ();
    }
F# __Копировать
     member AwaitCancellationDeltaSeconds : float with get
#### Значение свойства
[Double](https://learn.microsoft.com/dotnet/api/system.double)
##  __См. также
#### Ссылки
[PluginFacade.StartChildInfo -
](T_Chronos_Platform_Scheduling_PluginFacade_StartChildInfo.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
