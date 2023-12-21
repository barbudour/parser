# StageTypeDescriptor - класс
Дескриптор типа этапа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class StageTypeDescriptor
VB __Копировать
     Public NotInheritable Class StageTypeDescriptor
C++ __Копировать
     public ref class StageTypeDescriptor sealed
F# __Копировать
     [<SealedAttribute>]
    type StageTypeDescriptor = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ StageTypeDescriptor
##  __Свойства
[CanBeHidden](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_CanBeHidden.htm)|
Разрешить скрывать этап в документах.  
---|---  
[CanBeSkipped](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_CanBeSkipped.htm)|
Возвращает значение, показывающее, разрешён ли пропуск этапа.  
[CanOverrideAuthor](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_CanOverrideAuthor.htm)|
Использовать поле "От имени"  
[CanOverrideTaskHistoryGroup](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_CanOverrideTaskHistoryGroup.htm)|
Разрешить переопределять группу истории заданий в настройках этапа.  
[Caption](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_Caption.htm)|
Название типа этапа.  
[DefaultStageName](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_DefaultStageName.htm)|
Стандартное название для нового этапа.  
[ID](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_ID.htm)|
Уникальный идентификатор дескриптора типа этапа.  
[PerformerCaption](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_PerformerCaption.htm)|
Заголовок элемента управления исполнителя/исполнителей.  
[PerformerIsRequired](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_PerformerIsRequired.htm)|
Проверить наличие хотя бы одного исполнителя при редактировании в UI и перед
стартом этапа.  
[PerformerUsageMode](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_PerformerUsageMode.htm)|
Режим использования стандартного поля с исполнителями.  
[SettingsCardTypeID](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_SettingsCardTypeID.htm)|
Идентификатор типа карточки настроек.  
[SupportedModes](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_SupportedModes.htm)|
Поддерживаемые режимы выполнения.  
[UsePlanned](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_UsePlanned.htm)|
Использовать поле "Дата выполнения"  
[UseTaskKind](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_UseTaskKind.htm)|
Разрешить выбирать вид задания.  
[UseTimeLimit](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_UseTimeLimit.htm)|
Использовать поле "Срок"  
## __Методы
[Create](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_Create.htm)|
Создать новый дескриптор.  
---|---  
[CreateBasedOn](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_CreateBasedOn.htm)|
Создать дескриптор на основании существующего. Переопределение идентификатора
[ID](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_ID.htm)
является обязательным.  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor_ToString.htm)|
Returns a string that represents the current object.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
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
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
