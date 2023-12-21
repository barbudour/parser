# WorkplaceMetadataWalker<TContext> \- класс
Осуществляет обработку метаданных рабочего места в соответствии с политикой
доступности элементов рабочего места
## __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class WorkplaceMetadataWalker<TContext> : IWorkplaceMetadataWalker<TContext>
VB __Копировать
     Public Class WorkplaceMetadataWalker(Of TContext)
    	Implements IWorkplaceMetadataWalker(Of TContext)
C++ __Копировать
    generic<typename TContext>
    public ref class WorkplaceMetadataWalker : IWorkplaceMetadataWalker<TContext>
F# __Копировать
     type WorkplaceMetadataWalker<'TContext> = 
        class
            interface IWorkplaceMetadataWalker<'TContext>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkplaceMetadataWalker<TContext>
Implements
    [IWorkplaceMetadataWalker](T_Tessa_Views_AccessPolicy_IWorkplaceMetadataWalker_1.htm)<TContext>
#### Параметры типа
TContext
     Тип контекста 
## __Конструкторы
[WorkplaceMetadataWalker<TContext>](M_Tessa_Views_AccessPolicy_WorkplaceMetadataWalker_1__ctor.htm)|
Initializes a new instance of the WorkplaceMetadataWalker<TContext> class.  
---|---  
## __Методы
[ApplyAsync(IWorkplaceMetadata, TContext,
CancellationToken)](M_Tessa_Views_AccessPolicy_WorkplaceMetadataWalker_1_ApplyAsync.htm)|
Обрабатывает метаданные рабочего места metadata в соответствии с правилами
политики
[IWorkplaceAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_IWorkplaceAccessPolicy_1.htm)
и контекстом context  
---|---  
[ApplyAsync(IWorkplaceMetadata, TContext,
AccessRuleExecutor<IWorkplaceComponentMetadata, TContext>,
CancellationToken)](M_Tessa_Views_AccessPolicy_WorkplaceMetadataWalker_1_ApplyAsync_1.htm)|
Обрабатывает метаданные рабочего места metadata в соответствии с правилами
политики
[IWorkplaceAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_IWorkplaceAccessPolicy_1.htm)
и контекстом context  
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
