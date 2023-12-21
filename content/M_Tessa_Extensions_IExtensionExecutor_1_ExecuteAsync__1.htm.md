# IExtensionExecutor<TExtension>.ExecuteAsync<TContext> \- метод
Выполняет заданный метод асинхронно для всех зарегистрированных расширений
определённого типа.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task ExecuteAsync<TContext>(
    	Expression<ExtensionMethodReferenceAsync<TExtension, TContext>> method,
    	TContext context,
    	Func<IExtensionStrategyContext, ValueTask> handleExceptionAsync = null,
    	bool continueOnCapturedContext = false,
    	bool ignoreContextCancellation = false
    )
    where TContext : class, IExtensionContext
VB __Копировать
     Function ExecuteAsync(Of TContext As {Class, IExtensionContext}) ( 
    	method As Expression(Of ExtensionMethodReferenceAsync(Of TExtension, TContext)),
    	context As TContext,
    	Optional handleExceptionAsync As Func(Of IExtensionStrategyContext, ValueTask) = Nothing,
    	Optional continueOnCapturedContext As Boolean = false,
    	Optional ignoreContextCancellation As Boolean = false
    ) As Task
C++ __Копировать
    generic<typename TContext>
    where TContext : ref class, IExtensionContext
    Task^ ExecuteAsync(
    	Expression<ExtensionMethodReferenceAsync<TExtension, TContext>^>^ method, 
    	TContext context, 
    	Func<IExtensionStrategyContext^, ValueTask>^ handleExceptionAsync = nullptr, 
    	bool continueOnCapturedContext = false, 
    	bool ignoreContextCancellation = false
    )
F# __Копировать
     abstract ExecuteAsync : 
            method : Expression<ExtensionMethodReferenceAsync<'TExtension, 'TContext>> * 
            context : 'TContext * 
            ?handleExceptionAsync : Func<IExtensionStrategyContext, ValueTask> * 
            ?continueOnCapturedContext : bool * 
            ?ignoreContextCancellation : bool 
    (* Defaults:
            let _handleExceptionAsync = defaultArg handleExceptionAsync null
            let _continueOnCapturedContext = defaultArg continueOnCapturedContext false
            let _ignoreContextCancellation = defaultArg ignoreContextCancellation false
    *)
    -> Task  when 'TContext : not struct and IExtensionContext
#### Параметры
method
[Expression](https://learn.microsoft.com/dotnet/api/system.linq.expressions.expression-1)<[ExtensionMethodReferenceAsync](T_Tessa_Extensions_ExtensionMethodReferenceAsync_2.htm)<[TExtension](T_Tessa_Extensions_IExtensionExecutor_1.htm),
TContext>>
    Делегат, возвращающий метод расширения, который можно выполнить. Не должен быть равен null.
context TContext
     Параметр выполняемого метода, передаваемый между расширениями. Токен отмены асинхронной операции передаётся в этом объекте. Не должен быть равен null. 
handleExceptionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[IExtensionStrategyContext](T_Tessa_Extensions_IExtensionStrategyContext.htm),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
(Optional)
Метод, выполняющийся при обработке исключений для каждого экземпляра
расширений после того, как была выполнена трассировка расширения.
Метод может изменить
[IExtensionStrategyContext](T_Tessa_Extensions_IExtensionStrategyContext.htm),
в т.ч. установить режим обработки исключений в свойстве ExceptionHandlingMode.
Укажите null, если метод не требуется выполнять.
continueOnCapturedContext
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
Признак того, что выполнение асинхронных методов должно быть продолжено на том
же контексте SynchronizationContext, на котором оно было начато, если таковой
был.
Обычно это означает, что при запуске расширений из потока UI каждый метод
расширения будет выполнен на потоке UI.
ignoreContextCancellation
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
Признак того, что токен отмены context.CancellationToken не будет
использоваться во внутренней реализации метода. При этом токен может быть
задействован в выполняемых методах расширений.
Рекомендуется указывать для Finally-расширений, где исключения
[OperationCanceledException](https://learn.microsoft.com/dotnet/api/system.operationcanceledexception)
в обработчике handleExceptionAsync не должны прерывать выполнение последующих
расширений.
#### Параметры типа
TContext
    Тип параметра для выполняемого метода, реализующий интерфейс [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm).
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Полная копия объекта.
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Параметры method или context равны null.  
---|---  
## __См. также
#### Ссылки
[IExtensionExecutor<TExtension> \-
](T_Tessa_Extensions_IExtensionExecutor_1.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
