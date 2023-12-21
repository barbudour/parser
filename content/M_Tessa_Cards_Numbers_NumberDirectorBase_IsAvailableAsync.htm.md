# NumberDirectorBase.IsAvailableAsync - метод
Выполняет проверку доступности для типа события, происходящего с номером.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<bool> IsAvailableAsync(
    	INumberContext context,
    	NumberEventType eventType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function IsAvailableAsync ( 
    	context As INumberContext,
    	eventType As NumberEventType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    virtual ValueTask<bool> IsAvailableAsync(
    	INumberContext^ context, 
    	NumberEventType^ eventType, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract IsAvailableAsync : 
            context : INumberContext * 
            eventType : NumberEventType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
    override IsAvailableAsync : 
            context : INumberContext * 
            eventType : NumberEventType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
eventType [NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
    Тип события, происходящего с номером.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если действие доступно для выполнения; false в противном случае.
#### Реализации
[INumberDirectorBase.IsAvailableAsync(INumberContext, NumberEventType,
CancellationToken)](M_Tessa_Cards_Numbers_INumberDirectorBase_IsAvailableAsync.htm)  
##  __См. также
#### Ссылки
[NumberDirectorBase - ](T_Tessa_Cards_Numbers_NumberDirectorBase.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
