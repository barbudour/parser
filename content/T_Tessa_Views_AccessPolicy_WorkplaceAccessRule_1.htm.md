# WorkplaceAccessRule<TContext> \- класс
##  __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class WorkplaceAccessRule<TContext> : IWorkplaceAccessRule<TContext>, 
    	IAccessRule<IWorkplaceComponentMetadata, TContext>
VB __Копировать
     Public Class WorkplaceAccessRule(Of TContext)
    	Implements IWorkplaceAccessRule(Of TContext), IAccessRule(Of IWorkplaceComponentMetadata, TContext)
C++ __Копировать
    generic<typename TContext>
    public ref class WorkplaceAccessRule : IWorkplaceAccessRule<TContext>, 
    	IAccessRule<IWorkplaceComponentMetadata^, TContext>
F# __Копировать
     type WorkplaceAccessRule<'TContext> = 
        class
            interface IWorkplaceAccessRule<'TContext>
            interface IAccessRule<IWorkplaceComponentMetadata, 'TContext>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkplaceAccessRule<TContext>
Implements
    [IAccessRule](T_Tessa_Views_AccessPolicy_IAccessRule_2.htm)<[IWorkplaceComponentMetadata](T_Tessa_Views_Workplaces_IWorkplaceComponentMetadata.htm), TContext>, [IWorkplaceAccessRule](T_Tessa_Views_AccessPolicy_IWorkplaceAccessRule_1.htm)<TContext>
#### Параметры типа
TContext
##  __Конструкторы
[WorkplaceAccessRule<TContext>](M_Tessa_Views_AccessPolicy_WorkplaceAccessRule_1__ctor.htm)|
Инициализирует новый экземпляр класса WorkplaceAccessRule<TContext>  
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
[IsSatisfiedByAsync](M_Tessa_Views_AccessPolicy_WorkplaceAccessRule_1_IsSatisfiedByAsync.htm)|
Выполняет проверку доступности объекта subject  
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
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
