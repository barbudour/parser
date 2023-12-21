# CardSerializableEntry.Equals(ICardSerializableEntry) - метод
Сравнивает текущий объект с заданным.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool Equals(
    	ICardSerializableEntry other
    )
VB __Копировать
     Public Function Equals ( 
    	other As ICardSerializableEntry
    ) As Boolean
C++ __Копировать
     public:
    virtual bool Equals(
    	ICardSerializableEntry^ other
    ) sealed
F# __Копировать
     abstract Equals : 
            other : ICardSerializableEntry -> bool 
    override Equals : 
            other : ICardSerializableEntry -> bool 
#### Параметры
other [ICardSerializableEntry](T_Tessa_Cards_ICardSerializableEntry.htm)
    Объект, с которым сравнивается текущий объект.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если объекты равны; false в противном случае.
#### Реализации
[IEquatable<T>.Equals(T)](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))  
##  __Заметки
Объекты сравниваются по идентификатору.
##  __См. также
#### Ссылки
[CardSerializableEntry - ](T_Tessa_Cards_CardSerializableEntry.htm)
[Equals - перегрузка](Overload_Tessa_Cards_CardSerializableEntry_Equals.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
