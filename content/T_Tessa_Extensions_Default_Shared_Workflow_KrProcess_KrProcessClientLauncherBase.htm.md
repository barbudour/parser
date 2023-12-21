# KrProcessClientLauncherBase - класс
Базовый абстрактный класс предоставляющий методы для запуска процесса на
клиенте.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class KrProcessClientLauncherBase : IKrProcessLauncher
VB __Копировать
     Public MustInherit Class KrProcessClientLauncherBase
    	Implements IKrProcessLauncher
C++ __Копировать
     public ref class KrProcessClientLauncherBase abstract : IKrProcessLauncher
F# __Копировать
     [<AbstractClassAttribute>]
    type KrProcessClientLauncherBase = 
        class
            interface IKrProcessLauncher
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrProcessClientLauncherBase
Derived
[Tessa.Extensions.Default.Client.Workflow.KrProcess.KrProcessUILauncher](T_Tessa_Extensions_Default_Client_Workflow_KrProcess_KrProcessUILauncher.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.KrProcessClientLauncher](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientLauncher.htm)
Implements
    [IKrProcessLauncher](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrProcessLauncher.htm)
##  __Конструкторы
[KrProcessClientLauncherBase](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientLauncherBase__ctor.htm)|
Инициализирует новый экземпляр класса KrProcessClientLauncherBase  
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
[LaunchAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientLauncherBase_LaunchAsync.htm)|
Запускает указанный процесс.  
[LaunchCoreAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientLauncherBase_LaunchCoreAsync.htm)|
Запускает процесс.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[PrepareParametes](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientLauncherBase_PrepareParametes.htm)|
Обрабатывает параметры запуска процесса, которые должны быть добавлены в
дополнительную информацию используемую при запуске процесса.  
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
[LaunchWithCardEditorAsync](M_Tessa_Extensions_Default_Client_Workflow_KrProcess_KrProcessClientLauncherExtensions_LaunchWithCardEditorAsync.htm)|
Запускает указанный процесс с использованием заданного представления карточки
на клиенте (cardEditor).  
(Определяется
[KrProcessClientLauncherExtensions](T_Tessa_Extensions_Default_Client_Workflow_KrProcess_KrProcessClientLauncherExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
