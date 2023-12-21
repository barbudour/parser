# CardFile.HasChanges - метод
Возвращает признак того, что карточка файла содержит изменённые значения.
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
     Признак того, что требуется проверить состояние файла, а не только его данные. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если карточка файла содержит изменённые значения; false в противном
случае.
## __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
