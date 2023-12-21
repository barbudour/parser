# CardSerializableEntryCollection<T>.RemoveAt - метод
Удаляет элемент в заданной позиции.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void RemoveAt(
    	int index
    )
VB __Копировать
     Public Sub RemoveAt ( 
    	index As Integer
    )
C++ __Копировать
     public:
    virtual void RemoveAt(
    	int index
    ) sealed
F# __Копировать
     abstract RemoveAt : 
            index : int -> unit 
    override RemoveAt : 
            index : int -> unit 
#### Параметры
index [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Отсчитываемый от нуля индекс удаляемого элемента.
#### Реализации
[IList<T>.RemoveAt(Int32)](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1.removeat#system-
collections-generic-ilist-1-removeat\(system-int32\))  
[IList.RemoveAt(Int32)](https://learn.microsoft.com/dotnet/api/system.collections.ilist.removeat#system-
collections-ilist-removeat\(system-int32\))  
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
