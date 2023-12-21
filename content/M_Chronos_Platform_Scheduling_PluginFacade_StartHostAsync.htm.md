# PluginFacade.StartHostAsync - метод
Асинхронно запускает жизненный цикл процесса хоста, обрабатываюшего плагины.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Task StartHostAsync(
    	PluginFacade.StartHostInfo info,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StartHostAsync ( 
    	info As PluginFacade.StartHostInfo,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    Task^ StartHostAsync(
    	PluginFacade.StartHostInfo^ info, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member StartHostAsync : 
            info : PluginFacade.StartHostInfo * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
info
[PluginFacade.StartHostInfo](T_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo.htm)
    Объект, содержащий информацию о параметрах запуска этого метода.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __Заметки
Метод не выполняет обработку ошибок.
## __См. также
#### Ссылки
[PluginFacade - ](T_Chronos_Platform_Scheduling_PluginFacade.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
