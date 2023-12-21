# DefaultExecuteStrategy.ApplyAsync - метод
Применяет стратегию для заданного контекста, при этом при необходимости
изменяется контекст.
##  __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask ApplyAsync(
    	IExtensionStrategyContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ApplyAsync ( 
    	context As IExtensionStrategyContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask ApplyAsync(
    	IExtensionStrategyContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ApplyAsync : 
            context : IExtensionStrategyContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override ApplyAsync : 
            context : IExtensionStrategyContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
context
[IExtensionStrategyContext](T_Tessa_Extensions_IExtensionStrategyContext.htm)
    Контекст, для которого применяется стратегия.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
#### Реализации
[IExtensionStrategy.ApplyAsync(IExtensionStrategyContext,
CancellationToken)](M_Tessa_Extensions_IExtensionStrategy_ApplyAsync.htm)  
##  __См. также
#### Ссылки
[DefaultExecuteStrategy - ](T_Tessa_Extensions_DefaultExecuteStrategy.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
