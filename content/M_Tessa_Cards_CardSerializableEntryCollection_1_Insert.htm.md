# CardSerializableEntryCollection<T>.Insert - метод
Вставляет элемент в заданную позицию.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void Insert(
    	int index,
    	T item
    )
VB __Копировать
     Public Sub Insert ( 
    	index As Integer,
    	item As T
    )
C++ __Копировать
     public:
    virtual void Insert(
    	int index, 
    	T item
    ) sealed
F# __Копировать
     abstract Insert : 
            index : int * 
            item : 'T -> unit 
    override Insert : 
            index : int * 
            item : 'T -> unit 
#### Параметры
index [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Отсчитываемый от нуля индекс позиции вставки.
item [T](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
    Вставляемый элемент.
#### Реализации
[IList<T>.Insert(Int32,
T)](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1.insert#system-
collections-generic-ilist-1-insert\(system-int32-0\))  
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
