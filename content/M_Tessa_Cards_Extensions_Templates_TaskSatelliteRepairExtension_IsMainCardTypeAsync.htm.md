# TaskSatelliteRepairExtension.IsMainCardTypeAsync - метод
Возвращает признак того, что заданный тип является типом основной карточки, к
которой относится карточка-сателлит.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask<bool> IsMainCardTypeAsync(
    	CardType cardType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function IsMainCardTypeAsync ( 
    	cardType As CardType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     protected:
    virtual ValueTask<bool> IsMainCardTypeAsync(
    	CardType^ cardType, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract IsMainCardTypeAsync : 
            cardType : CardType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип, который требуется проверить.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если заданный тип является типом основной карточки, к которой относится
карточка-сателлит; false в противном случае.
## __См. также
#### Ссылки
[TaskSatelliteRepairExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteRepairExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
