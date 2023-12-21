# CardSerializableEntryCollection<T>.Item(Int32) - свойство
Возвращает элемент коллекции по его индексу в списке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public T this[
    	int index
    ] { get; }
VB __Копировать
     Public ReadOnly Default Property Item ( 
    	index As Integer
    ) As T
    	Get
C++ __Копировать
     public:
    virtual property T default[int index] {
    	T get (int index) sealed;
    }
F# __Копировать
     abstract Item : 'T with get
    override Item : 'T with get
#### Параметры
index [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Индекс элемента в списке.
#### Возвращаемое значение
[T](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)  
Элемент, полученный по заданному индексу.
#### Реализации
[IReadOnlyList<T>.Item[Int32]](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1.item#system-
collections-generic-ireadonlylist-1-item\(system-int32\))  
##  __См. также
#### Ссылки
[CardSerializableEntryCollection<T> \-
](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
[Item -
перегрузка](Overload_Tessa_Cards_CardSerializableEntryCollection_1_Item.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
