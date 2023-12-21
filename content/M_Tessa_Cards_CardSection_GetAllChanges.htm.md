# CardSection.GetAllChanges - метод
Возвращает коллекцию ключей всех объектов, значения которых были изменены.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICollection<string> GetAllChanges()
VB __Копировать
     Public Function GetAllChanges As ICollection(Of String)
C++ __Копировать
     public:
    virtual ICollection<String^>^ GetAllChanges() sealed
F# __Копировать
     abstract GetAllChanges : unit -> ICollection<string> 
    override GetAllChanges : unit -> ICollection<string> 
#### Возвращаемое значение
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Коллекция ключей всех объектов, значения которых были изменены.
#### Реализации
[IStorageObjectStateProvider.GetAllChanges()](M_Tessa_Platform_Storage_IStorageObjectStateProvider_GetAllChanges.htm)  
##  __См. также
#### Ссылки
[CardSection - ](T_Tessa_Cards_CardSection.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
