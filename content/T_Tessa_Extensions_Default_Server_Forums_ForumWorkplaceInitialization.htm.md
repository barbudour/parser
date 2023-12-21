# ForumWorkplaceInitialization - класс
Расширение скрывает узлы типовые дерева "Мои обсуждения" и "Последние
обсуждения" в рабочем месте "Пользователь", если не включён соответствующий
модуль лицензии. Без модуля невозможно перейти к обсуждениям из представления,
поэтому узлы рекомендуется скрыть.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Forums](N_Tessa_Extensions_Default_Server_Forums.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ForumWorkplaceInitialization : WorkplaceInitializationRule
VB __Копировать
     Public NotInheritable Class ForumWorkplaceInitialization
    	Inherits WorkplaceInitializationRule
C++ __Копировать
     public ref class ForumWorkplaceInitialization sealed : public WorkplaceInitializationRule
F# __Копировать
     [<SealedAttribute>]
    type ForumWorkplaceInitialization = 
        class
            inherit WorkplaceInitializationRule
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[WorkplaceInitializationRule](T_Tessa_Platform_Initialization_WorkplaceInitializationRule.htm) __ ForumWorkplaceInitialization
##  __Конструкторы
[ForumWorkplaceInitialization](M_Tessa_Extensions_Default_Server_Forums_ForumWorkplaceInitialization__ctor.htm)|
Инициализирует новый экземпляр класса ForumWorkplaceInitialization  
---|---  
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
[IsSatisfiedByAsync](M_Tessa_Extensions_Default_Server_Forums_ForumWorkplaceInitialization_IsSatisfiedByAsync.htm)|  
(Переопределяет
[WorkplaceInitializationRule.IsSatisfiedByAsync(IWorkplaceComponentMetadata,
IWorkplaceInitializationContext,
CancellationToken)](M_Tessa_Platform_Initialization_WorkplaceInitializationRule_IsSatisfiedByAsync.htm))  
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
[Tessa.Extensions.Default.Server.Forums - пространство
имён](N_Tessa_Extensions_Default_Server_Forums.htm)
