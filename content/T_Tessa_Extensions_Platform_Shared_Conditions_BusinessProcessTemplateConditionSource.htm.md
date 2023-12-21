# BusinessProcessTemplateConditionSource - класс
Источник данных для условий, получающий данные из карточки шаблона бизнес-
процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Shared.Conditions](N_Tessa_Extensions_Platform_Shared_Conditions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class BusinessProcessTemplateConditionSource : IConditionSource
VB __Копировать
     Public Class BusinessProcessTemplateConditionSource
    	Implements IConditionSource
C++ __Копировать
     public ref class BusinessProcessTemplateConditionSource : IConditionSource
F# __Копировать
     type BusinessProcessTemplateConditionSource = 
        class
            interface IConditionSource
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ BusinessProcessTemplateConditionSource
Implements
    [IConditionSource](T_Tessa_Platform_Conditions_IConditionSource.htm)
##  __Заметки
По умолчанию обрабатывает действие
[WorkflowConditionActionTypeID](F_Tessa_Workflow_Actions_WorkflowActionTypes_WorkflowConditionActionTypeID.htm).
## __Конструкторы
[BusinessProcessTemplateConditionSource](M_Tessa_Extensions_Platform_Shared_Conditions_BusinessProcessTemplateConditionSource__ctor.htm)|
Создаёт экземпляр класса с указанием занчений его полей.  
---|---  
## __Свойства
[ConditionRows](P_Tessa_Extensions_Platform_Shared_Conditions_BusinessProcessTemplateConditionSource_ConditionRows.htm)|
Список строк с данными условий.  
---|---  
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
[GetConditionRowsFromAction](M_Tessa_Extensions_Platform_Shared_Conditions_BusinessProcessTemplateConditionSource_GetConditionRowsFromAction.htm)|
Метод для получения списка строк с условиями из действия.  
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
[Store](M_Tessa_Extensions_Platform_Shared_Conditions_BusinessProcessTemplateConditionSource_Store.htm)|
Выполняет сохранение условий из
[ConditionRows](P_Tessa_Platform_Conditions_IConditionSource_ConditionRows.htm)
в карточку, по которой создан данный источник условий.  
[StoreConditionsToAction](M_Tessa_Extensions_Platform_Shared_Conditions_BusinessProcessTemplateConditionSource_StoreConditionsToAction.htm)|
Метод сохранения списка строк с условиями в действии.  
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
[Tessa.Extensions.Platform.Shared.Conditions - пространство
имён](N_Tessa_Extensions_Platform_Shared_Conditions.htm)
