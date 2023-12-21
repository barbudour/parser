# CardSatelliteDeleteExtension.SatelliteCardWasNotFoundAsync - метод
Возвращает признак того, что карточка-сателлит была установлена как
отсутствующая в пакете основной карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask<bool> SatelliteCardWasNotFoundAsync(
    	Card mainCard,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function SatelliteCardWasNotFoundAsync ( 
    	mainCard As Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     protected:
    virtual ValueTask<bool> SatelliteCardWasNotFoundAsync(
    	Card^ mainCard, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract SatelliteCardWasNotFoundAsync : 
            mainCard : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Пакет основной карточки, в которой может быть установлена карточка-сателлит.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если карточка-сателлит была установлена как отсутствующая в пакете
основной карточки; false в противном случае.
## __См. также
#### Ссылки
[CardSatelliteDeleteExtension -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteDeleteExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
