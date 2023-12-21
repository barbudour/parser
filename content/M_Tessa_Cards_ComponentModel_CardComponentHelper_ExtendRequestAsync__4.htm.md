# CardComponentHelper.ExtendRequestAsync<TRequest, TResponse, TContext,
TExtension> \- метод
Дополняет запрос к API карточек цепочками расширений.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<TResponse> ExtendRequestAsync<TRequest, TResponse, TContext, TExtension>(
    	Object validationObject,
    	IExtensionContainer extensionContainer,
    	TContext context,
    	Func<IExtensionExecutor<TExtension>, CancellationToken, Task<TResponse>> performRequestFuncAsync,
    	Expression<ExtensionMethodReferenceAsync<TExtension, TContext>> beforeRequestExpression,
    	Expression<ExtensionMethodReferenceAsync<TExtension, TContext>> afterRequestExpression,
    	Expression<ExtensionMethodReferenceAsync<TExtension, TContext>> afterRequestFinallyExpression = null,
    	Func<TContext, TResponse, CancellationToken, ValueTask> coerceContextActionAsync = null,
    	CancellationToken cancellationToken = default
    )
    where TRequest : CardInfoStorageObject
    where TResponse : new(), CardResponseBase
    where TContext : CardExtensionContext, ICardRequestExtensionContext<TRequest, TResponse>
    where TExtension : class, ICardExtension
VB __Копировать
     Public Shared Function ExtendRequestAsync(Of TRequest As CardInfoStorageObject, TResponse As {New, CardResponseBase}, TContext As {CardExtensionContext, ICardRequestExtensionContext(Of TRequest, TResponse)}, TExtension As {Class, ICardExtension}) ( 
    	validationObject As Object,
    	extensionContainer As IExtensionContainer,
    	context As TContext,
    	performRequestFuncAsync As Func(Of IExtensionExecutor(Of TExtension), CancellationToken, Task(Of TResponse)),
    	beforeRequestExpression As Expression(Of ExtensionMethodReferenceAsync(Of TExtension, TContext)),
    	afterRequestExpression As Expression(Of ExtensionMethodReferenceAsync(Of TExtension, TContext)),
    	Optional afterRequestFinallyExpression As Expression(Of ExtensionMethodReferenceAsync(Of TExtension, TContext)) = Nothing,
    	Optional coerceContextActionAsync As Func(Of TContext, TResponse, CancellationToken, ValueTask) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of TResponse)
