# SchemeObjectCollectionStructuralComparer<T> \- класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SchemeObjectCollectionStructuralComparer<T> : IEqualityComparer<SchemeObjectCollection<T>>
    where T : SchemeObject
VB __Копировать
     Public NotInheritable Class SchemeObjectCollectionStructuralComparer(Of T As SchemeObject)
    	Implements IEqualityComparer(Of SchemeObjectCollection(Of T))
C++ __Копировать
    generic<typename T>
    where T : SchemeObject
    public ref class SchemeObjectCollectionStructuralComparer sealed : IEqualityComparer<SchemeObjectCollection<T>^>
F# __Копировать
     [<SealedAttribute>]
    type SchemeObjectCollectionStructuralComparer<'T when 'T : SchemeObject> = 
        class
            interface IEqualityComparer<SchemeObjectCollection<'T>>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SchemeObjectCollectionStructuralComparer<T>
Implements
    [IEqualityComparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1)<[SchemeObjectCollection](T_Tessa_Scheme_SchemeObjectCollection_1.htm)<T>>
#### Параметры типа
T
##  __Конструкторы
[SchemeObjectCollectionStructuralComparer<T>](M_Tessa_Scheme_SchemeObjectCollectionStructuralComparer_1__ctor.htm)|
Инициализирует новый экземпляр класса
SchemeObjectCollectionStructuralComparer<T>  
---|---  
##  __Методы
[Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Equals(SchemeObjectCollection<T>,
SchemeObjectCollection<T>)](M_Tessa_Scheme_SchemeObjectCollectionStructuralComparer_1_Equals.htm)|  
[Equals(SchemeObjectCollection<T>, SchemeObjectCollection<T>,
Boolean)](M_Tessa_Scheme_SchemeObjectCollectionStructuralComparer_1_Equals_1.htm)|  
[EqualsStatic](M_Tessa_Scheme_SchemeObjectCollectionStructuralComparer_1_EqualsStatic.htm)|  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode(SchemeObjectCollection<T>)](M_Tessa_Scheme_SchemeObjectCollectionStructuralComparer_1_GetHashCode.htm)|  
[GetHashCode(SchemeObjectCollection<T>,
Boolean)](M_Tessa_Scheme_SchemeObjectCollectionStructuralComparer_1_GetHashCode_1.htm)|  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
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
[Tessa.Scheme - пространство имён](N_Tessa_Scheme.htm)
