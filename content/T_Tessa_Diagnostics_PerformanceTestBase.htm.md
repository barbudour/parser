# PerformanceTestBase - класс
##  __Definition
 **Пространство имён:** [Tessa.Diagnostics](N_Tessa_Diagnostics.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class PerformanceTestBase : IPerformanceTest, 
    	IPerformanceCounter
VB __Копировать
     Public MustInherit Class PerformanceTestBase
    	Implements IPerformanceTest, IPerformanceCounter
C++ __Копировать
     public ref class PerformanceTestBase abstract : IPerformanceTest, 
    	IPerformanceCounter
F# __Копировать
     [<AbstractClassAttribute>]
    type PerformanceTestBase = 
        class
            interface IPerformanceTest
            interface IPerformanceCounter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PerformanceTestBase
Derived
[Tessa.Diagnostics.PerformanceTest](T_Tessa_Diagnostics_PerformanceTest.htm)
[Tessa.Diagnostics.PerformanceTestGroup](T_Tessa_Diagnostics_PerformanceTestGroup.htm)
Implements
    [IPerformanceCounter](T_Tessa_Diagnostics_IPerformanceCounter.htm), [IPerformanceTest](T_Tessa_Diagnostics_IPerformanceTest.htm)
##  __Свойства
[Group](P_Tessa_Diagnostics_PerformanceTestBase_Group.htm)|  
---|---  
[IsFaulted](P_Tessa_Diagnostics_PerformanceTestBase_IsFaulted.htm)|  
[IsRunning](P_Tessa_Diagnostics_PerformanceTestBase_IsRunning.htm)|  
[Name](P_Tessa_Diagnostics_PerformanceTestBase_Name.htm)|  
[Status](P_Tessa_Diagnostics_PerformanceTestBase_Status.htm)|  
[Value](P_Tessa_Diagnostics_PerformanceTestBase_Value.htm)|  
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
[OnStarted](M_Tessa_Diagnostics_PerformanceTestBase_OnStarted.htm)|  
[OnStopping](M_Tessa_Diagnostics_PerformanceTestBase_OnStopping.htm)|  
[Start](M_Tessa_Diagnostics_PerformanceTestBase_Start.htm)|  
[Stop](M_Tessa_Diagnostics_PerformanceTestBase_Stop.htm)|  
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
[Tessa.Diagnostics - пространство имён](N_Tessa_Diagnostics.htm)
