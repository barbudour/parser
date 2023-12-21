# CardSatelliteGetExtension.SetSatelliteMainCardIDAsync - метод
Устанавливает идентификатор основной карточки в карточке-сателлите.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask SetSatelliteMainCardIDAsync(
    	Card satellite,
    	Guid mainCardID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function SetSatelliteMainCardIDAsync ( 
    	satellite As Card,
    	mainCardID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask SetSatelliteMainCardIDAsync(
    	Card^ satellite, 
    	Guid mainCardID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract SetSatelliteMainCardIDAsync : 
            satellite : Card * 
            mainCardID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
satellite [Card](T_Tessa_Cards_Card.htm)
    Пакет карточки-сателлита.
mainCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор основной карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
