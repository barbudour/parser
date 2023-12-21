# PluginSchedulingHelper.SchedulePluginAsync - метод
Асинхронно предоставляет указанному планировщику информацию, необходимую для
запуска указанного плагина.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task SchedulePluginAsync(
    	PluginImportingItem pluginImport,
    	IScheduler scheduler,
    	PluginLauncherKey launcherKey,
    	PluginShutdownMode hostShutdownMode
    )
VB __Копировать
     Public Shared Function SchedulePluginAsync ( 
    	pluginImport As PluginImportingItem,
    	scheduler As IScheduler,
    	launcherKey As PluginLauncherKey,
    	hostShutdownMode As PluginShutdownMode
    ) As Task
C++ __Копировать
     public:
    static Task^ SchedulePluginAsync(
    	PluginImportingItem^ pluginImport, 
    	IScheduler^ scheduler, 
    	PluginLauncherKey^ launcherKey, 
    	PluginShutdownMode hostShutdownMode
    )
F# __Копировать
     static member SchedulePluginAsync : 
            pluginImport : PluginImportingItem * 
            scheduler : IScheduler * 
            launcherKey : PluginLauncherKey * 
            hostShutdownMode : PluginShutdownMode -> Task 
#### Параметры
pluginImport
[PluginImportingItem](T_Chronos_Platform_Scheduling_PluginImportingItem.htm)
    Информация о плагине.
scheduler IScheduler
    Планировщик, который будет запускать плагин.
launcherKey
[PluginLauncherKey](T_Chronos_Platform_Scheduling_PluginLauncherKey.htm)
     Ключ объекта [IPluginLauncher](T_Chronos_Platform_Scheduling_IPluginLauncher.htm), зарегистрированного в контейнере [PluginLauncherResolver](T_Chronos_Platform_Scheduling_PluginLauncherResolver.htm). 
hostShutdownMode
[PluginShutdownMode](T_Chronos_Platform_Scheduling_PluginShutdownMode.htm)
     Способ завершения процесса хоста, определяющий способ завершения плагинов. 
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[PluginSchedulingHelper - ](T_Chronos_Platform_PluginSchedulingHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
