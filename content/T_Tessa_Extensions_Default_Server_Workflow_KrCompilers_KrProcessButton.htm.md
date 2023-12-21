# KrProcessButton - класс
Предоставляет информацию о вторичном процессе работающем в режиме "Кнопка".
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrProcessButton : KrSecondaryProcess, 
    	IKrProcessButton, IKrSecondaryProcess, IExecutionSources, IVisibilitySources
VB __Копировать
     Public NotInheritable Class KrProcessButton
    	Inherits KrSecondaryProcess
    	Implements IKrProcessButton, IKrSecondaryProcess, IExecutionSources, IVisibilitySources
C++ __Копировать
     public ref class KrProcessButton sealed : public KrSecondaryProcess, 
    	IKrProcessButton, IKrSecondaryProcess, IExecutionSources, IVisibilitySources
F# __Копировать
     [<SealedAttribute>]
    type KrProcessButton = 
        class
            inherit KrSecondaryProcess
            interface IKrProcessButton
            interface IKrSecondaryProcess
            interface IExecutionSources
            interface IVisibilitySources
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[KrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess.htm) __ KrProcessButton
Implements
    [IExecutionSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IExecutionSources.htm), [IKrProcessButton](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessButton.htm), [IKrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess.htm), [IVisibilitySources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IVisibilitySources.htm)
##  __Конструкторы
[KrProcessButton](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton__ctor.htm)|
Инициализирует новый экземпляр класса KrProcessButton.  
---|---  
## __Свойства
[ActionGrouping](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton_ActionGrouping.htm)|
Значение, показывающее, необходимо ли группировать тайл в группу "Действия".  
---|---  
[AskConfirmation](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton_AskConfirmation.htm)|
Спрашивать подтверждение перед выполнением.  
[Async](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_Async.htm)|
Возвращает значение, показывающе, что процесс допускает асинхронное
выполнение.  
(Унаследован от
[KrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess.htm))  
[ButtonHotkey](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton_ButtonHotkey.htm)|
Сочетание клавиш.  
[Caption](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton_Caption.htm)|
Отображаемое название кнопки.  
[Conditions](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton_Conditions.htm)|
Возвращает перечисление параметров условий.  
[ConfirmationMessage](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton_ConfirmationMessage.htm)|
Текст подтверждения перед выполнением.  
[ContextRolesIDs](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_ContextRolesIDs.htm)|
Возвращает cписок контекстных ролей, проверяемых перед выполнением процесса.  
(Унаследован от
[KrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess.htm))  
[ExecutionAccessDeniedMessage](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_ExecutionAccessDeniedMessage.htm)|
Возвращает сообщение о недоступности процесса для выполнения.  
(Унаследован от
[KrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess.htm))  
[ExecutionSourceCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_ExecutionSourceCondition.htm)|
Возвращает C# код, определяющий доступность выполнения.  
(Унаследован от
[KrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess.htm))  
[ExecutionSqlCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_ExecutionSqlCondition.htm)|
Возвращает текст SQL запроса с условием пределяющий доступность выполнения.  
(Унаследован от
[KrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess.htm))  
[Icon](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton_Icon.htm)|
Значок.  
[ID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_ID.htm)|
Возвращает идентификатор вторичного процесса.  
(Унаследован от
[KrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess.htm))  
[IsGlobal](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_IsGlobal.htm)|
Возвращает значение, показывающее, что процесс является глобальным.  
(Унаследован от
[KrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess.htm))  
[Name](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_Name.htm)|
Возвращает название вторичного процесса.  
(Унаследован от
[KrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess.htm))  
[NotMessageHasNoActiveStages](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_NotMessageHasNoActiveStages.htm)|
Возвращает значение, показывающее, что при отсутствии этапов, доступных для
выполнения, не должно отображаться сообщение.  
(Унаследован от
[KrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess.htm))  
[Order](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton_Order.htm)|
Порядок кнопки.  
[RefreshAndNotify](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton_RefreshAndNotify.htm)|
Значение, показывающее, необходимо ли проверить наличие новых заданий после
выполнения.  
[RunOnce](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_RunOnce.htm)|
Возвращает значение, показывающее, что процесс может быть запущен только один
раз в пределах одной и той же области выполнения процесса
([KrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope.htm)).  
(Унаследован от
[KrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess.htm))  
[TileGroup](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton_TileGroup.htm)|
Группа кнопки.  
[TileSize](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton_TileSize.htm)|
Размер кнопки.  
[Tooltip](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton_Tooltip.htm)|
Подсказка.  
[VisibilitySourceCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton_VisibilitySourceCondition.htm)|
Возвращает C# код, определяющий видимость.  
[VisibilitySqlCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton_VisibilitySqlCondition.htm)|
Возвращает текст SQL запроса с условием определяющим видимость.  
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
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
