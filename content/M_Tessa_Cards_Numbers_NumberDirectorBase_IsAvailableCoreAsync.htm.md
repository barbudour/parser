# NumberDirectorBase.IsAvailableCoreAsync - метод
Выполняет проверку доступности для типа события, происходящего с номером.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask<bool> IsAvailableCoreAsync(
    	INumberContext context,
    	NumberEventType eventType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function IsAvailableCoreAsync ( 
    	context As INumberContext,
    	eventType As NumberEventType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     protected:
    virtual ValueTask<bool> IsAvailableCoreAsync(
    	INumberContext^ context, 
    	NumberEventType^ eventType, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract IsAvailableCoreAsync : 
            context : INumberContext * 
            eventType : NumberEventType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
    override IsAvailableCoreAsync : 
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
## __См. также
#### Ссылки
[NumberDirectorBase - ](T_Tessa_Cards_Numbers_NumberDirectorBase.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
