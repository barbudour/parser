# AggregateFinder<T> \- класс
Выполняет поиск типов T, используя несколько других объектов
[IFinder<T>](T_Tessa_Platform_Composition_IFinder_1.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.Composition](N_Tessa_Platform_Composition.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class AggregateFinder<T> : IFinder<T>
VB __Копировать
     Public NotInheritable Class AggregateFinder(Of T)
    	Implements IFinder(Of T)
C++ __Копировать
    generic<typename T>
    public ref class AggregateFinder sealed : IFinder<T>
F# __Копировать
     [<SealedAttribute>]
    type AggregateFinder<'T> = 
        class
            interface IFinder<'T>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AggregateFinder<T>
Implements
    [IFinder](T_Tessa_Platform_Composition_IFinder_1.htm)<T>
#### Параметры типа
T
    Тип искомых объектов.
##  __Конструкторы
[AggregateFinder<T>](M_Tessa_Platform_Composition_AggregateFinder_1__ctor.htm)|
Инициализирует новый экземпляр класса AggregateFinder<T>  
---|---  
##  __Свойства
[Finders](P_Tessa_Platform_Composition_AggregateFinder_1_Finders.htm)|
Объекты, используемые для поиска.  
---|---  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Find](M_Tessa_Platform_Composition_AggregateFinder_1_Find.htm)| Выполняет
поиск объектов регистраторов и возвращает список объектов, описывающих искомые
объекты.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Platform.Composition - пространство
имён](N_Tessa_Platform_Composition.htm)
