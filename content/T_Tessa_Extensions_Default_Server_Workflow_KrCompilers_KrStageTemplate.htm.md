# KrStageTemplate - класс
Объект, предоставляющий информацию об шаблоне этапов, необходимую для его
компиляции и выполнения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrStageTemplate : IKrStageTemplate, 
    	IDesignTimeSources
VB __Копировать
     Public NotInheritable Class KrStageTemplate
    	Implements IKrStageTemplate, IDesignTimeSources
C++ __Копировать
     public ref class KrStageTemplate sealed : IKrStageTemplate, 
    	IDesignTimeSources
F# __Копировать
     [<SealedAttribute>]
    type KrStageTemplate = 
        class
            interface IKrStageTemplate
            interface IDesignTimeSources
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrStageTemplate
Implements
    [IDesignTimeSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IDesignTimeSources.htm), [IKrStageTemplate](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrStageTemplate.htm)
##  __Конструкторы
[KrStageTemplate](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageTemplate__ctor.htm)|
Инициализирует новый экземпляр класса KrStageTemplate  
---|---  
##  __Свойства
[CanChangeOrder](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageTemplate_CanChangeOrder.htm)|
Возвращает значение, показывающее, можно ли перемещать этапы.  
---|---  
[ID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageTemplate_ID.htm)|
Возвращает идентификатор шаблона этапов.  
[IsStagesReadonly](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageTemplate_IsStagesReadonly.htm)|
Возвращает значение, показывающее, являются ли этапы нередактируемыми.  
[Name](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageTemplate_Name.htm)|
Возвращает название шаблона этапов.  
[Order](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageTemplate_Order.htm)|
Возвращает порядок шаблона.  
[Position](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageTemplate_Position.htm)|
Возвращает положение относительно этапов, добавленных вручную.  
[SourceAfter](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageTemplate_SourceAfter.htm)|
C# код сценария постобработки времени построения.  
[SourceBefore](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageTemplate_SourceBefore.htm)|
C# код сценария инициализации времени построения.  
[SourceCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageTemplate_SourceCondition.htm)|
C# код условия времени построения.  
[SqlCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageTemplate_SqlCondition.htm)|
Текст SQL запроса условия времени построения.  
[StageGroupID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageTemplate_StageGroupID.htm)|
Возвращает идентификатор группы этапов, к которой относится шаблон.  
[StageGroupName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageTemplate_StageGroupName.htm)|
Возвращает название группы этапов, к которой относится шаблон.  
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
