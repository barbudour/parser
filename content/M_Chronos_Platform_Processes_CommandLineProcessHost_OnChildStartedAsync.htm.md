# CommandLineProcessHost.OnChildStartedAsync - метод
Запущен плагин с указанными параметрами. Метод может выполнять асинхронные
вызовы и должен вернуть задачу, по завершению которой выполнение будет
продолжено.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract Task OnChildStartedAsync(
    	string[] args,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function OnChildStartedAsync ( 
    	args As String(),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     protected:
    virtual Task^ OnChildStartedAsync(
    	array<String^>^ args, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract OnChildStartedAsync : 
            args : string[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
args [String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Параметры запуска, передаваемые в качестве аргументов командной строки.
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
