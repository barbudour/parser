# ServerSessionController.TryOpenSessionAsync - метод
Осуществляет запрос установки сессии
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IAsyncDisposable> TryOpenSessionAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryOpenSessionAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IAsyncDisposable)
C++ __Копировать
     public:
    virtual ValueTask<IAsyncDisposable^> TryOpenSessionAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryOpenSessionAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IAsyncDisposable> 
    override TryOpenSessionAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IAsyncDisposable> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)>  
Возвращает объект при вызове
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose), которого будет произведено отключение сессии, если
отсутствуют другие требующие сессию объекты. Либо возвращает null если при
поднятии сессии возникла ошибка
#### Реализации
[ISessionController.TryOpenSessionAsync(CancellationToken)](M_Tessa_Applications_ISessionController_TryOpenSessionAsync.htm)  
##  __См. также
#### Ссылки
[ServerSessionController - ](T_Tessa_Applications_ServerSessionController.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
