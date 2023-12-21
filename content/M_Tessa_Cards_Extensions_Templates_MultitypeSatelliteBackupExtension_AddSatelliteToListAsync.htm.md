# MultitypeSatelliteBackupExtension.AddSatelliteToListAsync - метод
Добавляет карточку-сателлит в список сателлитов, которые относятся к текущему
расширению и сохраняются в информации по основной карточке mainCard.Info. Если
список отсутствовал, то он должен быть создан в этом методе.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask AddSatelliteToListAsync(
    	Card mainCard,
    	Card satellite,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function AddSatelliteToListAsync ( 
    	mainCard As Card,
    	satellite As Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask AddSatelliteToListAsync(
    	Card^ mainCard, 
    	Card^ satellite, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract AddSatelliteToListAsync : 
            mainCard : Card * 
            satellite : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Основная карточка, в информации по которой требуется сохранить структуру сателлита.
satellite [Card](T_Tessa_Cards_Card.htm)
    Карточка-сателлит, структура которой сохраняется.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[MultitypeSatelliteBackupExtension -
](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteBackupExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
