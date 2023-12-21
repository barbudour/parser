# StageTypeFilter - структура
Фильтр обработчиков типов этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public readonly struct StageTypeFilter : IKrProcessFilter<Guid>
VB __Копировать
     Public Structure StageTypeFilter
    	Implements IKrProcessFilter(Of Guid)
C++ __Копировать
     public value class StageTypeFilter : IKrProcessFilter<Guid>
F# __Копировать
     [<SealedAttribute>]
    type StageTypeFilter = 
        struct
            inherit ValueType
            interface IKrProcessFilter<Guid>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ StageTypeFilter
Implements
    [IKrProcessFilter](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessFilter_1.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __Свойства
[Excluded](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeFilter_Excluded.htm)|
Возвращает доступную только для чтения коллекцию исключённых объектов.  
---|---  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\))| Indicates whether this instance and a
specified object are equal.  
(Унаследован от
[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype))  
---|---  
[Exclude(Guid[])](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeFilter_Exclude_1.htm)|
Инициализирует новый фильтр обработчиков типов этапов заданным массивом
идентификаторов типов этапов исключаемых из обработчки.  
[Exclude(ICollection<Guid>)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeFilter_Exclude.htm)|
Инициализирует новый фильтр обработчиков типов этапов заданной коллекцией
идентификаторов типов этапов исключаемых из обработчки.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode)| Returns the hash code for this instance.  
(Унаследован от
[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype))  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring)| Returns the fully qualified type name of this instance.  
(Унаследован от
[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype))  
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
