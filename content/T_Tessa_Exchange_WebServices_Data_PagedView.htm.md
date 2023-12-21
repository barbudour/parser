# PagedView - класс
Represents a view settings that support paging in a search operation.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
    [EditorBrowsableAttribute(EditorBrowsableState.Never)]
    public abstract class PagedView : ViewBase
VB __Копировать
    <EditorBrowsableAttribute(EditorBrowsableState.Never)>
    Public MustInherit Class PagedView
    	Inherits ViewBase
C++ __Копировать
    [EditorBrowsableAttribute(EditorBrowsableState::Never)]
    public ref class PagedView abstract : public ViewBase
F# __Копировать
     [<AbstractClassAttribute>]
    [<EditorBrowsableAttribute(EditorBrowsableState.Never)>]
    type PagedView = 
        class
            inherit ViewBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ViewBase](T_Tessa_Exchange_WebServices_Data_ViewBase.htm) __ PagedView
Derived
[Tessa.Exchange.WebServices.Data.ConversationIndexedItemView](T_Tessa_Exchange_WebServices_Data_ConversationIndexedItemView.htm)
[Tessa.Exchange.WebServices.Data.FolderView](T_Tessa_Exchange_WebServices_Data_FolderView.htm)
[Tessa.Exchange.WebServices.Data.ItemView](T_Tessa_Exchange_WebServices_Data_ItemView.htm)
[Tessa.Exchange.WebServices.Data.PeopleIndexedItemView](T_Tessa_Exchange_WebServices_Data_PeopleIndexedItemView.htm)
##  __Свойства
[Offset](P_Tessa_Exchange_WebServices_Data_PagedView_Offset.htm)|  Gets or
sets the offset.  
---|---  
[OffsetBasePoint](P_Tessa_Exchange_WebServices_Data_PagedView_OffsetBasePoint.htm)|
Gets or sets the base point of the offset.  
[PageSize](P_Tessa_Exchange_WebServices_Data_PagedView_PageSize.htm)|  The
maximum number of items or folders the search operation should return.  
[PropertySet](P_Tessa_Exchange_WebServices_Data_ViewBase_PropertySet.htm)|
Gets or sets the property set. PropertySet determines which properties will be
loaded on found items. If PropertySet is null, all first class properties are
loaded on found items.  
(Унаследован от [ViewBase](T_Tessa_Exchange_WebServices_Data_ViewBase.htm))  
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
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
