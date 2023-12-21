# FakeWorkflowEngineCompiler - класс
Фейковая реализация для
[IWorkflowEngineCompiler](T_Tessa_Workflow_Compilation_IWorkflowEngineCompiler.htm),
[IWorkflowEngineSourceBuilder](T_Tessa_Workflow_Compilation_IWorkflowEngineSourceBuilder.htm)
и
[IWorkflowEngineTilesCompiler](T_Tessa_Workflow_Compilation_IWorkflowEngineTilesCompiler.htm).
## __Definition
 **Пространство имён:** [Tessa.Compilation.Fake](N_Tessa_Compilation_Fake.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FakeWorkflowEngineCompiler : IWorkflowEngineCompiler, 
    	IWorkflowEngineSourceBuilder, IWorkflowEngineTilesCompiler
VB __Копировать
     Public NotInheritable Class FakeWorkflowEngineCompiler
    	Implements IWorkflowEngineCompiler, IWorkflowEngineSourceBuilder, IWorkflowEngineTilesCompiler
C++ __Копировать
     public ref class FakeWorkflowEngineCompiler sealed : IWorkflowEngineCompiler, 
    	IWorkflowEngineSourceBuilder, IWorkflowEngineTilesCompiler
F# __Копировать
     [<SealedAttribute>]
    type FakeWorkflowEngineCompiler = 
        class
            interface IWorkflowEngineCompiler
            interface IWorkflowEngineSourceBuilder
            interface IWorkflowEngineTilesCompiler
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FakeWorkflowEngineCompiler
Implements
    [IWorkflowEngineCompiler](T_Tessa_Workflow_Compilation_IWorkflowEngineCompiler.htm), [IWorkflowEngineSourceBuilder](T_Tessa_Workflow_Compilation_IWorkflowEngineSourceBuilder.htm), [IWorkflowEngineTilesCompiler](T_Tessa_Workflow_Compilation_IWorkflowEngineTilesCompiler.htm)
##  __Конструкторы
[FakeWorkflowEngineCompiler](M_Tessa_Compilation_Fake_FakeWorkflowEngineCompiler__ctor.htm)|
Инициализирует новый экземпляр класса FakeWorkflowEngineCompiler  
---|---  
##  __Свойства
[DefaultReferences](P_Tessa_Compilation_Fake_FakeWorkflowEngineCompiler_DefaultReferences.htm)|
Список зависимостей, используемых данным компилятором по умолчанию  
---|---  
[DefaultUsings](P_Tessa_Compilation_Fake_FakeWorkflowEngineCompiler_DefaultUsings.htm)|
Список юзингов, используемых данным компилятором по умолчанию  
## __Методы
[CompileActionAsync](M_Tessa_Compilation_Fake_FakeWorkflowEngineCompiler_CompileActionAsync.htm)|
Метод для компиляции шаблона действия WorkflowEngine  
---|---  
[CompileLinkAsync](M_Tessa_Compilation_Fake_FakeWorkflowEngineCompiler_CompileLinkAsync.htm)|
Метод для компиляции перехода  
[CompileNodeAsync](M_Tessa_Compilation_Fake_FakeWorkflowEngineCompiler_CompileNodeAsync.htm)|
Метод для компиляции шаблона узла WorkflowEngine  
[CompileProcessAsync](M_Tessa_Compilation_Fake_FakeWorkflowEngineCompiler_CompileProcessAsync.htm)|
Метод для компиляции шаблона процесса WorkflowEngine  
[CompileTile](M_Tessa_Compilation_Fake_FakeWorkflowEngineCompiler_CompileTile.htm)|
Метод для компиляции тайла для шаблона процесса.  
[CompileTiles](M_Tessa_Compilation_Fake_FakeWorkflowEngineCompiler_CompileTiles.htm)|
Метод для компиляции тайлов для шаблона процесса.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetProcessSources](M_Tessa_Compilation_Fake_FakeWorkflowEngineCompiler_GetProcessSources.htm)|
Метод для получения скриптов процесса  
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
[Tessa.Compilation.Fake - пространство имён](N_Tessa_Compilation_Fake.htm)
