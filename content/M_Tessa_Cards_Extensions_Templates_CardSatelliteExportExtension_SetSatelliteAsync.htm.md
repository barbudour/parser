# CardSatelliteExportExtension.SetSatelliteAsync - метод
Сохраняет карточку-сателлит в пакете основной карточки.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask SetSatelliteAsync(
    	Card mainCard,
    	Card satellite,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function SetSatelliteAsync ( 
    	mainCard As Card,
    	satellite As Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask SetSatelliteAsync(
    	Card^ mainCard, 
    	Card^ satellite, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract SetSatelliteAsync : 
            mainCard : Card * 
            satellite : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Пакет основной карточки.
satellite [Card](T_Tessa_Cards_Card.htm)
     Карточка-сателлит или null, если карточка-сателлит ещё не создана. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardSatelliteExportExtension -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteExportExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
