# ApplicationModel.CompareTo(Object) - метод
Compares the current instance with another object of the same type and returns
an integer that indicates whether the current instance precedes, follows, or
occurs in the same position in the sort order as the other object.
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public int CompareTo(
    	Object obj
    )
VB __Копировать
     Public Function CompareTo ( 
    	obj As Object
    ) As Integer
C++ __Копировать
     public:
    virtual int CompareTo(
    	Object^ obj
    ) sealed
F# __Копировать
     abstract CompareTo : 
            obj : Object -> int 
    override CompareTo : 
            obj : Object -> int 
#### Параметры
obj [Object](https://learn.microsoft.com/dotnet/api/system.object)
    An object to compare with this instance.
#### Возвращаемое значение
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)  
A value that indicates the relative order of the objects being compared. The
return value has these meanings: Value Meaning Less than zero This instance
precedes obj in the sort order. Zero This instance occurs in the same position
in the sort order as obj. Greater than zero This instance follows obj in the
sort order.
#### Реализации
[IComparable.CompareTo(Object)](https://learn.microsoft.com/dotnet/api/system.icomparable.compareto#system-
icomparable-compareto\(system-object\))  
##  __Исключения
[ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception)|
obj is not the same type as this instance.  
---|---  
##  __См. также
#### Ссылки
[ApplicationModel - ](T_Tessa_Applications_ApplicationModel.htm)
[CompareTo -
перегрузка](Overload_Tessa_Applications_ApplicationModel_CompareTo.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
