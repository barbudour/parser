# DialogStageTypeHandler.ScriptContext - класс
Контекст скрипта валидации.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ScriptContext : DialogStageTypeHandler.ScriptContextBase
VB __Копировать
     Public NotInheritable Class ScriptContext
    	Inherits DialogStageTypeHandler.ScriptContextBase
C++ __Копировать
     public ref class ScriptContext sealed : public DialogStageTypeHandler.ScriptContextBase
F# __Копировать
     [<SealedAttribute>]
    type ScriptContext = 
        class
            inherit DialogStageTypeHandler.ScriptContextBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[DialogStageTypeHandler.ScriptContextBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase.htm) __ DialogStageTypeHandler.ScriptContext
##  __Конструкторы
[DialogStageTypeHandler.ScriptContext](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContext__ctor.htm)|
Инициализирует новый экземпляр класса DialogStageTypeHandler.ScriptContext.  
---|---  
## __Свойства
[ButtonName](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase_ButtonName.htm)|
Алиас нажатой кнопки.  
(Унаследован от
[DialogStageTypeHandler.ScriptContextBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase.htm))  
---|---  
[Cancel](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContext_Cancel.htm)|
Возвращает или задаёт флаг, позволяющий прервать обработку диалога без
закрытия окна диалога.  
[CompleteDialog](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContext_CompleteDialog.htm)|
Возвращает или задаёт флаг, позволяющий отменить завершение диалога с
закрытием окна диалога.  
[StoreMode](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase_StoreMode.htm)|  
(Унаследован от
[DialogStageTypeHandler.ScriptContextBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase.htm))  
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
[GetDialogCardAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase_GetDialogCardAsync.htm)|
Возвращает карточку диалога.  
(Унаследован от
[DialogStageTypeHandler.ScriptContextBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase.htm))  
[GetFileContainerAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase_GetFileContainerAsync.htm)|
Возвращает файловый контейнер для карточки диалога с временем жизни карточка и
задание.  
(Унаследован от
[DialogStageTypeHandler.ScriptContextBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase.htm))  
[GetFileContentAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase_GetFileContentAsync.htm)|
Возвращает контент файла карточки диалога с временем жизни: запрос или
задание.  
(Унаследован от
[DialogStageTypeHandler.ScriptContextBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase.htm))  
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
[SetFileContent](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase_SetFileContent.htm)|
Задаёт контент файла карточки диалога с временем жизни запрос.  
(Унаследован от
[DialogStageTypeHandler.ScriptContextBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[dialogCardAccessStrategy](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase_dialogCardAccessStrategy.htm)|
Стратегия доступа к карточке диалога.  
(Унаследован от
[DialogStageTypeHandler.ScriptContextBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase.htm))  
---|---  
[session](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase_session.htm)|  
(Унаследован от
[DialogStageTypeHandler.ScriptContextBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ScriptContextBase.htm))  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)
