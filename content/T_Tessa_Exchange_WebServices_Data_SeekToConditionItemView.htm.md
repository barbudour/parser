# SeekToConditionItemView - класс
Represents the view settings in a folder search operation.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SeekToConditionItemView : ViewBase
VB __Копировать
     Public NotInheritable Class SeekToConditionItemView
    	Inherits ViewBase
C++ __Копировать
     public ref class SeekToConditionItemView sealed : public ViewBase
F# __Копировать
     [<SealedAttribute>]
    type SeekToConditionItemView = 
        class
            inherit ViewBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ViewBase](T_Tessa_Exchange_WebServices_Data_ViewBase.htm) __ SeekToConditionItemView
##  __Конструкторы
[SeekToConditionItemView(SearchFilter,
Int32)](M_Tessa_Exchange_WebServices_Data_SeekToConditionItemView__ctor.htm)|
Initializes a new instance of the SeekToConditionItemView class.  
---|---  
[SeekToConditionItemView(SearchFilter, Int32,
OffsetBasePoint)](M_Tessa_Exchange_WebServices_Data_SeekToConditionItemView__ctor_1.htm)|
Initializes a new instance of the SeekToConditionItemView class.  
## __Свойства
[Condition](P_Tessa_Exchange_WebServices_Data_SeekToConditionItemView_Condition.htm)|
Gets or sets the condition for seek. Available search filter classes include
SearchFilter.IsEqualTo, SearchFilter.ContainsSubstring and
SearchFilter.SearchFilterCollection. If SearchFilter is null, no search
filters are applied.  
---|---  
[OffsetBasePoint](P_Tessa_Exchange_WebServices_Data_SeekToConditionItemView_OffsetBasePoint.htm)|
Gets or sets the base point of the offset.  
[OrderBy](P_Tessa_Exchange_WebServices_Data_SeekToConditionItemView_OrderBy.htm)|
Gets the properties against which the returned items should be ordered.  
[PageSize](P_Tessa_Exchange_WebServices_Data_SeekToConditionItemView_PageSize.htm)|
The maximum number of items or folders the search operation should return.  
[PropertySet](P_Tessa_Exchange_WebServices_Data_ViewBase_PropertySet.htm)|
Gets or sets the property set. PropertySet determines which properties will be
loaded on found items. If PropertySet is null, all first class properties are
loaded on found items.  
(Унаследован от [ViewBase](T_Tessa_Exchange_WebServices_Data_ViewBase.htm))  
[Traversal](P_Tessa_Exchange_WebServices_Data_SeekToConditionItemView_Traversal.htm)|
Gets or sets the search traversal mode. Defaults to ItemTraversal.Shallow.  
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
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
