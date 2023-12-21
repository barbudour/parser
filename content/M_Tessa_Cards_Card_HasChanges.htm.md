# Card.HasChanges - метод
Возвращает признак того, что хотя бы одна секция карточки или одна из
вложенных карточек файлов или заданий содержит изменения.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool HasChanges(
    	bool checkStates = true
    )
VB __Копировать
     Public Function HasChanges ( 
    	Optional checkStates As Boolean = true
    ) As Boolean
C++ __Копировать
     public:
    bool HasChanges(
    	bool checkStates = true
    )
F# __Копировать
     member HasChanges : 
            ?checkStates : bool 
    (* Defaults:
            let _checkStates = defaultArg checkStates true
    *)
    -> bool 
#### Параметры
checkStates [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
     Признак того, что требуется проверить состояние всех вложенных заданий и файлов, а не только данные их карточек. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если карточка содержит изменения; false в противном случае.
## __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
