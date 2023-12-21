# CardTypePriorityComparer.Compare - метод
When overridden in a derived class, performs a comparison of two objects of
the same type and returns a value indicating whether one object is less than,
equal to, or greater than the other.
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow](N_Tessa_Extensions_Default_Shared_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public override int Compare(
    	Card? x,
    	Card? y
    )
VB __Копировать
     Public Overrides Function Compare ( 
    	x As Card,
    	y As Card
    ) As Integer
C++ __Копировать
     public:
    virtual int Compare(
    	Card^ x, 
    	Card^ y
    ) override
F# __Копировать
     abstract Compare : 
            x : Card * 
            y : Card -> int 
    override Compare : 
            x : Card * 
            y : Card -> int 
#### Параметры
x [Card](T_Tessa_Cards_Card.htm)
    The first object to compare.
y [Card](T_Tessa_Cards_Card.htm)
    The second object to compare.
#### Возвращаемое значение
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)  
A signed integer that indicates the relative values of x and y, as shown in
the following table. Value Meaning Less than zero x is less than y. Zero x
equals y. Greater than zero x is greater than y.
#### Реализации
[IComparer<T>.Compare(T,
T)](https://learn.microsoft.com/dotnet/api/system.collections.generic.icomparer-1.compare#system-
collections-generic-icomparer-1-compare\(-0-0\))  
[IComparer<T>.Compare(T,
T)](https://learn.microsoft.com/dotnet/api/system.collections.generic.icomparer-1.compare#system-
collections-generic-icomparer-1-compare\(-0-0\))  
##  __Исключения
[ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception)|
Type T does not implement either the
[IComparable<T>](https://learn.microsoft.com/dotnet/api/system.icomparable-1)
generic interface or the
[IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable)
interface.  
---|---  
##  __См. также
#### Ссылки
[CardTypePriorityComparer -
](T_Tessa_Extensions_Default_Shared_Workflow_CardTypePriorityComparer.htm)
[Tessa.Extensions.Default.Shared.Workflow - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow.htm)
