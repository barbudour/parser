# PluginFacade.StartHostInfo.SetHostActivity - метод
Задаёт метод, который должен осуществлять некоторые действия, по окончании
которых хост завершает свою работу.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public PluginFacade.StartHostInfo SetHostActivity(
    	Func<CancellationToken, Task> hostActivityActionAsync
    )
VB __Копировать
     Public Function SetHostActivity ( 
    	hostActivityActionAsync As Func(Of CancellationToken, Task)
    ) As PluginFacade.StartHostInfo
C++ __Копировать
     public:
    PluginFacade.StartHostInfo^ SetHostActivity(
    	Func<CancellationToken, Task^>^ hostActivityActionAsync
    )
F# __Копировать
     member SetHostActivity : 
            hostActivityActionAsync : Func<CancellationToken, Task> -> PluginFacade.StartHostInfo 
#### Параметры
hostActivityActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
     Метод, который должен осуществлять некоторые действия, по окончании которых хост завершает свою работу. Если параметр равен null, то в качестве такого метода используется вызов await Task.Delay(Timeout.Infinite, cancellationToken). Исключение [OperationCanceledException](https://learn.microsoft.com/dotnet/api/system.operationcanceledexception), выбрасываемое этим методом, игнорируется, поэтому его можно не перехватывать внутри метода при ожидании токена. 
#### Возвращаемое значение
[PluginFacade.StartHostInfo](T_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo.htm)  
Текущий объект.
##  __См. также
#### Ссылки
[PluginFacade.StartHostInfo -
](T_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
