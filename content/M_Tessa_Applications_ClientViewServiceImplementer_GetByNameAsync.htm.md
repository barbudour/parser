# ClientViewServiceImplementer.GetByNameAsync - метод
Возвращает представление заданное по имени viewName
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<ITessaView> GetByNameAsync(
    	string viewName,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetByNameAsync ( 
    	viewName As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ITessaView)
C++ __Копировать
     public:
    virtual ValueTask<ITessaView^> GetByNameAsync(
    	String^ viewName, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetByNameAsync : 
            viewName : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ITessaView> 
    override GetByNameAsync : 
            viewName : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ITessaView> 
#### Параметры
viewName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя представления 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ITessaView](T_Tessa_Views_ITessaView.htm)>  
Найденное представление или null
#### Реализации
[IViewServiceImplementer.GetByNameAsync(String,
CancellationToken)](M_Tessa_Views_IViewServiceImplementer_GetByNameAsync.htm)  
##  __См. также
#### Ссылки
[ClientViewServiceImplementer -
](T_Tessa_Applications_ClientViewServiceImplementer.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
