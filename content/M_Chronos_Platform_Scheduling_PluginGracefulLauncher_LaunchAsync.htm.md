# PluginGracefulLauncher.LaunchAsync - метод
Асинхронно запускает плагин на выполнение.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<PluginLaunchingData> LaunchAsync(
    	PluginRemoteCreationInfo pluginCreationInfo,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function LaunchAsync ( 
    	pluginCreationInfo As PluginRemoteCreationInfo,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of PluginLaunchingData)
C++ __Копировать
     public:
    virtual Task<PluginLaunchingData^>^ LaunchAsync(
    	PluginRemoteCreationInfo^ pluginCreationInfo, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract LaunchAsync : 
            pluginCreationInfo : PluginRemoteCreationInfo * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<PluginLaunchingData> 
    override LaunchAsync : 
            pluginCreationInfo : PluginRemoteCreationInfo * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<PluginLaunchingData> 
#### Параметры
pluginCreationInfo
[PluginRemoteCreationInfo](T_Chronos_Platform_Scheduling_PluginRemoteCreationInfo.htm)
    Информация для удалённого запуска плагина.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[PluginLaunchingData](T_Chronos_Platform_Scheduling_PluginLaunchingData.htm)>  
Асинхронная задача, которая возвращает данные о запущенном плагине.
#### Реализации
[IPluginLauncher.LaunchAsync(PluginRemoteCreationInfo,
CancellationToken)](M_Chronos_Platform_Scheduling_IPluginLauncher_LaunchAsync.htm)  
##  __См. также
#### Ссылки
[PluginGracefulLauncher -
](T_Chronos_Platform_Scheduling_PluginGracefulLauncher.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
