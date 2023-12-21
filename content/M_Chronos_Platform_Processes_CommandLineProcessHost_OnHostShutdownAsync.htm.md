# CommandLineProcessHost.OnHostShutdownAsync - метод
Хост остановлен. Вызывается после того, как все ресурсы хоста были
освобождены, а все процессы плагинов остановлены. Предоставляет последний шанс
выполнить некоторую очистку. Метод может выполнять асинхронные вызовы и должен
вернуть задачу, по завершению которой выполнение будет продолжено.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task OnHostShutdownAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function OnHostShutdownAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     protected:
    virtual Task^ OnHostShutdownAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract OnHostShutdownAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override OnHostShutdownAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __Заметки
Выполнение метода может быть в любой момент прервано операционной системой.
## __См. также
#### Ссылки
[CommandLineProcessHost -
](T_Chronos_Platform_Processes_CommandLineProcessHost.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