C++ __Копировать
     public:
    generic<typename TRequest, typename TResponse, typename TContext, typename TExtension>
    where TRequest : CardInfoStorageObject
    where TResponse : gcnew(), CardResponseBase
    where TContext : CardExtensionContext, ICardRequestExtensionContext<TRequest, TResponse>
    where TExtension : ref class, ICardExtension
    static Task<TResponse>^ ExtendRequestAsync(
    	Object^ validationObject, 
    	IExtensionContainer^ extensionContainer, 
    	TContext context, 
    	Func<IExtensionExecutor<TExtension>^, CancellationToken, Task<TResponse>^>^ performRequestFuncAsync, 
    	Expression<ExtensionMethodReferenceAsync<TExtension, TContext>^>^ beforeRequestExpression, 
    	Expression<ExtensionMethodReferenceAsync<TExtension, TContext>^>^ afterRequestExpression, 
    	Expression<ExtensionMethodReferenceAsync<TExtension, TContext>^>^ afterRequestFinallyExpression = nullptr, 
    	Func<TContext, TResponse, CancellationToken, ValueTask>^ coerceContextActionAsync = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member ExtendRequestAsync : 
            validationObject : Object * 
            extensionContainer : IExtensionContainer * 
            context : 'TContext * 
            performRequestFuncAsync : Func<IExtensionExecutor<'TExtension>, CancellationToken, Task<'TResponse>> * 
            beforeRequestExpression : Expression<ExtensionMethodReferenceAsync<'TExtension, 'TContext>> * 
            afterRequestExpression : Expression<ExtensionMethodReferenceAsync<'TExtension, 'TContext>> * 
            ?afterRequestFinallyExpression : Expression<ExtensionMethodReferenceAsync<'TExtension, 'TContext>> * 
            ?coerceContextActionAsync : Func<'TContext, 'TResponse, CancellationToken, ValueTask> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _afterRequestFinallyExpression = defaultArg afterRequestFinallyExpression null
            let _coerceContextActionAsync = defaultArg coerceContextActionAsync null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<'TResponse>  when 'TRequest : CardInfoStorageObject when 'TResponse : new() and CardResponseBase when 'TContext : CardExtensionContext and ICardRequestExtensionContext<'TRequest, 'TResponse> when 'TExtension : not struct and ICardExtension
#### Параметры
validationObject
[Object](https://learn.microsoft.com/dotnet/api/system.object)
    Объект, от имени которого выполняется валидация.
extensionContainer
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
    Контейнер, содержащий зарегистрированные расширения.
context TContext
    Контекст, передаваемый между расширениями в цепочке.
performRequestFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[IExtensionExecutor](T_Tessa_Extensions_IExtensionExecutor_1.htm)<TExtension>,
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<TResponse>>
     Функция, которая принимает объект, выполняющий расширения, осуществляет запрос к API карточек и возвращает ответ. 
beforeRequestExpression
[Expression](https://learn.microsoft.com/dotnet/api/system.linq.expressions.expression-1)<[ExtensionMethodReferenceAsync](T_Tessa_Extensions_ExtensionMethodReferenceAsync_2.htm)<TExtension,
TContext>>
     Выражение, ссылающееся на цепочку расширений, выполняемых перед запросом к API карточек. 
afterRequestExpression
[Expression](https://learn.microsoft.com/dotnet/api/system.linq.expressions.expression-1)<[ExtensionMethodReferenceAsync](T_Tessa_Extensions_ExtensionMethodReferenceAsync_2.htm)<TExtension,
TContext>>
     Выражение, ссылающееся на цепочку расширений, выполняемых после запроса к API карточек. 
afterRequestFinallyExpression
[Expression](https://learn.microsoft.com/dotnet/api/system.linq.expressions.expression-1)<[ExtensionMethodReferenceAsync](T_Tessa_Extensions_ExtensionMethodReferenceAsync_2.htm)<TExtension,
TContext>> (Optional)
     Выражение, ссылающееся на цепочку расширений, выполняемых при возникновении исключения на любом моменте выполнения (включая цепочку beforeRequestExpression) или после расширений afterRequestExpression в случае отсутствия исключений. Любые исключения, возникающие в этих расширениях, не приводят к прекращению выполнения цепочки (последующие расширения выполняются). При этом все исключения, кроме [OperationCanceledException](https://learn.microsoft.com/dotnet/api/system.operationcanceledexception), логируются в результате валидации. 
coerceContextActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-4)<TContext,
TResponse,
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
(Optional)
     Метод, выполняющий корректировку контекста перед вызовом цепочки расширений afterRequestExpression, или null, если корректировка не требуется. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Параметры типа
TRequest
     Тип запроса к API карточек. Должен быть унаследован от класса [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm). 
TResponse
     Тип ответа на запрос к API карточек. Должен быть унаследован от класса [CardResponseBase](T_Tessa_Cards_CardResponseBase.htm) и иметь открытый конструктор по умолчанию. 
TContext
     Тип контекста, используемого в расширениях. Должен быть унаследован от класса [CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm), и должен реализовывать интерфейс [ICardRequestExtensionContext<TRequest, TResponse>](T_Tessa_Cards_Extensions_ICardRequestExtensionContext_2.htm). 
TExtension
     Ссылочный тип расширений. Должен реализовывать интерфейс [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm). 
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<TResponse>  
Ответ на запрос к API карточек, который мог быть изменён цепочками расширений.
##  __См. также
#### Ссылки
[CardComponentHelper - ](T_Tessa_Cards_ComponentModel_CardComponentHelper.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
