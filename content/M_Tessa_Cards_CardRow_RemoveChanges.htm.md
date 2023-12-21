# CardRow.RemoveChanges - метод
Выполняет удаление информации по состояниям, из которой можно было бы
определить, что строка изменена. Возвращает признак того, что при этом были
внесены изменения.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool RemoveChanges(
    	CardTableType tableType,
    	CardRemoveChangesDeletedHandling deletedHandling = CardRemoveChangesDeletedHandling.ResetToNone
    )
VB __Копировать
     Public Function RemoveChanges ( 
    	tableType As CardTableType,
    	Optional deletedHandling As CardRemoveChangesDeletedHandling = CardRemoveChangesDeletedHandling.ResetToNone
    ) As Boolean
C++ __Копировать
     public:
    bool RemoveChanges(
    	CardTableType tableType, 
    	CardRemoveChangesDeletedHandling deletedHandling = CardRemoveChangesDeletedHandling::ResetToNone
    )
F# __Копировать
     member RemoveChanges : 
            tableType : CardTableType * 
            ?deletedHandling : CardRemoveChangesDeletedHandling 
    (* Defaults:
            let _deletedHandling = defaultArg deletedHandling CardRemoveChangesDeletedHandling.ResetToNone
    *)
    -> bool 
#### Параметры
tableType [CardTableType](T_Tessa_Cards_CardTableType.htm)
    Тип секции, в которую включена строка.
deletedHandling
[CardRemoveChangesDeletedHandling](T_Tessa_Cards_CardRemoveChangesDeletedHandling.htm)
(Optional)
    Способ обработки удалённых строк, файлов и заданий.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если в процессе удаления были внесены изменения; false в противном
случае.
## __См. также
#### Ссылки
[CardRow - ](T_Tessa_Cards_CardRow.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
