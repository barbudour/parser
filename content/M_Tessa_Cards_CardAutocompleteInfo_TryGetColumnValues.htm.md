# CardAutocompleteInfo.TryGetColumnValues - метод
Возвращает все колонки для выбранной ссылки в порядке, в котором они указаны в
метаинформации по референсной колонке
[ReferenceColumnID](P_Tessa_Cards_CardAutocompleteInfo_ReferenceColumnID.htm)
внутри секции
[ReferenceSectionID](P_Tessa_Cards_CardAutocompleteInfo_ReferenceSectionID.htm),
или null, если колонки ещё не были заданы.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ListStorage<Object> TryGetColumnValues()
VB __Копировать
     Public Function TryGetColumnValues As ListStorage(Of Object)
C++ __Копировать
     public:
    ListStorage<Object^>^ TryGetColumnValues()
F# __Копировать
     member TryGetColumnValues : unit -> ListStorage<Object> 
#### Возвращаемое значение
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>  
Все колонки для выбранной ссылки в порядке, в котором они указаны в
метаинформации по референсной колонке
[ReferenceColumnID](P_Tessa_Cards_CardAutocompleteInfo_ReferenceColumnID.htm)
внутри секции
[ReferenceSectionID](P_Tessa_Cards_CardAutocompleteInfo_ReferenceSectionID.htm),
или null, если колонки ещё не были заданы.
## __См. также
#### Ссылки
[CardAutocompleteInfo - ](T_Tessa_Cards_CardAutocompleteInfo.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
