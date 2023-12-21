# NotNullViewMetadataRule<TContext>.IsSatisfiedByAsync - метод
Выполняет проверку доступности объекта subject
##  __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<bool> IsSatisfiedByAsync(
    	ITessaView subject,
    	TContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function IsSatisfiedByAsync ( 
    	subject As ITessaView,
    	context As TContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    virtual ValueTask<bool> IsSatisfiedByAsync(
    	ITessaView^ subject, 
    	TContext context, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract IsSatisfiedByAsync : 
            subject : ITessaView * 
            context : 'TContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
    override IsSatisfiedByAsync : 
            subject : ITessaView * 
            context : 'TContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
subject [ITessaView](T_Tessa_Views_ITessaView.htm)
     Объект проверяемый на наличие доступности 
context [TContext](T_Tessa_Views_AccessPolicy_NotNullViewMetadataRule_1.htm)
     Контекст обработки 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
Результат проверки
#### Реализации
[IAccessRule<TAccessSubject,
TMandatoryContext>.IsSatisfiedByAsync(TAccessSubject, TMandatoryContext,
CancellationToken)](M_Tessa_Views_AccessPolicy_IAccessRule_2_IsSatisfiedByAsync.htm)  
##  __См. также
#### Ссылки
[NotNullViewMetadataRule<TContext> \-
](T_Tessa_Views_AccessPolicy_NotNullViewMetadataRule_1.htm)
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
