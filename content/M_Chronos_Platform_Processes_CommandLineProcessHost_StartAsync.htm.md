# CommandLineProcessHost.StartAsync - метод
Запускает асинхронную обработку заданных аргументов командной строки, выбирая
режим хоста или дочернего процесса.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Task StartAsync(
    	string[] args,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StartAsync ( 
    	args As String(),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    Task^ StartAsync(
    	array<String^>^ args, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member StartAsync : 
            args : string[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
args [String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Массив аргументов командной строки, полученных процессом.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CommandLineProcessHost -
](T_Chronos_Platform_Processes_CommandLineProcessHost.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
