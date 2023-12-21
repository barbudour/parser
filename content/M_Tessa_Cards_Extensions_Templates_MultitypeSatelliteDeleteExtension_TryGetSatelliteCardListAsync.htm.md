# MultitypeSatelliteDeleteExtension.TryGetSatelliteCardListAsync - метод
Возвращает список с карточками-сателлитами, которые относятся к текущему
расширению, где список получен по данным основной карточки mainCard.Info, или
null, если список не был установлен.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask<List<Card>> TryGetSatelliteCardListAsync(
    	Card mainCard,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function TryGetSatelliteCardListAsync ( 
    	mainCard As Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of List(Of Card))
C++ __Копировать
     protected:
    virtual ValueTask<List<Card^>^> TryGetSatelliteCardListAsync(
    	Card^ mainCard, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract TryGetSatelliteCardListAsync : 
            mainCard : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<List<Card>> 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Основная карточка.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Card](T_Tessa_Cards_Card.htm)>>  
Список с карточками-сателлитами, которые относятся к текущему расширению, где
список получен по данным основной карточки mainCard.Info, или null, если
список не был установлен.
## __См. также
#### Ссылки
[MultitypeSatelliteDeleteExtension -
](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
