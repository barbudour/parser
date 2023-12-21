# DocumentNumberDirector.IsAvailableCoreAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Numbers](N_Tessa_Extensions_Default_Shared_Numbers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<bool> IsAvailableCoreAsync(
    	INumberContext context,
    	NumberEventType eventType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function IsAvailableCoreAsync ( 
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
    ) override
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
eventType [NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
##  __См. также
#### Ссылки
[DocumentNumberDirector -
](T_Tessa_Extensions_Default_Shared_Numbers_DocumentNumberDirector.htm)
[Tessa.Extensions.Default.Shared.Numbers - пространство
имён](N_Tessa_Extensions_Default_Shared_Numbers.htm)
