# CardSection.HasChanges - метод
Возвращает признак того, что объект содержит изменённые значения.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool HasChanges()
VB __Копировать
     Public Function HasChanges As Boolean
C++ __Копировать
     public:
    virtual bool HasChanges() sealed
F# __Копировать
     abstract HasChanges : unit -> bool 
    override HasChanges : unit -> bool 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если объект содержит изменённые значения; false в противном случае.
#### Реализации
[IStorageObjectStateProvider.HasChanges()](M_Tessa_Platform_Storage_IStorageObjectStateProvider_HasChanges.htm)  
##  __Заметки
Для строковой секции проверяется наличие изменений в её полях, а для
коллекционной и древовидной секции - наличие изменений хотя бы в одной её
строке.
## __См. также
#### Ссылки
[CardSection - ](T_Tessa_Cards_CardSection.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
