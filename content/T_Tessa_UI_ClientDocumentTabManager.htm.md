# ClientDocumentTabManager - класс
The client workplace item manager.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ClientDocumentTabManager : IDocumentTabManager
VB __Копировать
     Public NotInheritable Class ClientDocumentTabManager
    	Implements IDocumentTabManager
C++ __Копировать
     public ref class ClientDocumentTabManager sealed : IDocumentTabManager
F# __Копировать
     [<SealedAttribute>]
    type ClientDocumentTabManager = 
        class
            interface IDocumentTabManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ClientDocumentTabManager
Implements
    [IDocumentTabManager](T_Tessa_UI_Windows_IDocumentTabManager.htm)
##  __Конструкторы
[ClientDocumentTabManager](M_Tessa_UI_ClientDocumentTabManager__ctor.htm)|
Initializes a new instance of the ClientDocumentTabManager class.
Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
## __Свойства
[ActiveContext](P_Tessa_UI_ClientDocumentTabManager_ActiveContext.htm)|  Gets
Возвращает контекст текущего элемента  
---|---  
## __Методы
[ActivateCard](M_Tessa_UI_ClientDocumentTabManager_ActivateCard.htm)|
Осуществляет активацию карточки  
---|---  
[CloseCardAsync](M_Tessa_UI_ClientDocumentTabManager_CloseCardAsync.htm)|
Закрывает карточку  
[CloseWorkplace](M_Tessa_UI_ClientDocumentTabManager_CloseWorkplace.htm)|
Осуществляет закрытие узла, открытого в отдельном окне  
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
[GetContextMenuAsync](M_Tessa_UI_ClientDocumentTabManager_GetContextMenuAsync.htm)|
Создаёт контекстное меню, которое относится к вкладке.  
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
[OpenCardAsync](M_Tessa_UI_ClientDocumentTabManager_OpenCardAsync.htm)|  The
open card.  
[OpenWorkplaceAsync(IWorkplaceViewModel, Boolean,
CancellationToken)](M_Tessa_UI_ClientDocumentTabManager_OpenWorkplaceAsync_1.htm)|
Осуществляет отображение модели рабочего места  
[OpenWorkplaceAsync(IWorkplaceCreationContext, Boolean, Int32, String,
CancellationToken)](M_Tessa_UI_ClientDocumentTabManager_OpenWorkplaceAsync.htm)|
Осуществляет создание и открытие нового рабочего места.  
[OpenWorkplaceAsync(IWorkplaceMetadata, IEnumerable<RequestParameter>,
Boolean, Boolean, Visibility, Boolean, WorkplaceOpenPosition, String,
CancellationToken)](M_Tessa_UI_ClientDocumentTabManager_OpenWorkplaceAsync_2.htm)|
Осуществляет создание и открытие нового рабочего места.  
[OpenWorkplaceItem](M_Tessa_UI_ClientDocumentTabManager_OpenWorkplaceItem.htm)|
Осуществляет открытие элемента рабочей области  
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
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
