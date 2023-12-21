# PluginSyncLauncher.LaunchAsync - метод
Асинхронно запускает метод
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm),
если не установлен флаг
[DisallowConcurrency](P_Chronos_Platform_Scheduling_PluginRemoteCreationInfo_DisallowConcurrency.htm)
или не выполняется другого процесса с этим же плагином, запущенным таким же
методом.
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
    Информация для создания плагина.
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
[PluginSyncLauncher - ](T_Chronos_Platform_Scheduling_PluginSyncLauncher.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
