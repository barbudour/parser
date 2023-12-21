# PluginFacade.StartHostInfo.HostActivityActionAsync - свойство
Метод, который должен осуществлять некоторые действия, по окончании которых
хост завершает свою работу. Если значение не задано или равно null, то в
качестве такого метода используется вызов await Task.Delay(Timeout.Infinite,
cancellationToken). Исключение
[OperationCanceledException](https://learn.microsoft.com/dotnet/api/system.operationcanceledexception),
выбрасываемое этим методом, игнорируется, поэтому его можно не перехватывать
внутри метода при ожидании токена.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Func<CancellationToken, Task> HostActivityActionAsync { get; }
VB __Копировать
     Public ReadOnly Property HostActivityActionAsync As Func(Of CancellationToken, Task)
    	Get
C++ __Копировать
     public:
    property Func<CancellationToken, Task^>^ HostActivityActionAsync {
    	Func<CancellationToken, Task^>^ get ();
    }
F# __Копировать
     member HostActivityActionAsync : Func<CancellationToken, Task> with get
#### Значение свойства
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
##  __См. также
#### Ссылки
[PluginFacade.StartHostInfo -
](T_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
