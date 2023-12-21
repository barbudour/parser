# KrRuntimeStage - класс
Объект, предоставляющий информацию об этапе.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrRuntimeStage : IKrRuntimeStage, 
    	IRuntimeSources, IExtraSources
VB __Копировать
     Public NotInheritable Class KrRuntimeStage
    	Implements IKrRuntimeStage, IRuntimeSources, IExtraSources
C++ __Копировать
     public ref class KrRuntimeStage sealed : IKrRuntimeStage, 
    	IRuntimeSources, IExtraSources
F# __Копировать
     [<SealedAttribute>]
    type KrRuntimeStage = 
        class
            interface IKrRuntimeStage
            interface IRuntimeSources
            interface IExtraSources
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrRuntimeStage
Implements
    [IKrRuntimeStage](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage.htm), [IRuntimeSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IRuntimeSources.htm), [IExtraSources](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_IExtraSources.htm)
##  __Конструкторы
[KrRuntimeStage](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage__ctor.htm)|
Инициализирует новый экземпляр класса
[IKrRuntimeStage](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage.htm).  
---|---  
## __Свойства
[CanBeSkipped](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_CanBeSkipped.htm)|
Возвращает значение признака, показывающего, разрешено ли пропускать этап.  
---|---  
[ExtraSources](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_ExtraSources.htm)|
Возвращает список дополнительных методов.  
[GroupID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_GroupID.htm)|
Идентификатор группы, в которой находится шаблон, в котором находится этап.  
[GroupName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_GroupName.htm)|
Имя группы этапов, в которой находится шаблон, в котором находится этап.  
[GroupOrder](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_GroupOrder.htm)|
Порядок группы, в которой находится шаблон, в котором находится этап.  
[Hidden](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_Hidden.htm)|
Этап является скрытым.  
[Order](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_Order.htm)|
Порядок этапа в шаблоне.  
[Planned](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_Planned.htm)|
Дата выполнения.  
[RuntimeSourceAfter](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_RuntimeSourceAfter.htm)|
C# код сценария постобработки времени выполнения.  
[RuntimeSourceBefore](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_RuntimeSourceBefore.htm)|
C# код сценария инициализации времени выполнения.  
[RuntimeSourceCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_RuntimeSourceCondition.htm)|
C# код условия времени выполнения.  
[RuntimeSqlCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_RuntimeSqlCondition.htm)|
Текст SQL запроса условия времени выполнения.  
[Skip](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_Skip.htm)|
Флаг пропуска этапа.  
[SqlRoles](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_SqlRoles.htm)|
Запрос для вычисления SQL исполнителей.  
[StageID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_StageID.htm)|
Идентификатор этапа.  
[StageName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_StageName.htm)|
Название этапа.  
[StageTypeCaption](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_StageTypeCaption.htm)|
Отображаемое название типа этапа.  
[StageTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_StageTypeID.htm)|
Идентификатор типа этапа.  
[TemplateID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_TemplateID.htm)|
Идентификатор шаблона этапов.  
[TemplateName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_TemplateName.htm)|
Название шаблона этапов.  
[TimeLimit](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_TimeLimit.htm)|
Срок выполнения (рабочие дни).  
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
[GetSettingsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrRuntimeStage_GetSettingsAsync.htm)|
Возвращает параметры этапа.  
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
