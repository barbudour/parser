# ViewWalker<TContext>.ApplyAsync(IEnumerable<ITessaView>, TContext,
AccessRuleExecutor<ITessaView, TContext>, CancellationToken) - метод
Осуществляет фильтрацию списка представлений views согласно политике
доступности
[IViewAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_IViewAccessPolicy_1.htm)
в контексте context с помощью исполнителя правил ruleExecutor
##  __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IEnumerable<ITessaView>> ApplyAsync(
    	IEnumerable<ITessaView> views,
    	TContext context,
    	AccessRuleExecutor<ITessaView, TContext> ruleExecutor,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ApplyAsync ( 
    	views As IEnumerable(Of ITessaView),
    	context As TContext,
    	ruleExecutor As AccessRuleExecutor(Of ITessaView, TContext),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IEnumerable(Of ITessaView))
C++ __Копировать
     public:
    virtual ValueTask<IEnumerable<ITessaView^>^> ApplyAsync(
    	IEnumerable<ITessaView^>^ views, 
    	TContext context, 
    	AccessRuleExecutor<ITessaView^, TContext>^ ruleExecutor, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ApplyAsync : 
            views : IEnumerable<ITessaView> * 
            context : 'TContext * 
            ruleExecutor : AccessRuleExecutor<ITessaView, 'TContext> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IEnumerable<ITessaView>> 
    override ApplyAsync : 
            views : IEnumerable<ITessaView> * 
            context : 'TContext * 
            ruleExecutor : AccessRuleExecutor<ITessaView, 'TContext> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IEnumerable<ITessaView>> 
#### Параметры
views
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ITessaView](T_Tessa_Views_ITessaView.htm)>
     Фильтруемый список представлений 
context [TContext](T_Tessa_Views_AccessPolicy_ViewWalker_1.htm)
     Контекст выполнения 
ruleExecutor
[AccessRuleExecutor](T_Tessa_Views_AccessPolicy_AccessRuleExecutor_2.htm)<[ITessaView](T_Tessa_Views_ITessaView.htm),
[TContext](T_Tessa_Views_AccessPolicy_ViewWalker_1.htm)>
     Исполнитель правил доступности 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ITessaView](T_Tessa_Views_ITessaView.htm)>>  
Список содержащий представления соответствующие политике доступности
#### Реализации
[IViewWalker<TContext>.ApplyAsync(IEnumerable<ITessaView>, TContext,
AccessRuleExecutor<ITessaView, TContext>,
CancellationToken)](M_Tessa_Views_AccessPolicy_IViewWalker_1_ApplyAsync_1.htm)  
##  __См. также
#### Ссылки
[ViewWalker<TContext> \- ](T_Tessa_Views_AccessPolicy_ViewWalker_1.htm)
[ApplyAsync -
перегрузка](Overload_Tessa_Views_AccessPolicy_ViewWalker_1_ApplyAsync.htm)
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
