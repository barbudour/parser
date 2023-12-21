# PluginFacade.StartChildInfo.SetAwaitCancellationDeltaSeconds - метод
Задаёт количество секунд до завершения интервала
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
     public PluginFacade.StartChildInfo SetAwaitCancellationDeltaSeconds(
    	double awaitCancellationDeltaSeconds
    )
VB __Копировать
     Public Function SetAwaitCancellationDeltaSeconds ( 
    	awaitCancellationDeltaSeconds As Double
    ) As PluginFacade.StartChildInfo
C++ __Копировать
     public:
    PluginFacade.StartChildInfo^ SetAwaitCancellationDeltaSeconds(
    	double awaitCancellationDeltaSeconds
    )
F# __Копировать
     member SetAwaitCancellationDeltaSeconds : 
            awaitCancellationDeltaSeconds : float -> PluginFacade.StartChildInfo 
#### Параметры
awaitCancellationDeltaSeconds
[Double](https://learn.microsoft.com/dotnet/api/system.double)
     Количество секунд до завершения интервала [AwaitGracefulStopSeconds](P_Chronos_Platform_Scheduling_PluginFacade_StartChildInfo_AwaitGracefulStopSeconds.htm), когда дочерний процесс пытается принудительно завершить [EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm) через [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken). 
#### Возвращаемое значение
[PluginFacade.StartChildInfo](T_Chronos_Platform_Scheduling_PluginFacade_StartChildInfo.htm)  
Текущий объект.
##  __См. также
#### Ссылки
[PluginFacade.StartChildInfo -
](T_Chronos_Platform_Scheduling_PluginFacade_StartChildInfo.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
