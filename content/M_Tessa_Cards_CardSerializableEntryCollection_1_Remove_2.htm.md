# CardSerializableEntryCollection<T>.Remove(T) - метод
Удаляет заданный элемент из коллекции.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool Remove(
    	T item
    )
VB __Копировать
     Public Function Remove ( 
    	item As T
    ) As Boolean
C++ __Копировать
     public:
    virtual bool Remove(
    	T item
    ) sealed
F# __Копировать
     abstract Remove : 
            item : 'T -> bool 
    override Remove : 
            item : 'T -> bool 
#### Параметры
item [T](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
    Элемент, который должен быть удалён из коллекции.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если элемент был удалён из коллекции; false, если элемент не был найден.
#### Реализации
[ICollection<T>.Remove(T)](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.remove#system-
collections-generic-icollection-1-remove\(-0\))  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardSerializableEntryCollection<T> \-
](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
[Remove -
перегрузка](Overload_Tessa_Cards_CardSerializableEntryCollection_1_Remove.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
