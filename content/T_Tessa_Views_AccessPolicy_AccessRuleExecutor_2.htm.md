# AccessRuleExecutor<TAccessSubject, TContext> \- делегат
Осуществляет выполнение правил проверки доступности объекта
## __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate ValueTask<bool> AccessRuleExecutor<TAccessSubject, TContext>(
    	[CanBeNullAttribute] TAccessSubject accessSubject,
    	[CanBeNullAttribute] TContext context,
    	[NotNullAttribute] IEnumerable<IAccessRule<TAccessSubject, TContext>> rules,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Delegate Function AccessRuleExecutor(Of TAccessSubject, TContext) ( 
    	<CanBeNullAttribute> accessSubject As TAccessSubject,
    	<CanBeNullAttribute> context As TContext,
    	<NotNullAttribute> rules As IEnumerable(Of IAccessRule(Of TAccessSubject, TContext)),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     generic<typename TAccessSubject, typename TContext>
    public delegate ValueTask<bool> AccessRuleExecutor(
    	[CanBeNullAttribute] TAccessSubject accessSubject, 
    	[CanBeNullAttribute] TContext context, 
    	[NotNullAttribute] IEnumerable<IAccessRule<TAccessSubject, TContext>^>^ rules, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     type AccessRuleExecutor = 
        delegate of 
            [<CanBeNullAttribute>] accessSubject : 'TAccessSubject * 
            [<CanBeNullAttribute>] context : 'TContext * 
            [<NotNullAttribute>] rules : IEnumerable<IAccessRule<'TAccessSubject, 'TContext>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool>
#### Параметры
accessSubject TAccessSubject
     Объект наличие доступа к которому проверяется набором правил 
context TContext
     Контекст выполнения 
rules
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IAccessRule](T_Tessa_Views_AccessPolicy_IAccessRule_2.htm)<TAccessSubject,
TContext>>
     Правила проверки доступности 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Параметры типа
TAccessSubject
     Тип элемента к которому требуется проверка доступа 
TContext
     Тип контекста 
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
Признак доступности элемента
## __См. также
#### Ссылки
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
