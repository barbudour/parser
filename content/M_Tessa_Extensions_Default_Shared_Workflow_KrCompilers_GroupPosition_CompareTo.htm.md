# GroupPosition.CompareTo - метод
Compares the current instance with another object of the same type and returns
an integer that indicates whether the current instance precedes, follows, or
occurs in the same position in the sort order as the other object.
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrCompilers](N_Tessa_Extensions_Default_Shared_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public int CompareTo(
    	GroupPosition other
    )
VB __Копировать
     Public Function CompareTo ( 
    	other As GroupPosition
    ) As Integer
C++ __Копировать
     public:
    virtual int CompareTo(
    	GroupPosition other
    ) sealed
F# __Копировать
     abstract CompareTo : 
            other : GroupPosition -> int 
    override CompareTo : 
            other : GroupPosition -> int 
#### Параметры
other
[GroupPosition](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition.htm)
    An object to compare with this instance.
#### Возвращаемое значение
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)  
A value that indicates the relative order of the objects being compared. The
return value has these meanings: Value Meaning Less than zero This instance
precedes other in the sort order. Zero This instance occurs in the same
position in the sort order as other. Greater than zero This instance follows
other in the sort order.
#### Реализации
[IComparable<T>.CompareTo(T)](https://learn.microsoft.com/dotnet/api/system.icomparable-1.compareto#system-
icomparable-1-compareto\(-0\))  
##  __См. также
#### Ссылки
[GroupPosition -
](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrCompilers.htm)
