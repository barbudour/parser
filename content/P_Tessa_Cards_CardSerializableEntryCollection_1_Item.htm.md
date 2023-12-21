# CardSerializableEntryCollection<T>.Item(Guid) - свойство
Возвращает элемент коллекции по его идентификатору.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public T this[
    	Guid id
    ] { get; }
VB __Копировать
     Public ReadOnly Default Property Item ( 
    	id As Guid
    ) As T
    	Get
C++ __Копировать
     public:
    property T default[Guid id] {
    	T get (Guid id);
    }
F# __Копировать
     member Item : 'T with get
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор элемента.
#### Возвращаемое значение
[T](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)  
Элемент, полученный по заданному идентификатору.
##  __См. также
#### Ссылки
[CardSerializableEntryCollection<T> \-
](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
[Item -
перегрузка](Overload_Tessa_Cards_CardSerializableEntryCollection_1_Item.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
