# CardSerializableEntryCollection<T>.Add - метод
Добавляет заданный элемент в коллекцию.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void Add(
    	T item
    )
VB __Копировать
     Public Sub Add ( 
    	item As T
    )
C++ __Копировать
     public:
    virtual void Add(
    	T item
    ) sealed
F# __Копировать
     abstract Add : 
            item : 'T -> unit 
    override Add : 
            item : 'T -> unit 
#### Параметры
item [T](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
    Элемент, добавляемый в коллекцию.
#### Реализации
[ICollection<T>.Add(T)](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.add#system-
collections-generic-icollection-1-add\(-0\))  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardSerializableEntryCollection<T> \-
](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
