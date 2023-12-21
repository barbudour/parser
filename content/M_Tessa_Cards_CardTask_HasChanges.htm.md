# CardTask.HasChanges - метод
Возвращает признак того, что карточка задания содержит изменённые значения.
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
     Признак того, что требуется проверить состояние задания и вложенных в него файлов, а не только их данные. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если карточка задания содержит изменённые значения; false в противном
случае.
## __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
