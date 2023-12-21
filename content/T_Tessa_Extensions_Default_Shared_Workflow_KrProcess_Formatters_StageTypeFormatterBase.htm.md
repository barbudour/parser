# StageTypeFormatterBase - класс
Предоставляет базовую реализацию форматтера типа этапа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class StageTypeFormatterBase : IStageTypeFormatter
VB __Копировать
     Public MustInherit Class StageTypeFormatterBase
    	Implements IStageTypeFormatter
C++ __Копировать
     public ref class StageTypeFormatterBase abstract : IStageTypeFormatter
F# __Копировать
     [<AbstractClassAttribute>]
    type StageTypeFormatterBase = 
        class
            interface IStageTypeFormatter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ StageTypeFormatterBase
Derived
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.AcquaintanceStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_AcquaintanceStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.AddFileFromTemplateStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_AddFileFromTemplateStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.ApprovalStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_ApprovalStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.ChangeStateStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_ChangeStateStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.CreateCardStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_CreateCardStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.DialogsStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_DialogsStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.EditStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_EditStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.ForkManagementStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_ForkManagementStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.ForkStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_ForkStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.HistoryManagementStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_HistoryManagementStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.NotificationStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_NotificationStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.ProcessManagementStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_ProcessManagementStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.RegistrationStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_RegistrationStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.ResolutionStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_ResolutionStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.SigningStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_SigningStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.TypedTaskStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_TypedTaskStageTypeFormatter.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters.UniversalTaskStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_UniversalTaskStageTypeFormatter.htm)
Подробнее __Less __
Implements
    [IStageTypeFormatter](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatter.htm)
##  __Конструкторы
[StageTypeFormatterBase](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterBase__ctor.htm)|
Инициализирует новый экземпляр класса StageTypeFormatterBase  
---|---  
##  __Методы
[AppendExtendedLocalization](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterBase_AppendExtendedLocalization.htm)|
Добавляет указанную строку в формате расширенной локализации, если она
является строкой локализации.  
---|---  
[AppendString](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterBase_AppendString.htm)|
Добавляет форматированную строку с описанием настройки этапа в builder.  
[DefaultDateFormatting](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterBase_DefaultDateFormatting.htm)|
Задаёт отображаемый строк исполнения.  
[DefaultSinglePerformerFormatting](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterBase_DefaultSinglePerformerFormatting.htm)|
Задаёт отображаемый список участников состоящий из одного указанного
исполнителя.  
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
[FormatClientAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterBase_FormatClientAsync.htm)|
Выполняет форматирование ячеек на клиенте.  
[FormatServerAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterBase_FormatServerAsync.htm)|
Выполняет форматирование ячеек на сервере.  
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
[ToExtendedLocalization](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterBase_ToExtendedLocalization.htm)|
Преобразует указанную строку в формат расширенной локализации, если она
является строкой локализации.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[DefaultSettingMax](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterBase_DefaultSettingMax.htm)|
Максимальная длина значения параметра выводимая при форматировании на клиенте.  
---|---  
## __Методы расширения
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
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)
