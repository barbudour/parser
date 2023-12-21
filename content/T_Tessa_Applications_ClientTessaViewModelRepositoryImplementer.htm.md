# ClientTessaViewModelRepositoryImplementer - класс
Клиентский репозиторий для обращения к сервису представлений
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ClientTessaViewModelRepositoryImplementer : IRepository<IGetModelRequest, IStoreTessaViewRequest, IEnumerable<TessaViewModel>>
VB __Копировать
     Public NotInheritable Class ClientTessaViewModelRepositoryImplementer
    	Implements IRepository(Of IGetModelRequest, IStoreTessaViewRequest, IEnumerable(Of TessaViewModel))
C++ __Копировать
     public ref class ClientTessaViewModelRepositoryImplementer sealed : IRepository<IGetModelRequest^, IStoreTessaViewRequest^, IEnumerable<TessaViewModel^>^>
F# __Копировать
     [<SealedAttribute>]
    type ClientTessaViewModelRepositoryImplementer = 
        class
            interface IRepository<IGetModelRequest, IStoreTessaViewRequest, IEnumerable<TessaViewModel>>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ClientTessaViewModelRepositoryImplementer
Implements
    [IRepository](T_Tessa_Views_IRepository_3.htm)<[IGetModelRequest](T_Tessa_Views_IGetModelRequest.htm), [IStoreTessaViewRequest](T_Tessa_Views_IStoreTessaViewRequest.htm), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[TessaViewModel](T_Tessa_Views_TessaViewModel.htm)>>
##  __Конструкторы
[ClientTessaViewModelRepositoryImplementer](M_Tessa_Applications_ClientTessaViewModelRepositoryImplementer__ctor.htm)|
Initializes a new instance of the ClientTessaViewModelRepositoryImplementer
class.  
---|---  
## __Методы
[ChangeAsync](M_Tessa_Applications_ClientTessaViewModelRepositoryImplementer_ChangeAsync.htm)|
Осуществляет изменение элементов хранилища  
---|---  
[DeleteAsync](M_Tessa_Applications_ClientTessaViewModelRepositoryImplementer_DeleteAsync.htm)|
Удаляет элементы из хранилища  
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
[GetAsync](M_Tessa_Applications_ClientTessaViewModelRepositoryImplementer_GetAsync.htm)|
Возвращает элементы из хранилища  
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
[ImportAsync](M_Tessa_Applications_ClientTessaViewModelRepositoryImplementer_ImportAsync.htm)|
Осуществляет пакетное добавление списка элементов  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[NewAsync](M_Tessa_Applications_ClientTessaViewModelRepositoryImplementer_NewAsync.htm)|
Осуществляет создание новоых элементов в хранилище  
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
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
