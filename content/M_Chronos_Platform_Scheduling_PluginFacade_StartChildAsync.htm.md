# PluginFacade.StartChildAsync - метод
Асинхронно запускает жизненный цикл дочернего процесса, запускающего плагин.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Task StartChildAsync(
    	string[] args,
    	PluginFacade.StartChildInfo startChildInfo,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StartChildAsync ( 
    	args As String(),
    	startChildInfo As PluginFacade.StartChildInfo,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    Task^ StartChildAsync(
    	array<String^>^ args, 
    	PluginFacade.StartChildInfo^ startChildInfo, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member StartChildAsync : 
            args : string[] * 
            startChildInfo : PluginFacade.StartChildInfo * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
args [String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Аргументы командной строки, переданные дочернему процессу.
startChildInfo
[PluginFacade.StartChildInfo](T_Chronos_Platform_Scheduling_PluginFacade_StartChildInfo.htm)
    Параметры запуска плагина.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхроная задача.
##  __Заметки
Не выполняет обработку ошибок.
## __См. также
#### Ссылки
[PluginFacade - ](T_Chronos_Platform_Scheduling_PluginFacade.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
