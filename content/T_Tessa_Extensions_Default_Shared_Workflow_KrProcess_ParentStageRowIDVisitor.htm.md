# ParentStageRowIDVisitor - класс
Объект, устанавливающий значение поля
[ParentStageRowID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_ParentStageRowID.htm)
равным идентификатору строки секции верхнего уровня.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public class ParentStageRowIDVisitor : DescendantSectionsVisitor
VB __Копировать
     Public Class ParentStageRowIDVisitor
    	Inherits DescendantSectionsVisitor
C++ __Копировать
     public ref class ParentStageRowIDVisitor : public DescendantSectionsVisitor
F# __Копировать
     type ParentStageRowIDVisitor = 
        class
            inherit DescendantSectionsVisitor
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[DescendantSectionsVisitor](T_Tessa_Extensions_Default_Shared_Workflow_DescendantSectionsVisitor.htm) __ ParentStageRowIDVisitor
##  __Конструкторы
[ParentStageRowIDVisitor](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ParentStageRowIDVisitor__ctor.htm)|
Инициализирует новый экземпляр класса ParentStageRowIDVisitor.  
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
[VisitAsync](M_Tessa_Extensions_Default_Shared_Workflow_DescendantSectionsVisitor_VisitAsync.htm)|
Выполняет обход всех коллекционных секций, для которых предком является строка
из секции topLevelSectionName.  
(Унаследован от
[DescendantSectionsVisitor](T_Tessa_Extensions_Default_Shared_Workflow_DescendantSectionsVisitor.htm))  
[VisitNestedSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ParentStageRowIDVisitor_VisitNestedSection.htm)|
Выполняет посещение строки дочерней секции по отношению к секции верхнего
уровня.  
(Переопределяет [DescendantSectionsVisitor.VisitNestedSection(CardRow,
CardSection, Guid, Guid, IDictionary<Guid,
Guid>)](M_Tessa_Extensions_Default_Shared_Workflow_DescendantSectionsVisitor_VisitNestedSection.htm))  
[VisitTopLevelSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ParentStageRowIDVisitor_VisitTopLevelSection.htm)|
Выполняет посещение строки секции верхнего уровня.  
(Переопределяет [DescendantSectionsVisitor.VisitTopLevelSection(CardRow,
CardSection, IDictionary<Guid,
Guid>)](M_Tessa_Extensions_Default_Shared_Workflow_DescendantSectionsVisitor_VisitTopLevelSection.htm))  
##  __Поля
[CardMetadata](F_Tessa_Extensions_Default_Shared_Workflow_DescendantSectionsVisitor_CardMetadata.htm)|  
(Унаследован от
[DescendantSectionsVisitor](T_Tessa_Extensions_Default_Shared_Workflow_DescendantSectionsVisitor.htm))  
---|---  
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
