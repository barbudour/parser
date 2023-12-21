# ClientViewServiceImplementer.GetAllViewsAsync - метод
Возвращает список представлений [ITessaView](T_Tessa_Views_ITessaView.htm).
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IReadOnlyList<ITessaView>> GetAllViewsAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetAllViewsAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IReadOnlyList(Of ITessaView))
C++ __Копировать
     public:
    virtual ValueTask<IReadOnlyList<ITessaView^>^> GetAllViewsAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetAllViewsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IReadOnlyList<ITessaView>> 
    override GetAllViewsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IReadOnlyList<ITessaView>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[ITessaView](T_Tessa_Views_ITessaView.htm)>>  
Асинхронная задача.
#### Реализации
[IViewServiceImplementer.GetAllViewsAsync(CancellationToken)](M_Tessa_Views_IViewServiceImplementer_GetAllViewsAsync.htm)  
##  __См. также
#### Ссылки
[ClientViewServiceImplementer -
](T_Tessa_Applications_ClientViewServiceImplementer.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
