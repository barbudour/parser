# AdvancedDialogCommandHandler - класс
Базовый класс обработчика клиентской команды отображения диалога.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Workflow.KrProcess.CommandInterpreter](N_Tessa_Extensions_Default_Client_Workflow_KrProcess_CommandInterpreter.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class AdvancedDialogCommandHandler : ClientCommandHandlerBase
VB __Копировать
     Public MustInherit Class AdvancedDialogCommandHandler
    	Inherits ClientCommandHandlerBase
C++ __Копировать
     public ref class AdvancedDialogCommandHandler abstract : public ClientCommandHandlerBase
F# __Копировать
     [<AbstractClassAttribute>]
    type AdvancedDialogCommandHandler = 
        class
            inherit ClientCommandHandlerBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ClientCommandHandlerBase](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_ClientCommandHandlerBase.htm) __ AdvancedDialogCommandHandler
Derived
[Tessa.Extensions.Default.Client.Workflow.KrProcess.CommandInterpreter.KrAdvancedDialogCommandHandler](T_Tessa_Extensions_Default_Client_Workflow_KrProcess_CommandInterpreter_KrAdvancedDialogCommandHandler.htm)
[Tessa.Extensions.Default.Client.Workflow.WorkflowEngine.WeAdvancedDialogCommandHandler](T_Tessa_Extensions_Default_Client_Workflow_WorkflowEngine_WeAdvancedDialogCommandHandler.htm)
##  __Конструкторы
[AdvancedDialogCommandHandler](M_Tessa_Extensions_Default_Client_Workflow_KrProcess_CommandInterpreter_AdvancedDialogCommandHandler__ctor.htm)|
Инициализирует новый экземпляр класса AdvancedDialogCommandHandler  
---|---  
##  __Методы
[CompleteDialogCoreAsync](M_Tessa_Extensions_Default_Client_Workflow_KrProcess_CommandInterpreter_AdvancedDialogCommandHandler_CompleteDialogCoreAsync.htm)|
Метод выполнения диалога.  
---|---  
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
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Handle](M_Tessa_Extensions_Default_Client_Workflow_KrProcess_CommandInterpreter_AdvancedDialogCommandHandler_Handle.htm)|
Обработать клиентскую команду.  
(Переопределяет
[ClientCommandHandlerBase.Handle(IClientCommandHandlerContext)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_ClientCommandHandlerBase_Handle.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[PrepareDialogCommand](M_Tessa_Extensions_Default_Client_Workflow_KrProcess_CommandInterpreter_AdvancedDialogCommandHandler_PrepareDialogCommand.htm)|
Метод для подготовки диалога для выполнения.  
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
[Tessa.Extensions.Default.Client.Workflow.KrProcess.CommandInterpreter -
пространство
имён](N_Tessa_Extensions_Default_Client_Workflow_KrProcess_CommandInterpreter.htm)
