# GroupPosition - структура
Положение относительно этапов, добавленных вручную.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrCompilers](N_Tessa_Extensions_Default_Shared_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public readonly struct GroupPosition : IEquatable<GroupPosition>, 
    	IComparable<GroupPosition>
VB __Копировать
     Public Structure GroupPosition
    	Implements IEquatable(Of GroupPosition), IComparable(Of GroupPosition)
C++ __Копировать
     public value class GroupPosition : IEquatable<GroupPosition>, 
    	IComparable<GroupPosition>
F# __Копировать
     [<SealedAttribute>]
    type GroupPosition = 
        struct
            inherit ValueType
            interface IEquatable<GroupPosition>
            interface IComparable<GroupPosition>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ GroupPosition
Implements
    [IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable-1)<GroupPosition>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<GroupPosition>
##  __Конструкторы
[GroupPosition](M_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition__ctor.htm)|
Инициализирует новый экземпляр GroupPosition.  
---|---  
## __Свойства
[AtFirst](P_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_AtFirst.htm)|
В начале группы.  
---|---  
[AtLast](P_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_AtLast.htm)|
В конце группы.  
[ID](P_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_ID.htm)|
Идентификатор положения относительно этапов, добавленных вручную.  
[Unspecified](P_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_Unspecified.htm)|
Информация о положении не определена.  
## __Методы
[CompareTo](M_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_CompareTo.htm)|
Compares the current instance with another object of the same type and returns
an integer that indicates whether the current instance precedes, follows, or
occurs in the same position in the sort order as the other object.  
---|---  
[Equals(GroupPosition)](M_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_Equals_1.htm)|
Indicates whether the current object is equal to another object of the same
type.  
[Equals(Object)](M_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_Equals.htm)|
Indicates whether this instance and a specified object are equal.  
(Переопределяет
[ValueType.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetByID(Nullable<Int32>)](M_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_GetByID.htm)|
Возвращает объект GroupPosition в соответствии с заданным идентификатором
положения относительно этапов, добавленных вручную.  
[GetByID(Object)](M_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_GetByID_1.htm)|
Возвращает объект GroupPosition в соответствии с заданным идентификатором
положения относительно этапов, добавленных вручную.  
[GetHashCode](M_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_GetHashCode.htm)|
Returns the hash code for this instance.  
(Переопределяет
[ValueType.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](M_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_ToString.htm)|
Returns the fully qualified type name of this instance.  
(Переопределяет
[ValueType.ToString()](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring))  
##  __Операторы
[Equality(GroupPosition,
GroupPosition)](M_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_op_Equality.htm)|  
---|---  
[Inequality(GroupPosition,
GroupPosition)](M_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition_op_Inequality.htm)|  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrCompilers.htm)
