# CardSatelliteImportExtension.TryGetSatelliteCardAsync - метод
Возвращает карточку-сателлит, которая была установлена в пакете основной
карточки, или null, если карточка-сателлит не была установлена или была
установлена как отсутствующая.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask<Card> TryGetSatelliteCardAsync(
    	Card mainCard,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function TryGetSatelliteCardAsync ( 
    	mainCard As Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Card)
C++ __Копировать
     protected:
    virtual ValueTask<Card^> TryGetSatelliteCardAsync(
    	Card^ mainCard, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract TryGetSatelliteCardAsync : 
            mainCard : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Card> 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Пакет основной карточки, в которой может быть установлена карточка-сателлит.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Card](T_Tessa_Cards_Card.htm)>  
Карточку-сателлит, которая была установлена в пакете основной карточки, или
null, если карточка-сателлит не была установлена или была установлена как
отсутствующая.
## __См. также
#### Ссылки
[CardSatelliteImportExtension -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteImportExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
