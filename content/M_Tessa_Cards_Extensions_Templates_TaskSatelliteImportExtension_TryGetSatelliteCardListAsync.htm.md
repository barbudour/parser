# TaskSatelliteImportExtension.TryGetSatelliteCardListAsync - метод
Возвращает список карточек-сателлитов для задач, которые были установлены в
пакете основной карточки, или null, если карточки-сателлиты отсутствуют
(аналогично пустому списку).
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
    Пакет основной карточки, в которой может быть установлен список карточек-сателлитов для задач.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Card](T_Tessa_Cards_Card.htm)>>  
Список карточек-сателлитов для задач, которые были установлены в пакете
основной карточки, или null, если карточки-сателлиты отсутствуют (аналогично
пустому списку).
## __См. также
#### Ссылки
[TaskSatelliteImportExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteImportExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
