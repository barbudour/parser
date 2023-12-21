# ClientViewServiceImplementer.GetByNamesAsync - метод
Возвращает список представлений заданных именами в списке viewsNames
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IReadOnlyList<ITessaView>> GetByNamesAsync(
    	IEnumerable<string> viewsNames,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetByNamesAsync ( 
    	viewsNames As IEnumerable(Of String),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IReadOnlyList(Of ITessaView))
C++ __Копировать
     public:
    virtual ValueTask<IReadOnlyList<ITessaView^>^> GetByNamesAsync(
    	IEnumerable<String^>^ viewsNames, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetByNamesAsync : 
            viewsNames : IEnumerable<string> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IReadOnlyList<ITessaView>> 
    override GetByNamesAsync : 
            viewsNames : IEnumerable<string> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IReadOnlyList<ITessaView>> 
#### Параметры
viewsNames
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
     Список имен 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[ITessaView](T_Tessa_Views_ITessaView.htm)>>  
Список представлений
#### Реализации
[IViewServiceImplementer.GetByNamesAsync(IEnumerable<String>,
CancellationToken)](M_Tessa_Views_IViewServiceImplementer_GetByNamesAsync.htm)  
##  __См. также
#### Ссылки
[ClientViewServiceImplementer -
](T_Tessa_Applications_ClientViewServiceImplementer.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
