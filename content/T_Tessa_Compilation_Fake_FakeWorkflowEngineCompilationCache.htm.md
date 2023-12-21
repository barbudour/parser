# FakeWorkflowEngineCompilationCache - класс
Фейковая реализация для
[IWorkflowEngineCompilationCache](T_Tessa_Workflow_Compilation_IWorkflowEngineCompilationCache.htm).
## __Definition
 **Пространство имён:** [Tessa.Compilation.Fake](N_Tessa_Compilation_Fake.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FakeWorkflowEngineCompilationCache : IWorkflowEngineCompilationCache
VB __Копировать
     Public NotInheritable Class FakeWorkflowEngineCompilationCache
    	Implements IWorkflowEngineCompilationCache
C++ __Копировать
     public ref class FakeWorkflowEngineCompilationCache sealed : IWorkflowEngineCompilationCache
F# __Копировать
     [<SealedAttribute>]
    type FakeWorkflowEngineCompilationCache = 
        class
            interface IWorkflowEngineCompilationCache
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FakeWorkflowEngineCompilationCache
Implements
    [IWorkflowEngineCompilationCache](T_Tessa_Workflow_Compilation_IWorkflowEngineCompilationCache.htm)
##  __Конструкторы
[FakeWorkflowEngineCompilationCache](M_Tessa_Compilation_Fake_FakeWorkflowEngineCompilationCache__ctor.htm)|
Инициализирует новый экземпляр класса FakeWorkflowEngineCompilationCache  
---|---  
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
[GetAsync](M_Tessa_Compilation_Fake_FakeWorkflowEngineCompilationCache_GetAsync.htm)|
Получение значения из кэша по ID версии шаблона процесса  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetTilesAsync](M_Tessa_Compilation_Fake_FakeWorkflowEngineCompilationCache_GetTilesAsync.htm)|
Получение значения из кэша по ID карточки шаблона процесса  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateAllAsync](M_Tessa_Compilation_Fake_FakeWorkflowEngineCompilationCache_InvalidateAllAsync.htm)|
Метод для сброса кеша всех процессов  
[InvalidateAsync](M_Tessa_Compilation_Fake_FakeWorkflowEngineCompilationCache_InvalidateAsync.htm)|
Сброс кэша по ID версии шаблона процесса. В случае ошибки при инвалидации
файла со сборкой, возвращает
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm).  
[InvalidateCardAsync](M_Tessa_Compilation_Fake_FakeWorkflowEngineCompilationCache_InvalidateCardAsync.htm)|
Сброс кэша по ID карточки процесса. В случае ошибки при инвалидации файла со
сборкой, возвращает
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm).  
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
[Tessa.Compilation.Fake - пространство имён](N_Tessa_Compilation_Fake.htm)
