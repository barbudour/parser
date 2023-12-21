# MultitypeSatelliteExportExtension.ClearSatelliteListAsync - метод
Удаляет все карточки-сателлиты в списке сателлитов, которые относятся к
текущему расширению и сохраняются в информации по основной карточке
mainCard.Info.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask ClearSatelliteListAsync(
    	Card mainCard,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function ClearSatelliteListAsync ( 
    	mainCard As Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask ClearSatelliteListAsync(
    	Card^ mainCard, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract ClearSatelliteListAsync : 
            mainCard : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
     Основная карточка, в информации по которой требуется удалить список с карточками-сателлитами. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[MultitypeSatelliteExportExtension -
](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteExportExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
