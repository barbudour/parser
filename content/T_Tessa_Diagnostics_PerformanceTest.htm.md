# PerformanceTest - класс
##  __Definition
 **Пространство имён:** [Tessa.Diagnostics](N_Tessa_Diagnostics.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PerformanceTest : PerformanceTestBase
VB __Копировать
     Public NotInheritable Class PerformanceTest
    	Inherits PerformanceTestBase
C++ __Копировать
     public ref class PerformanceTest sealed : public PerformanceTestBase
F# __Копировать
     [<SealedAttribute>]
    type PerformanceTest = 
        class
            inherit PerformanceTestBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[PerformanceTestBase](T_Tessa_Diagnostics_PerformanceTestBase.htm) __ PerformanceTest
##  __Конструкторы
[PerformanceTest(String, TimeSpan,
Action)](M_Tessa_Diagnostics_PerformanceTest__ctor.htm)| Инициализирует новый
экземпляр класса PerformanceTest  
---|---  
[PerformanceTest(String, TimeSpan, Action, Action,
Action)](M_Tessa_Diagnostics_PerformanceTest__ctor_1.htm)| Инициализирует
новый экземпляр класса PerformanceTest  
[PerformanceTest(String, TimeSpan, Int32, Action, Action,
Action)](M_Tessa_Diagnostics_PerformanceTest__ctor_2.htm)| Инициализирует
новый экземпляр класса PerformanceTest  
##  __Свойства
[Executed](P_Tessa_Diagnostics_PerformanceTest_Executed.htm)|  
---|---  
[Group](P_Tessa_Diagnostics_PerformanceTestBase_Group.htm)|  
(Унаследован от
[PerformanceTestBase](T_Tessa_Diagnostics_PerformanceTestBase.htm))  
[Interval](P_Tessa_Diagnostics_PerformanceTest_Interval.htm)|  
[IsFaulted](P_Tessa_Diagnostics_PerformanceTestBase_IsFaulted.htm)|  
(Унаследован от
[PerformanceTestBase](T_Tessa_Diagnostics_PerformanceTestBase.htm))  
[IsRunning](P_Tessa_Diagnostics_PerformanceTestBase_IsRunning.htm)|  
(Унаследован от
[PerformanceTestBase](T_Tessa_Diagnostics_PerformanceTestBase.htm))  
[MaxDegreeOfParallelism](P_Tessa_Diagnostics_PerformanceTest_MaxDegreeOfParallelism.htm)|  
[Maximum](P_Tessa_Diagnostics_PerformanceTest_Maximum.htm)|  
[Minimum](P_Tessa_Diagnostics_PerformanceTest_Minimum.htm)|  
[Name](P_Tessa_Diagnostics_PerformanceTestBase_Name.htm)|  
(Унаследован от
[PerformanceTestBase](T_Tessa_Diagnostics_PerformanceTestBase.htm))  
[Started](P_Tessa_Diagnostics_PerformanceTest_Started.htm)|  
[Status](P_Tessa_Diagnostics_PerformanceTestBase_Status.htm)|  
(Унаследован от
[PerformanceTestBase](T_Tessa_Diagnostics_PerformanceTestBase.htm))  
[Value](P_Tessa_Diagnostics_PerformanceTest_Value.htm)|  
(Переопределяет
[PerformanceTestBase.Value](P_Tessa_Diagnostics_PerformanceTestBase_Value.htm))  
##  __Методы
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
[OnStarted](M_Tessa_Diagnostics_PerformanceTest_OnStarted.htm)|  
(Переопределяет
[PerformanceTestBase.OnStarted()](M_Tessa_Diagnostics_PerformanceTestBase_OnStarted.htm))  
[OnStopping](M_Tessa_Diagnostics_PerformanceTest_OnStopping.htm)|  
(Переопределяет
[PerformanceTestBase.OnStopping()](M_Tessa_Diagnostics_PerformanceTestBase_OnStopping.htm))  
[Start](M_Tessa_Diagnostics_PerformanceTestBase_Start.htm)|  
(Унаследован от
[PerformanceTestBase](T_Tessa_Diagnostics_PerformanceTestBase.htm))  
[Stop](M_Tessa_Diagnostics_PerformanceTestBase_Stop.htm)|  
(Унаследован от
[PerformanceTestBase](T_Tessa_Diagnostics_PerformanceTestBase.htm))  
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
